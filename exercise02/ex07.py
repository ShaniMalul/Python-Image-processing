import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_manual_histogram(img):
    hist = [0] * 256
    for row in img:
        for pixel_value in row:
            hist[pixel_value] += 1
            
    return hist


input_path = 'my_image_grayscale_cv2.png'
gray_img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

if gray_img is None:
    print("שגיאה: הקובץ לא נמצא.")
else:
    manual_hist = calculate_manual_histogram(gray_img)
    plt.figure(figsize=(10, 5))
    

    plt.subplot(1, 2, 1)
    plt.imshow(gray_img, cmap='gray', vmin=0, vmax=255)
    plt.title("Grayscale Image")
    
    plt.subplot(1, 2, 2)

    plt.bar(range(256), manual_hist, color='black', width=1.0)
    plt.title("Manual Histogram (No Library Func)")
    plt.xlabel("Pixel Value (0-255)")
    plt.ylabel("Number of Pixels")
    
    plt.tight_layout()
    plt.show()