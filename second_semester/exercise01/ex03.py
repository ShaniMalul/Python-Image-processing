import numpy as np
import matplotlib.pyplot as plt
import math

theta_deg = 30
theta_rad = math.radians(theta_deg)

r_30 = np.array([
    [math.cos(theta_rad), -math.sin(theta_rad)],
    [math.sin(theta_rad),  math.cos(theta_rad)]
])

print("30_r =")
print(r_30)

s_2x = np.array([
    [2, 0],
    [0, 1]
])

print("\n2_sx =")
print(s_2x)


rs = s_2x @ r_30
print("\nrs = 2_sx @ 30_r =")
print(rs)

sr = r_30 @ s_2x
print("\nsr = 30_r @ 2_sx =")
print(sr)

rectangle = np.array([
    [-1, -0.5],
    [ 1, -0.5],
    [ 1,  0.5],
    [-1,  0.5],
    [-1, -0.5]  
]).T  

rect_rotated = r_30 @ rectangle

rect_scaled = s_2x @ rectangle

rect_sr = sr @ rectangle
rect_rs = rs @ rectangle

plt.figure()

plt.plot(rectangle[0], rectangle[1], label="Original")
plt.plot(rect_rotated[0], rect_rotated[1], label="Rotated (30°)")
plt.plot(rect_scaled[0], rect_scaled[1], label="Scaled x2 (x-axis)")
plt.plot(rect_sr[0], rect_sr[1], label="sr = R @ S")
plt.plot(rect_rs[0], rect_rs[1], label="rs = S @ R")

plt.axhline(0)
plt.axvline(0)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title("Rectangle Transformations")
plt.show()