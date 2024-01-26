import numpy as np
import math
def p_omega(u,theta):
    # Calculate dplus and dminus values
    # joint bounds (rad and rad/s)
    theta_lower = np.array([[-180, -90, -230, -200, -115, -180]])*math.pi/180
    theta_upper = np.array([[180, 110, 50, 200, 115, 180]])*math.pi/180
    w_upper = np.array([[200, 200, 260, 360, 360, 450]])*math.pi/180
    w_lower = -w_upper
    gamma = 5  # epsilon <= gamma <= 1

    dplus = np.zeros((6, 1))
    dminus = np.zeros((6, 1))
    for i in range(len(u)):
        dplus[i] = np.minimum(w_upper[0, i], -gamma * (theta[0, i] - theta_upper[0, i]))
        dminus[i] = np.maximum(w_lower[0, i], -gamma * (theta[0, i] - theta_lower[0, i]))
    y = u
    y = dplus * (y >= dplus) + dminus * (y <= dminus) + ((y > dminus) & (y < dplus)) * y
    return np.transpose(y)