def nearest_neighbor(alpha, beta, I00, I01, I10, I11):
    if beta < 0.5:  # חצי עליון
        if alpha < 0.5:
            return I00
        else:
            return I01
    else:  # חצי תחתון
        if alpha < 0.5:
            return I10
        else:
            return I11
        

def bilinear_interpolation(alpha, beta, I00, I01, I10, I11):
    return (
        (1 - alpha) * (1 - beta) * I00 +
        alpha * (1 - beta) * I01 +
        (1 - alpha) * beta * I10 +
        alpha * beta * I11
    )