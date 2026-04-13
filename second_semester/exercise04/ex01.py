import numpy as np

def warp_numpy_nearest(image, theta, sx, sy):
    H, W = image.shape[:2]

    # מרכז התמונה
    cx = W / 2
    cy = H / 2

    # המרת זווית לרדיאנים
    theta_rad = np.deg2rad(theta)

    # מטריצות טרנספורמציה
    S = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

    R = np.array([
        [np.cos(theta_rad), -np.sin(theta_rad), 0],
        [np.sin(theta_rad),  np.cos(theta_rad), 0],
        [0, 0, 1]
    ])

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

    # מטריצת הטרנספורמציה הכוללת
    M = T2 @ R @ S @ T1
    M_inv = np.linalg.inv(M)

    # יצירת רשת קואורדינטות
    j, i = np.meshgrid(np.arange(W), np.arange(H))
    x = j + 0.5
    y = i + 0.5

    ones = np.ones_like(x)
    target = np.stack([x, y, ones], axis=0).reshape(3, -1)

    # Backward Mapping
    source = M_inv @ target
    xs = source[0, :] - 0.5
    ys = source[1, :] - 0.5

    # Nearest Neighbor
    xs_round = np.round(xs).astype(int)
    ys_round = np.round(ys).astype(int)

    valid = (
        (xs_round >= 0) & (xs_round < W) &
        (ys_round >= 0) & (ys_round < H)
    )

    output = np.zeros_like(image)

    if image.ndim == 2:
        output_flat = output.reshape(-1)
        input_flat = image[ys_round[valid], xs_round[valid]]
        output_flat[valid] = input_flat
    else:
        output_flat = output.reshape(-1, image.shape[2])
        input_flat = image[ys_round[valid], xs_round[valid]]
        output_flat[valid] = input_flat

    return output