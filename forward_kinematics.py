import numpy as np
def forward_kinematics(theta):
    theta1, theta2, theta3, theta4, theta5, theta6 = np.transpose(theta)

    r = np.array([
        (7 * np.cos(theta1)) / 100 + (9 * np.cos(theta1) * np.cos(theta2)) / 25 - (13 * np.sin(theta5) * (
                    np.sin(theta1) * np.sin(theta4) + np.cos(theta4) * (
                        np.cos(theta1) * np.sin(theta2) * np.sin(theta3) - np.cos(theta1) * np.cos(theta2) * np.cos(
                    theta3)))) / 200 + (13 * np.cos(theta5) * (
                    np.cos(theta1) * np.cos(theta2) * np.sin(theta3) + np.cos(theta1) * np.cos(theta3) * np.sin(
                theta2))) / 200 + (19 * np.cos(theta1) * np.cos(theta2) * np.sin(theta3)) / 50 + (
                    19 * np.cos(theta1) * np.cos(theta3) * np.sin(theta2)) / 50,
        (7 * np.sin(theta1)) / 100 + (9 * np.cos(theta2) * np.sin(theta1)) / 25 + (13 * np.sin(theta5) * (
                    np.cos(theta1) * np.sin(theta4) - np.cos(theta4) * (
                        np.sin(theta1) * np.sin(theta2) * np.sin(theta3) - np.cos(theta2) * np.cos(theta3) * np.sin(
                    theta1)))) / 200 + (13 * np.cos(theta5) * (
                    np.cos(theta2) * np.sin(theta1) * np.sin(theta3) + np.cos(theta3) * np.sin(theta1) * np.sin(
                theta2))) / 200 + (19 * np.cos(theta2) * np.sin(theta1) * np.sin(theta3)) / 50 + (
                    19 * np.cos(theta3) * np.sin(theta1) * np.sin(theta2)) / 50,
        (19 * np.cos(theta2) * np.cos(theta3)) / 50 - (9 * np.sin(theta2)) / 25 - (
                    19 * np.sin(theta2) * np.sin(theta3)) / 50 + (
                    13 * np.cos(theta5) * (np.cos(theta2) * np.cos(theta3) - np.sin(theta2) * np.sin(theta3))) / 200 - (
                    13 * np.cos(theta4) * np.sin(theta5) * (
                        np.cos(theta2) * np.sin(theta3) + np.cos(theta3) * np.sin(theta2))) / 200 + 44 / 125
    ])
    return np.transpose(r)
