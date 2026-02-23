import cv2
import numpy as np
import matplotlib.pyplot as plt
from ex01 import create_gradient_image
from ex02 import brightening_func

original_img = create_gradient_image(255, 255)


res_cv2 = brightening_func(original_img, 100, "cv2") 
res_plus = brightening_func(original_img, 100, "+") 

plt.figure(figsize=(8, 3)) 

plt.subplot(1, 3, 1)
plt.imshow(original_img, cmap='gray', vmin=0, vmax=255)
plt.title("Original", fontsize=10)

plt.subplot(1, 3, 2)
plt.imshow(res_cv2, cmap='gray', vmin=0, vmax=255)
plt.title("CV2 Add", fontsize=10)

plt.subplot(1, 3, 3)
plt.imshow(res_plus, cmap='gray', vmin=0, vmax=255)
plt.title("Modulo Add", fontsize=10)

plt.tight_layout()
plt.show()
