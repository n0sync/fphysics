import scipy.special as sp

def bessel_function(nu, x):
    return sp.jv(nu, x)

def legendre_polynomial(n, x):
    return sp.legendre(n)(x)

def gamma_function(z):
    return sp.gamma(z)

def airy_function(x):
    return sp.airy(x)

def spherical_harmonic(l, m, theta, phi):
    return sp.sph_harm(m, l, phi, theta)
