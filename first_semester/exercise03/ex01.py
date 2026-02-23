import sys
import numpy as np
import cv2

if len(sys.argv) != 4:
    print("Usage: python color_convert.py R G B")
    sys.exit(1)

R = int(sys.argv[1])
G = int(sys.argv[2])
B = int(sys.argv[3])

r = R / 255.0
g = G / 255.0
b = B / 255.0

cmax = max(r, g, b)
cmin = min(r, g, b)
delta = cmax - cmin

if delta == 0:
    H_hsv = 0
elif cmax == r:
    H_hsv = 60 * (((g - b) / delta) % 6)
elif cmax == g:
    H_hsv = 60 * (((b - r) / delta) + 2)
else:
    H_hsv = 60 * (((r - g) / delta) + 4)

S_hsv = 0 if cmax == 0 else delta / cmax

V = cmax

HSV_manual = (H_hsv, S_hsv, V)

L = (cmax + cmin) / 2

if delta == 0:
    S_hsl = 0
else:
    S_hsl = delta / (1 - abs(2 * L - 1))

H_hsl = H_hsv  

HSL_manual = (H_hsl, S_hsl, L)

Y  = 0.299 * R + 0.587 * G + 0.114 * B
Cr = (R - Y) * 0.713 + 128
Cb = (B - Y) * 0.564 + 128

YCrCb_manual = (Y, Cr, Cb)

pixel = np.array([[[B, G, R]]], dtype=np.uint8)

HSV_cv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)[0][0]
HSL_cv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HLS)[0][0]  # HLS = HSL ב־OpenCV
YCrCb_cv = cv2.cvtColor(pixel, cv2.COLOR_BGR2YCrCb)[0][0]

print("=== Manual Calculations ===")
print("HSV:", HSV_manual)
print("HSL:", HSL_manual)
print("YCrCb:", YCrCb_manual)

print("\n=== OpenCV Calculations ===")
print("HSV:", HSV_cv)
print("HSL:", HSL_cv)
print("YCrCb:", YCrCb_cv)

print("\n=== Differences ===")
print("HSV diff:", np.array(HSV_manual) - HSV_cv)
print("HSL diff:", np.array(HSL_manual) - HSL_cv)
print("YCrCb diff:", np.array(YCrCb_manual) - YCrCb_cv)
