from main import *
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
    return r
def jacobian(theta):
    theta1, theta2, theta3, theta4, theta5, theta6 = np.transpose(theta)

    J = np.array([
        [
            - (7 * np.sin(theta1)) / 100 - (9 * np.cos(theta2) * np.sin(theta1)) / 25 - (13 * np.sin(theta5) * (
                        np.cos(theta1) * np.sin(theta4) + np.cos(theta2) * np.cos(theta3) * np.cos(theta4) * np.sin(
                    theta1) - np.cos(theta4) * np.sin(theta1) * np.sin(theta2) * np.sin(theta3))) / 200 - (
                        19 * np.cos(theta2) * np.sin(theta1) * np.sin(theta3)) / 50 - (
                        19 * np.cos(theta3) * np.sin(theta1) * np.sin(theta2)) / 50 - (
                        13 * np.sin(theta2 + theta3) * np.cos(theta5) * np.sin(theta1)) / 200,
            - (np.cos(theta1) * (
                        72 * np.sin(theta2) - 76 * np.cos(theta2) * np.cos(theta3) + 76 * np.sin(theta2) * np.sin(
                    theta3) + 13 * np.cos(theta5) * np.sin(theta2) * np.sin(theta3) - 13 * np.cos(theta2) * np.cos(
                    theta3) * np.cos(theta5) + 13 * np.cos(theta2) * np.cos(theta4) * np.sin(theta3) * np.sin(
                    theta5) + 13 * np.cos(theta3) * np.cos(theta4) * np.sin(theta2) * np.sin(theta5))) / 200,
            (19 * np.cos(theta1) * np.cos(theta2) * np.cos(theta3)) / 50 - (
                        19 * np.cos(theta1) * np.sin(theta2) * np.sin(theta3)) / 50 - (
                        13 * np.cos(theta4) * np.sin(theta5) * (
                            np.cos(theta1) * np.cos(theta2) * np.sin(theta3) + np.cos(theta1) * np.cos(theta3) * np.sin(
                        theta2))) / 200 - (13 * np.cos(theta5) * (
                        np.cos(theta1) * np.sin(theta2) * np.sin(theta3) - np.cos(theta1) * np.cos(theta2) * np.cos(
                    theta3))) / 200,
            - (13 * np.sin(theta5) * (np.cos(theta4) * np.sin(theta1) - np.sin(theta4) * (
                        np.cos(theta1) * np.sin(theta2) * np.sin(theta3) - np.cos(theta1) * np.cos(theta2) * np.cos(
                    theta3)))) / 200,
            - (13 * np.cos(theta5) * (np.sin(theta1) * np.sin(theta4) + np.cos(theta4) * (
                        np.cos(theta1) * np.sin(theta2) * np.sin(theta3) - np.cos(theta1) * np.cos(theta2) * np.cos(
                    theta3)))) / 200 - (13 * np.sin(theta5) * (
                        np.cos(theta1) * np.cos(theta2) * np.sin(theta3) + np.cos(theta1) * np.cos(theta3) * np.sin(
                    theta2))) / 200,
            np.array([0])
        ],
        [
            (7 * np.cos(theta1)) / 100 + (9 * np.cos(theta1) * np.cos(theta2)) / 25 - (13 * np.sin(theta5) * (
                        np.sin(theta1) * np.sin(theta4) - np.cos(theta1) * np.cos(theta2) * np.cos(theta3) * np.cos(
                    theta4) + np.cos(theta1) * np.cos(theta4) * np.sin(theta2) * np.sin(theta3))) / 200 + (
                        13 * np.sin(theta2 + theta3) * np.cos(theta1) * np.cos(theta5)) / 200 + (
                        19 * np.cos(theta1) * np.cos(theta2) * np.sin(theta3)) / 50 + (
                        19 * np.cos(theta1) * np.cos(theta3) * np.sin(theta2)) / 50,
            - (np.sin(theta1) * (
                        72 * np.sin(theta2) - 76 * np.cos(theta2) * np.cos(theta3) + 76 * np.sin(theta2) * np.sin(
                    theta3) + 13 * np.cos(theta5) * np.sin(theta2) * np.sin(theta3) - 13 * np.cos(theta2) * np.cos(
                    theta3) * np.cos(theta5) + 13 * np.cos(theta2) * np.cos(theta4) * np.sin(theta3) * np.sin(
                    theta5) + 13 * np.cos(theta3) * np.cos(theta4) * np.sin(theta2) * np.sin(theta5))) / 200,
            (19 * np.cos(theta2) * np.cos(theta3) * np.sin(theta1)) / 50 - (
                        19 * np.sin(theta1) * np.sin(theta2) * np.sin(theta3)) / 50 - (
                        13 * np.cos(theta4) * np.sin(theta5) * (
                            np.cos(theta2) * np.sin(theta1) * np.sin(theta3) + np.cos(theta3) * np.sin(theta1) * np.sin(
                        theta2))) / 200 - (13 * np.cos(theta5) * (
                        np.sin(theta1) * np.sin(theta2) * np.sin(theta3) - np.cos(theta2) * np.cos(theta3) * np.sin(
                    theta1))) / 200,
            (13 * np.sin(theta5) * (np.cos(theta1) * np.cos(theta4) + np.sin(theta4) * (
                        np.sin(theta1) * np.sin(theta2) * np.sin(theta3) - np.cos(theta2) * np.cos(theta3) * np.sin(
                    theta1)))) / 200,
            (13 * np.cos(theta5) * (np.cos(theta1) * np.sin(theta4) - np.cos(theta4) * (
                        np.sin(theta1) * np.sin(theta2) * np.sin(theta3) - np.cos(theta2) * np.cos(theta3) * np.sin(
                    theta1)))) / 200 - (13 * np.sin(theta5) * (
                        np.cos(theta2) * np.sin(theta1) * np.sin(theta3) + np.cos(theta3) * np.sin(theta1) * np.sin(
                    theta2))) / 200,
            np.array([0])
        ],
        [
            np.array([0]),
            (13 * np.sin(theta4 - theta5) * np.cos(theta2 + theta3)) / 400 - (9 * np.cos(theta2)) / 25 - (
                        19 * np.sin(theta2 + theta3)) / 50 - (
                        13 * np.cos(theta2 + theta3) * np.sin(theta4 + theta5)) / 400 - (
                        13 * np.sin(theta2 + theta3) * np.cos(theta5)) / 200,
            - (19 * np.sin(theta2 + theta3)) / 50 - (13 * np.sin(theta2 + theta3) * np.cos(theta5)) / 200 - (
                        13 * np.cos(theta2 + theta3) * np.cos(theta4) * np.sin(theta5)) / 200,
            (13 * np.sin(theta2 + theta3) * np.sin(theta4) * np.sin(theta5)) / 200,
            - (13 * np.cos(theta2 + theta3) * np.sin(theta5)) / 200 - (
                        13 * np.sin(theta2 + theta3) * np.cos(theta4) * np.cos(theta5)) / 200,
            np.array([0])
        ]
    ])

    J = J.reshape(3, 6)

    return J