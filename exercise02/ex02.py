import cv2
import numpy as np
def brightening_func(img, b, func):
    if func == "cv2":
        return cv2.add(img, np.array([float(b)]).astype(img.dtype))
    
    elif func == "+":
        return img + b