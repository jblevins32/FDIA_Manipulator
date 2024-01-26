def p_gamma(x, epsilon):
    if x > 1:
        p_gamma_soln = 1
    elif epsilon <= x <= 1:
        p_gamma_soln = x
    elif x < epsilon:
        p_gamma_soln = epsilon

    return p_gamma_soln