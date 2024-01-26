import dyers
import numpy as np
from jacobian import *
from p_gamma import *
from p_omega import *
from forward_kinematics import *
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Manipulator sends joint angles to control center
# FDIA is or is not detected
# Detection result, join angles, and desired end point position are sent to controller
# Control input sent to the manipulator (where attacker may FDIA the value)

# Jacobian: find coordinates of end effector wrt base frame
# take derivative of each
# take derivative of angle of end effector  as well
# form into 4xn matrix. n = number joints, where the matrix is multiplied by derivative of joint angles

def model(state, t):

    # Parsing state vector into usable data
    theta = state[0:6]
    r_hat = state[6:9]
    beta_hat = state[9]

    # Attack from manipulator to controller
    d_theta = (1 - 1 / beta) * theta0
    tilde_theta = (1 / beta) * theta + d_theta

    r = forward_kinematics(tilde_theta)

    #Desired position and velocities at each moment
    rd = forward_kinematics(theta0) + 0.1*math.sin(t) * np.ones((1, 3))
    rd_dot = 0.1*math.cos(t) * np.ones((1, 3))

    J = jacobian(tilde_theta)

    # Control Law
    test = rd-r
    ctrl = (alpha*np.transpose(J)@np.transpose(rd - r))
    u_s = p_omega(ctrl, tilde_theta)/beta_hat # Projection operator

    # Injection attack
    u_r = beta * u_s

    # Update laws
    r_hat_dot = np.transpose(beta_hat*J@np.transpose(u_s)) - k_1*(r_hat - r)

    if abs(beta_hat - p_gamma(beta_hat, epsilon)) > 0:
        s = abs(k_2*u_s@np.transpose(J)@np.transpose(r - r_hat))/abs(beta_hat - p_gamma(beta_hat, epsilon))
    else:
        s = 1

    test1 = np.transpose(r_hat - r)
    beta_hat_dot = -k_2 * u_s @ np.transpose(J) @ np.transpose(r_hat - r) - (s * (beta_hat - p_gamma(beta_hat, epsilon)))

    theta_dot = u_r  # sent to manipulator

    state_dot = np.concatenate((theta_dot, r_hat_dot, beta_hat_dot), axis=1)
    state_dot = state_dot.flatten()

    return state_dot

# region Setup
# Gains
k_1 = 500
k_2 = 500

# joint bounds (rad and rad/s)
theta_lower = np.array([[-180, -90, -230, -200, -115, -180]])*math.pi/180
theta_upper = np.array([[180, 110, 50, 200, 115, 180]])*math.pi/180
w_upper = np.array([[200, 200, 260, 360, 360, 450]])*math.pi/180
w_lower = -w_upper

# Set up parameters
t = np.linspace(0, 100, 1001)
epsilon = .0001  # Gamma parameter
gamma = 5  # epsilon <= gamma <= 1
alpha = 1000  # parameter to scale feedback strength (> 0)
theta = theta0 = theta_lower + 0.2*(theta_upper-theta_lower)  # Random initial starting position
r_hat = forward_kinematics(theta0)
beta_hat = np.array([1]).reshape(1, 1)
beta = .5  # Actual attack

# Forming state vector to input to differential equation
state = np.concatenate((theta0, forward_kinematics(theta0), beta_hat), axis=1)
state = state.flatten()

x = odeint(model, state, t)
#endregion

# Plotting
rd_vec = []
for i in t:
    rd = forward_kinematics(theta0) + 0.1 * math.sin(i) * np.ones((1, 3))
    rd_vec.append(rd)
rd_vec = np.squeeze(np.array(rd_vec))

r_vec = []
for row in x[:, 0:6]:
    r = forward_kinematics(row)
    r_vec.append(r)
r_vec = np.squeeze(np.array(r_vec))

plt.figure(figsize=(8, 6))
plt.plot(t, x[:, 9], label='beta_hat')
plt.axhline(y=beta, color='r', linestyle='--', label='beta')  # Add a horizontal line at y = beta
plt.xlabel('Time')
plt.legend()
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(t, x[:, 8], label='r_hat')
plt.plot(t, x[:, 7], label='r_hat')
plt.plot(t, x[:, 6], label='r_hat')
plt.plot(t, rd_vec[:, 2], label='rd', linestyle='--')
plt.plot(t, rd_vec[:, 1], label='rd', linestyle='--')
plt.plot(t, rd_vec[:, 0], label='rd', linestyle='--')
plt.plot(t, r_vec[:, 2], label='r', linestyle='--')
plt.plot(t, r_vec[:, 1], label='r', linestyle='--')
plt.plot(t, r_vec[:, 0], label='r', linestyle='--')
plt.xlabel('Time')
plt.ylabel('End Effector Position')
plt.legend()
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(t, x[:, 5])
plt.plot(t, x[:, 4])
plt.plot(t, x[:, 3])
plt.plot(t, x[:, 2])
plt.plot(t, x[:, 1])
plt.plot(t, x[:, 0])
plt.xlabel('Time')
plt.ylabel('Joint Positions')
plt.legend()
plt.show()