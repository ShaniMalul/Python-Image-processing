import numpy as np

def translation_matrix(a, b):
    return np.array([
        [1, 0, a],
        [0, 1, b],
        [0, 0, 1]
    ])


def rotation_matrix(theta):
    theta_rad = np.deg2rad(theta)
    
    return np.array([
        [np.cos(theta_rad), -np.sin(theta_rad), 0],
        [np.sin(theta_rad),  np.cos(theta_rad), 0],
        [0, 0, 1]
    ])

def scale_matrix(sx, sy=None):
    if sy is None:
        sy = sx
        
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

def rotate_around_point(theta, x0, y0):
    T1 = matrix_translation(-x0, -y0)
    R = matrix_rotation(theta)
    T2 = matrix_translation(x0, y0)
    
    return T2 @ R @ T1


M = rotate_around_point(30, 100, 200)

print(M)