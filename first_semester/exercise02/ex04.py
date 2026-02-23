import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_low_contrast_image(bg, fg, height=300, width=300):
    image = np.full((height, width), bg, dtype=np.uint8) 
    center = (width // 2, height // 2) 
    radius = 50
    cv2.circle(image, center, radius, fg, -1)
    return image

low_contrast_img = create_low_contrast_image(100, 105)

plt.imshow(low_contrast_img, cmap='gray', vmin=0, vmax=255)
plt.title("Low Contrast Image (Background: 100, Circle: 105)")
plt.show()