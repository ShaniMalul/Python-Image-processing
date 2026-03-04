import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# מטריצות טרנספורמציה
# -------------------------

def matrix_rotation(theta):
    theta_rad = np.deg2rad(theta)
    return np.array([
        [np.cos(theta_rad), -np.sin(theta_rad), 0],
        [np.sin(theta_rad),  np.cos(theta_rad), 0],
        [0, 0, 1]
    ])

def matrix_scale(sx, sy=None):
    if sy is None:
        sy = sx
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

# -------------------------
# יצירת מלבן מרכזו בראשית
# גובה = 1, רוחב = 2
# -------------------------

# חצי רוחב = 1
# חצי גובה = 0.5

rectangle = np.array([
    [-1, -0.5, 1],
    [ 1, -0.5, 1],
    [ 1,  0.5, 1],
    [-1,  0.5, 1],
    [-1, -0.5, 1]   # לסגירת הצורה
]).T  # מטריצה בגודל 3×N

# -------------------------
# טרנספורמציות
# -------------------------

# ב. סיבוב 30 מעלות
rect_rot30 = matrix_rotation(30) @ rectangle

# ג. סיבוב 45 ואז מתיחה פי 2 בציר x
rect_rot45_scale = matrix_scale(2, 1) @ matrix_rotation(45) @ rectangle

# ד. מתיחה ואז סיבוב 45
rect_scale_rot45 = matrix_rotation(45) @ matrix_scale(2, 1) @ rectangle

# -------------------------
# ציור
# -------------------------

plt.figure(figsize=(8,8))

# א. המלבן המקורי
plt.plot(rectangle[0], rectangle[1], label="Original")

# ב. סיבוב 30
plt.plot(rect_rot30[0], rect_rot30[1], label="Rotate 30°")

# ג. סיבוב ואז מתיחה
plt.plot(rect_rot45_scale[0], rect_rot45_scale[1], 
         label="Rotate 45° then Scale x2")

# ד. מתיחה ואז סיבוב
plt.plot(rect_scale_rot45[0], rect_scale_rot45[1], 
         label="Scale x2 then Rotate 45°")

plt.axhline(0)
plt.axvline(0)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title("Homogeneous Transformations of a Rectangle")
plt.grid()
plt.show()