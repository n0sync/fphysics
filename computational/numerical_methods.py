import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve


def euler(f, y0, t_span, h):
    t_start, t_end = t_span
    t = np.arange(t_start, t_end + h, h)
    y = np.zeros((len(t), len(y0) if hasattr(y0, '__len__') else 1))
    y[0] = y0
    
    for i in range(len(t) - 1):
        y[i + 1] = y[i] + h * f(t[i], y[i])
    
    return t, y


def rk4(f, y0, t_span, h):
    t_start, t_end = t_span
    t = np.arange(t_start, t_end + h, h)
    y = np.zeros((len(t), len(y0) if hasattr(y0, '__len__') else 1))
    y[0] = y0
    
    for i in range(len(t) - 1):
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + h/2, y[i] + k1/2)
        k3 = h * f(t[i] + h/2, y[i] + k2/2)
        k4 = h * f(t[i] + h, y[i] + k3)
        y[i + 1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return t, y


def rk45_adaptive(f, y0, t_span, rtol=1e-6, atol=1e-9):
    sol = solve_ivp(f, t_span, y0, method='RK45', rtol=rtol, atol=atol, dense_output=True)
    return sol.t, sol.y.T


def newton_raphson(f, df, x0, tol=1e-10, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        x = x - fx / df(x)
    return x


def bisection(f, a, b, tol=1e-10, max_iter=100):
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


def secant(f, x0, x1, tol=1e-10, max_iter=100):
    for i in range(max_iter):
        fx0, fx1 = f(x0), f(x1)
        if abs(fx1) < tol:
            return x1
        x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        x0, x1 = x1, x_new
    return x1


def trapezoid(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])


def simpson(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h/3 * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]) + y[-1])


def gauss_quadrature(f, a, b, n=5):
    if n == 2:
        points = np.array([-1/np.sqrt(3), 1/np.sqrt(3)])
        weights = np.array([1, 1])
    elif n == 3:
        points = np.array([-np.sqrt(3/5), 0, np.sqrt(3/5)])
        weights = np.array([5/9, 8/9, 5/9])
    elif n == 4:
        points = np.array([-np.sqrt((3+2*np.sqrt(6/5))/7), -np.sqrt((3-2*np.sqrt(6/5))/7),
                          np.sqrt((3-2*np.sqrt(6/5))/7), np.sqrt((3+2*np.sqrt(6/5))/7)])
        weights = np.array([(18-np.sqrt(30))/36, (18+np.sqrt(30))/36,
                           (18+np.sqrt(30))/36, (18-np.sqrt(30))/36])
    else:
        points, weights = np.polynomial.legendre.leggauss(n)
    
    x_transformed = 0.5 * (b - a) * points + 0.5 * (b + a)
    return 0.5 * (b - a) * np.sum(weights * f(x_transformed))


def finite_difference(f, x, h=1e-5, order=1):
    if order == 1:
        return (f(x + h) - f(x - h)) / (2 * h)
    elif order == 2:
        return (f(x + h) - 2*f(x) + f(x - h)) / h**2
    else:
        raise ValueError("Only first and second order derivatives supported")


def gradient(f, x, h=1e-5):
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x_plus = x.copy()
        x_minus = x.copy()
        x_plus[i] += h
        x_minus[i] -= h
        grad[i] = (f(x_plus) - f(x_minus)) / (2 * h)
    return grad


def jacobian(f, x, h=1e-5):
    n = len(x)
    m = len(f(x))
    jac = np.zeros((m, n))
    
    for j in range(n):
        x_plus = x.copy()
        x_minus = x.copy()
        x_plus[j] += h
        x_minus[j] -= h
        jac[:, j] = (f(x_plus) - f(x_minus)) / (2 * h)
    
    return jac


def laplacian_2d(u, dx, dy):
    return (np.roll(u, 1, axis=0) + np.roll(u, -1, axis=0) - 2*u) / dx**2 + \
           (np.roll(u, 1, axis=1) + np.roll(u, -1, axis=1) - 2*u) / dy**2


def poisson_2d_jacobi(f, boundary, dx, dy, tol=1e-6, max_iter=10000):
    nx, ny = f.shape
    u = np.zeros_like(f)
    u[0, :] = boundary['bottom']
    u[-1, :] = boundary['top']
    u[:, 0] = boundary['left']
    u[:, -1] = boundary['right']
    
    for iteration in range(max_iter):
        u_new = u.copy()
        for i in range(1, nx-1):
            for j in range(1, ny-1):
                u_new[i, j] = 0.25 * (u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1] - dx*dy*f[i, j])
        
        if np.max(np.abs(u_new - u)) < tol:
            return u_new
        u = u_new
    
    return u


def fourier_transform(signal, dt):
    n = len(signal)
    frequencies = np.fft.fftfreq(n, dt)
    fft_signal = np.fft.fft(signal)
    return frequencies, fft_signal


def power_spectrum(signal, dt):
    frequencies, fft_signal = fourier_transform(signal, dt)
    power = np.abs(fft_signal)**2
    return frequencies[:len(frequencies)//2], power[:len(power)//2]


def cross_correlation(x, y):
    return np.correlate(x, y, mode='full')


def autocorrelation(x):
    return cross_correlation(x, x)


def convolution(x, y):
    return np.convolve(x, y, mode='full')


def savitzky_golay_filter(data, window_length, polyorder):
    from scipy.signal import savgol_filter
    return savgol_filter(data, window_length, polyorder)


def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')
