import numpy as np
from scipy.integrate import odeint, solve_ivp
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt

def euler_method(f, y0, t_span, h):
    t = np.arange(t_span[0], t_span[1] + h, h)
    y = np.zeros((len(t), len(y0) if hasattr(y0, '__len__') else 1))
    y[0] = y0
    
    for i in range(1, len(t)):
        y[i] = y[i-1] + h * f(t[i-1], y[i-1])
    
    return t, y

def runge_kutta_4(f, y0, t_span, h):
    t = np.arange(t_span[0], t_span[1] + h, h)
    y = np.zeros((len(t), len(y0) if hasattr(y0, '__len__') else 1))
    y[0] = y0
    
    for i in range(1, len(t)):
        k1 = h * f(t[i-1], y[i-1])
        k2 = h * f(t[i-1] + h/2, y[i-1] + k1/2)
        k3 = h * f(t[i-1] + h/2, y[i-1] + k2/2)
        k4 = h * f(t[i-1] + h, y[i-1] + k3)
        y[i] = y[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return t, y

def heat_equation_1d(alpha, L, T, nx, nt, initial_condition, boundary_conditions):
    dx = L / (nx - 1)
    dt = T / nt
    r = alpha * dt / dx**2
    
    if r > 0.5:
        raise ValueError("Stability condition violated: r must be <= 0.5")
    
    x = np.linspace(0, L, nx)
    u = np.zeros((nt + 1, nx))
    u[0, :] = initial_condition(x)
    
    for n in range(nt):
        u[n+1, 1:-1] = u[n, 1:-1] + r * (u[n, 2:] - 2*u[n, 1:-1] + u[n, :-2])
        u[n+1, 0] = boundary_conditions[0](n * dt)
        u[n+1, -1] = boundary_conditions[1](n * dt)
    
    return x, u

def wave_equation_1d(c, L, T, nx, nt, initial_position, initial_velocity, boundary_conditions):
    dx = L / (nx - 1)
    dt = T / nt
    r = c * dt / dx
    
    if r > 1:
        raise ValueError("Stability condition violated: r must be <= 1")
    
    x = np.linspace(0, L, nx)
    u = np.zeros((nt + 1, nx))
    u[0, :] = initial_position(x)
    
    u[1, 1:-1] = u[0, 1:-1] + dt * initial_velocity(x[1:-1]) + \
                 0.5 * r**2 * (u[0, 2:] - 2*u[0, 1:-1] + u[0, :-2])
    u[1, 0] = boundary_conditions[0](dt)
    u[1, -1] = boundary_conditions[1](dt)
    
    for n in range(1, nt):
        u[n+1, 1:-1] = 2*u[n, 1:-1] - u[n-1, 1:-1] + r**2 * (u[n, 2:] - 2*u[n, 1:-1] + u[n, :-2])
        u[n+1, 0] = boundary_conditions[0]((n+1) * dt)
        u[n+1, -1] = boundary_conditions[1]((n+1) * dt)
    
    return x, u

def laplace_equation_2d(nx, ny, tolerance=1e-6, max_iterations=10000):
    dx = 1.0 / (nx - 1)
    dy = 1.0 / (ny - 1)
    
    u = np.zeros((nx, ny))
    u_new = np.zeros((nx, ny))
    
    for iteration in range(max_iterations):
        u_new[1:-1, 1:-1] = 0.25 * (u[2:, 1:-1] + u[:-2, 1:-1] + u[1:-1, 2:] + u[1:-1, :-2])
        
        if np.max(np.abs(u_new - u)) < tolerance:
            break
        
        u = u_new.copy()
    
    return u

def poisson_equation_1d(f, a, b, n, boundary_conditions):
    h = (b - a) / (n + 1)
    x = np.linspace(a, b, n + 2)
    
    A = diags([-1, 2, -1], [-1, 0, 1], shape=(n, n)) / h**2
    b_vector = f(x[1:-1])
    
    b_vector[0] += boundary_conditions[0] / h**2
    b_vector[-1] += boundary_conditions[1] / h**2
    
    u_interior = spsolve(A, b_vector)
    u = np.zeros(n + 2)
    u[0] = boundary_conditions[0]
    u[1:-1] = u_interior
    u[-1] = boundary_conditions[1]
    
    return x, u

def lotka_volterra(t, y, alpha, beta, gamma, delta):
    x, y_pop = y
    dxdt = alpha * x - beta * x * y_pop
    dydt = delta * x * y_pop - gamma * y_pop
    return [dxdt, dydt]

def van_der_pol_oscillator(t, y, mu):
    x, v = y
    dxdt = v
    dvdt = mu * (1 - x**2) * v - x
    return [dxdt, dvdt]

def pendulum_nonlinear(t, y, g, L):
    theta, omega = y
    dthetadt = omega
    domegadt = -(g/L) * np.sin(theta)
    return [dthetadt, domegadt]

def duffing_oscillator(t, y, alpha, beta, gamma, omega, F):
    x, v = y
    dxdt = v
    dvdt = -alpha * x - beta * x**3 - gamma * v + F * np.cos(omega * t)
    return [dxdt, dvdt]

def lorenz_system(t, y, sigma, rho, beta):
    x, y_coord, z = y
    dxdt = sigma * (y_coord - x)
    dydt = x * (rho - z) - y_coord
    dzdt = x * y_coord - beta * z
    return [dxdt, dydt, dzdt]

def rossler_system(t, y, a, b, c):
    x, y_coord, z = y
    dxdt = -y_coord - z
    dydt = x + a * y_coord
    dzdt = b + z * (x - c)
    return [dxdt, dydt, dzdt]

def schrodinger_1d_finite_difference(V, x, m=1, hbar=1):
    dx = x[1] - x[0]
    n = len(x)
    
    kinetic = -hbar**2 / (2 * m * dx**2) * diags([-1, 2, -1], [-1, 0, 1], shape=(n-2, n-2))
    potential = diags(V[1:-1], 0, shape=(n-2, n-2))
    
    H = kinetic + potential
    eigenvalues, eigenvectors = np.linalg.eigh(H.toarray())
    
    return eigenvalues, eigenvectors

def burgers_equation_1d(nu, L, T, nx, nt, initial_condition):
    dx = L / (nx - 1)
    dt = T / nt
    
    x = np.linspace(0, L, nx)
    u = np.zeros((nt + 1, nx))
    u[0, :] = initial_condition(x)
    
    for n in range(nt):
        u_new = u[n].copy()
        for i in range(1, nx - 1):
            u_new[i] = u[n, i] - u[n, i] * dt/dx * (u[n, i] - u[n, i-1]) + \
                      nu * dt/dx**2 * (u[n, i+1] - 2*u[n, i] + u[n, i-1])
        u[n+1] = u_new
    
    return x, u

def kdv_equation_soliton(c, x, t):
    return 0.5 * c * (1 / np.cosh(0.5 * np.sqrt(c) * (x - c * t)))**2

def sine_gordon_soliton(x, t, v=0.5):
    gamma = 1 / np.sqrt(1 - v**2)
    xi = gamma * (x - v * t)
    return 4 * np.arctan(np.exp(xi))
