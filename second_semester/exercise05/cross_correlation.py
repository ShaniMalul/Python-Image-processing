import numpy as np
from scipy import signal

def initialize_kernel():
    # יצירת ה-kernel כפי שמופיע בטבלה בתרגיל [cite: 148, 158]
    kernel = np.array([
        [-1, 2, 1],
        [-2, 1, -3],
        [3, 0, -1]
    ], dtype=np.float32)
    return kernel

def get_image():
    # יצירת התמונה כפי שמופיעה בטבלה בתרגיל [cite: 149, 161]
    image = np.array([
        [103, 102, 101, 100],
        [104, 103, 102, 101],
        [53, 52, 51, 50],
        [45, 53, 52, 51]
    ], dtype=np.uint8)
    return image

def cross_correlate_loop(image, kernel):
    # מימוש באמצעות לולאות ו-slicing (patch) [cite: 162, 171]
    h_img, w_img = image.shape
    h_ker, w_ker = kernel.shape
    # הממדים של התוצאה ב-mode=valid הם (H-h+1, W-w+1) [cite: 154]
    res_h, res_w = h_img - h_ker + 1, w_img - w_ker + 1
    result = np.zeros((res_h, res_w), dtype=np.float32)
    
    for i in range(res_h):
        for j in range(res_w):
            patch = image[i:i+h_ker, j:j+w_ker]
            result[i, j] = np.sum(patch * kernel) # [cite: 170]
    return result

def cross_correlate_np(image, kernel):
    # מימוש באמצעות sliding_window_view [cite: 173]
    from numpy.lib.stride_tricks import sliding_window_view
    windows = sliding_window_view(image, kernel.shape)
    # הכפלה ב-kernel וסכימה על הצירים של החלון (צירים 2 ו-3) [cite: 176]
    result = np.sum(windows * kernel, axis=(2, 3))
    return result.astype(np.float32)

def cross_correlate_scipy(image, kernel):
    # מימוש באמצעות scipy [cite: 178]
    # signal.correlate2d משמש לביצוע cross-correlation דו-ממדי
    result = signal.correlate2d(image, kernel, mode='valid')
    return result.astype(np.float32)

def compare_cross_correlations():
    kernel = initialize_kernel()
    image = get_image()
    
    res_loop = cross_correlate_loop(image, kernel)
    res_np = cross_correlate_np(image, kernel)
    res_scipy = cross_correlate_scipy(image, kernel)
    
    # בדיקה שכל התוצאות זהות [cite: 180, 181]
    check1 = np.allclose(res_loop, res_np)
    check2 = np.allclose(res_np, res_scipy)
    
    if check1 and check2:
        print("All results match!")
        return True
    else:
        print("Results do not match!")
        return False

if __name__ == "__main__":
    compare_cross_correlations()