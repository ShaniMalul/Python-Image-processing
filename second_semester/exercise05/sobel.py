import cv2
import numpy as np
import sys


def normalize(img):
    img = img - np.min(img)
    img = img / np.max(img)
    return (img * 255).astype(np.uint8)


def sobel(image_path):
    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gx_kernel = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], dtype=np.float32)

    gy_kernel = np.array([
        [-1, -2, -1],
        [0,  0,  0],
        [1,  2,  1]
    ], dtype=np.float32)

    gx = cv2.filter2D(gray.astype(np.float32), -1, gx_kernel)
    gy = cv2.filter2D(gray.astype(np.float32), -1, gy_kernel)

    gx_abs = normalize(np.abs(gx))
    gy_abs = normalize(np.abs(gy))

    G = np.sqrt(gx**2 + gy**2)
    G = normalize(G)

    cv2.imwrite("image_grayscale.jpg", gray)
    cv2.imwrite("image_gx.jpg", gx_abs)
    cv2.imwrite("image_gy.jpg", gy_abs)
    cv2.imwrite("image_magnitude.jpg", G)


if __name__ == "__main__":
    sobel(sys.argv[1])