import matplotlib.pyplot as plt
from ex04 import create_low_contrast_image
from ex05 import normalize

img_q6 = create_low_contrast_image(100, 105)
img_q6[0, 0] = 0 
img_q6[0, 1] = 255 
normalized_q6 = normalize(img_q6)

plt.figure(figsize=(6, 6))
plt.imshow(normalized_q6, cmap='gray', vmin=0, vmax=255)
plt.title("Question 6: Normalized with Outliers")
plt.show()