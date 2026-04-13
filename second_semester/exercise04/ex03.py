import cv2
import time
import pandas as pd
from ex01 import warp_numpy_nearest
from ex02 import warp_bilinear_python

def measure_time(func, image, theta, sx, sy):
    start = time.perf_counter()
    func(image, theta, sx, sy)
    end = time.perf_counter()
    return end - start


image = cv2.imread("input.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

sizes = [(256, 256), (512, 512), (1024, 1024)]
theta, sx, sy = 30, 1.2, 0.8

results = []

for h, w in sizes:
    resized = cv2.resize(image, (w, h))

    t_numpy = measure_time(
        warp_numpy_nearest, resized, theta, sx, sy
    )
    t_bilinear = measure_time(
        warp_bilinear_python, resized, theta, sx, sy
    )

    results.append([h, w, t_numpy, t_bilinear])

df = pd.DataFrame(results, columns=[
    "אורך", "רוחב",
    "זמן ריצה - NumPy (Nearest)",
    "זמן ריצה - Bilinear (Python)"
])

print(df)