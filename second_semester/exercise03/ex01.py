import numpy as np

def warp(image, theta, sx, sy):
    H, W = image.shape[:2]
    
    # תמונת פלט
    output = np.zeros_like(image)

    # מרכז תמונה
    cx = W / 2
    cy = H / 2

    # המרת מעלות לרדיאנים
    theta_rad = np.deg2rad(theta)

    # מטריצת scale
    S = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

    # מטריצת סיבוב
    R = np.array([
        [np.cos(theta_rad), -np.sin(theta_rad), 0],
        [np.sin(theta_rad),  np.cos(theta_rad), 0],
        [0, 0, 1]
    ])

    # מטריצות הזזה
    T1 = np.array([
        [1, 0, -cx],
        [0, 1, -cy],
        [0, 0, 1]
    ])

    T2 = np.array([
        [1, 0, cx],
        [0, 1, cy],
        [0, 0, 1]
    ])

    # מטריצה כוללת
    M = T2 @ R @ S @ T1

    # בגלל backward mapping משתמשים בהופכי
    M_inv = np.linalg.inv(M)

    # מעבר על כל פיקסל בתמונת היעד
    for i in range(H):
        for j in range(W):

            # מרכז פיקסל
            x = j + 0.5
            y = i + 0.5

            target = np.array([x, y, 1])
            source = M_inv @ target

            xs = source[0] - 0.5
            ys = source[1] - 0.5

            # בדיקה אם בתחום
            if 0 <= xs < W-1 and 0 <= ys < H-1:

                # Bilinear interpolation
                x0 = int(np.floor(xs))
                y0 = int(np.floor(ys))

                dx = xs - x0
                dy = ys - y0

                if image.ndim == 2:  # grayscale
                    I00 = image[y0, x0]
                    I01 = image[y0, x0+1]
                    I10 = image[y0+1, x0]
                    I11 = image[y0+1, x0+1]

                    value = (
                        (1-dx)*(1-dy)*I00 +
                        dx*(1-dy)*I01 +
                        (1-dx)*dy*I10 +
                        dx*dy*I11
                    )

                    output[i, j] = value

                else:  # צבעוני
                    for c in range(image.shape[2]):
                        I00 = image[y0, x0, c]
                        I01 = image[y0, x0+1, c]
                        I10 = image[y0+1, x0, c]
                        I11 = image[y0+1, x0+1, c]

                        value = (
                            (1-dx)*(1-dy)*I00 +
                            dx*(1-dy)*I01 +
                            (1-dx)*dy*I10 +
                            dx*dy*I11
                        )

                        output[i, j, c] = value

    return output