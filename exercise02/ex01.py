import numpy as np

def create_gradient_image(height, width):
    img = np.zeros((height, width), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            img[y, x] = (255 * (x + y)) // (height + width - 2)

    return img
