import dyers
import numpy as np
from projections import *
from robotics_functions import *
import math
import matplotlib.pyplot as plt


# Manipulator sends joint angles to control center
# FDIA is or is not detected
# Detection result, join angles, and desired end point position are sent to controller
# Control input sent to the manipulator (where attacker may FDIA the value)

# Jacobian: find coordinates of end effector wrt base frame
# take derivative of each
# take derivative of angle of end effector  as well
# form into 4xn matrix. n = number joints, where the matrix is multiplied by derivative of joint angles

if __name__ == '__main__':

    # region Setup
    # Gains
    k_1 = 50
    k_2 = 1

    # joint bounds (rad and rad/s)
    theta_lower = np.array([[-180, -90, -230, -200, -115, -180]])*math.pi/180
    theta_upper = np.array([[180, 110, 50, 200, 115, 180]])*math.pi/180
    w_upper = np.array([[200, 200, 260, 360, 360, 450]])*math.pi/180
    w_lower = -w_upper

    # Set up parameters
    t = 0 # start time
    tau = .001 # time step
    t_span = 10 # max time
    theta = np.transpose(theta_lower + 0.2*(theta_upper-theta_lower)) # Random initial starting position
    beta_hat = 1 # scale of an attack (1 = no attack)
    kappa = 5  # idk what this is
    e = 0  # Initialize error
    epsilon = .0001  # Gamma parameter
    gamma = 5  # epsilon <= gamma <= 1
    r = forward_kinematics(theta)
    r_hat = r  # ???
    r_vec = np.array([])
    r_hat_vec = np.array([])
    beta_hat_vec = np.array([])
    theta_vec = np.array([])
    t_vec = np.array([])

    #endregion

    while t <= t_span:
        r = forward_kinematics(theta)

        #Desired location and velocities
        rd = forward_kinematics(theta) + 0.1 * np.sin(t) * np.ones((3, 1))
        rd_next = 0.1 * np.cos(t) * np.ones((3, 1))

        J = jacobian(theta)
        alpha = 1000 # parameter to scale feedback strength (> 0)

        # Control Law
        ctrl = (alpha*np.transpose(J)@(rd - r))/beta_hat
        u_s = p_omega(ctrl, theta) # Projection operator

        # Injection attack
        u_r = .01 * u_s # Why isn't this beta the same as the previous?

        # Update law
        r_hat_next = r_hat + tau*beta_hat*J@u_s - k_1*(r_hat - r) # What is k1 and k2?

        if abs(beta_hat - p_gamma(beta_hat, epsilon)) > 0:
            s = abs(k_2*np.transpose(u_s)@np.transpose(J)@(r - r_hat))/abs(beta_hat - p_gamma(beta_hat, epsilon))
        else:
            s = 1

        beta_hat_next = beta_hat + tau*k_2*np.transpose(u_s)@np.transpose(J)@(r_hat - r) - s*(beta_hat - p_gamma(beta_hat, epsilon))

        theta_next = u_r # Attacked control command received by plant

        r_next = forward_kinematics(theta_next)

        # Checking error
        e = abs(r - rd)

        # Update stuff for next iteration
        r = r_next
        r_hat = r_hat_next
        beta_hat = beta_hat_next
        theta = theta_next

        r_vec = np.concatenate((r_vec, r[0]))
        r_hat_vec = np.concatenate((r_hat_vec, r_hat[0]))
        beta_hat_vec = np.concatenate((beta_hat_vec, beta_hat[0]))
        theta_vec = np.concatenate((theta_vec, theta[0]))
        t_vec = np.concatenate((t_vec, np.array([t])))

        t = t + tau
        # endregion

    # Plotting
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1)
    plt.plot(t_vec, r_vec, label='r')
    plt.title('r vs t')
    plt.xlabel('t')
    plt.ylabel('r')
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(t_vec, r_hat_vec, label='r_hat')
    plt.title('r_hat vs t')
    plt.xlabel('t')
    plt.ylabel('r_hat')
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.plot(t_vec, beta_hat_vec, label='beta_hat')
    plt.title('beta_hat vs t')
    plt.xlabel('t')
    plt.ylabel('beta_hat')
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.plot(t_vec, theta_vec, label='theta')
    plt.title('theta vs t')
    plt.xlabel('t')
    plt.ylabel('theta')
    plt.legend()

    plt.tight_layout()
    plt.show()