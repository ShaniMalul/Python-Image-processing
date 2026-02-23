import cv2
import numpy as np
import matplotlib.pyplot as plt

def normalize(img):
    src_float = img.astype(np.float32)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img)
    mean_val = np.mean(img)
    diff = max_val - min_val
    stretch_factor = 255.0 / diff if diff != 0 else 1.0
    print(f"Min: {min_val}, Max: {max_val}, Mean: {mean_val:.2f}")
    print(f"Stretch Factor: {stretch_factor:.2f}")
    dst_float = (src_float - min_val) * stretch_factor
    
    return np.clip(dst_float, 0, 255).astype(np.uint8)


filename = 'my_image_grayscale_cv2.png' 
gray_img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

if gray_img is None:
    print(f"Error: Could not find grayscale image '{filename}'")
else:

    normalized_img = normalize(gray_img)
    

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(gray_img, cmap='gray', vmin=0, vmax=255)
    plt.title("Original (From Convert File)")
    
    plt.subplot(1, 2, 2)
    plt.imshow(normalized_img, cmap='gray', vmin=0, vmax=255)
    plt.title("After Normalization")
    
    plt.show()