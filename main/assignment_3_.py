# Given function f'(t) = t - y^2
def f(t, y):
    return t - y**2

# Euler Method
def euler_method(f, t0, y0, t_end, n):
    h = (t_end - t0) / n  # Step size
    t = t0
    y = y0
    for _ in range(n):
        y = y + h * f(t, y)
        t += h
    return y

# Runge-Kutta (RK4) Method
def runge_kutta_method(f, t0, y0, t_end, n):
    h = (t_end - t0) / n  # Step size
    t = t0
    y = y0
    for _ in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h
    return y

# Parameters
t0 = 0
y0 = 1
t_end = 2
n = 10

# Compute results
euler_result = euler_method(f, t0, y0, t_end, n)
rk_result = runge_kutta_method(f, t0, y0, t_end, n)

# Print results
print("Euler Method Result:", euler_result)
print("Runge-Kutta Method Result:", rk_result)

