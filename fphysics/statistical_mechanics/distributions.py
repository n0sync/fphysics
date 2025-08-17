import math
from constants import *

def boltzmann_distribution(energy, temperature):
    return math.exp(-energy / (BOLTZMANN_CONSTANT * temperature))

def maxwell_boltzmann_velocity(velocity, mass, temperature):
    factor = math.sqrt(mass / (2 * PI * BOLTZMANN_CONSTANT * temperature))
    exponent = -mass * velocity**2 / (2 * BOLTZMANN_CONSTANT * temperature)
    return 4 * PI * velocity**2 * factor**3 * math.exp(exponent)

def maxwell_boltzmann_speed(speed, mass, temperature):
    factor = (mass / (2 * PI * BOLTZMANN_CONSTANT * temperature))**(3/2)
    exponent = -mass * speed**2 / (2 * BOLTZMANN_CONSTANT * temperature)
    return 4 * PI * speed**2 * factor * math.exp(exponent)

def maxwell_boltzmann_energy(energy, temperature):
    return 2 * math.sqrt(energy / (PI * BOLTZMANN_CONSTANT * temperature)) * math.exp(-energy / (BOLTZMANN_CONSTANT * temperature))

def fermi_dirac_distribution(energy, chemical_potential, temperature):
    exponent = (energy - chemical_potential) / (BOLTZMANN_CONSTANT * temperature)
    return 1 / (math.exp(exponent) + 1)

def bose_einstein_distribution(energy, chemical_potential, temperature):
    exponent = (energy - chemical_potential) / (BOLTZMANN_CONSTANT * temperature)
    return 1 / (math.exp(exponent) - 1)

def planck_distribution(frequency, temperature):
    hf_kt = PLANCK_CONSTANT * frequency / (BOLTZMANN_CONSTANT * temperature)
    return (2 * PLANCK_CONSTANT * frequency**3 / SPEED_OF_LIGHT**2) / (math.exp(hf_kt) - 1)

def rayleigh_jeans_distribution(frequency, temperature):
    return 2 * frequency**2 * BOLTZMANN_CONSTANT * temperature / SPEED_OF_LIGHT**2

def wien_distribution(frequency, temperature):
    hf_kt = PLANCK_CONSTANT * frequency / (BOLTZMANN_CONSTANT * temperature)
    return (2 * PLANCK_CONSTANT * frequency**3 / SPEED_OF_LIGHT**2) * math.exp(-hf_kt)

def gaussian_distribution(x, mean, variance):
    return (1 / math.sqrt(2 * PI * variance)) * math.exp(-(x - mean)**2 / (2 * variance))

def exponential_distribution(x, decay_rate):
    return decay_rate * math.exp(-decay_rate * x)

def poisson_distribution(k, mean):
    return (mean**k * math.exp(-mean)) / math.factorial(k)

def binomial_distribution(k, n, probability):
    return math.comb(n, k) * probability**k * (1 - probability)**(n - k)

def gamma_distribution(x, shape, scale):
    return (x**(shape - 1) * math.exp(-x / scale)) / (scale**shape * math.gamma(shape))

def beta_distribution(x, alpha, beta_param):
    return (x**(alpha - 1) * (1 - x)**(beta_param - 1)) / math.beta(alpha, beta_param)

def chi_squared_distribution(x, degrees_of_freedom):
    return (x**(degrees_of_freedom/2 - 1) * math.exp(-x/2)) / (2**(degrees_of_freedom/2) * math.gamma(degrees_of_freedom/2))

def student_t_distribution(t, degrees_of_freedom):
    numerator = math.gamma((degrees_of_freedom + 1) / 2)
    denominator = math.sqrt(degrees_of_freedom * PI) * math.gamma(degrees_of_freedom / 2)
    return numerator / denominator * (1 + t**2 / degrees_of_freedom)**(-(degrees_of_freedom + 1) / 2)

def lognormal_distribution(x, mu, sigma):
    return (1 / (x * sigma * math.sqrt(2 * PI))) * math.exp(-(math.log(x) - mu)**2 / (2 * sigma**2))

def weibull_distribution(x, shape, scale):
    return (shape / scale) * (x / scale)**(shape - 1) * math.exp(-(x / scale)**shape)

def pareto_distribution(x, scale, shape):
    return shape * scale**shape / x**(shape + 1)

def laplace_distribution(x, location, scale):
    return (1 / (2 * scale)) * math.exp(-abs(x - location) / scale)

def cauchy_distribution(x, location, scale):
    return 1 / (PI * scale * (1 + ((x - location) / scale)**2))

def levy_distribution(x, location, scale):
    return math.sqrt(scale / (2 * PI)) * math.exp(-scale / (2 * (x - location))) / (x - location)**(3/2)

def gumbel_distribution(x, location, scale):
    z = (x - location) / scale
    return (1 / scale) * math.exp(-(z + math.exp(-z)))

def extreme_value_distribution(x, location, scale, shape):
    if shape == 0:
        return gumbel_distribution(x, location, scale)
    else:
        t = 1 + shape * (x - location) / scale
        return (1 / scale) * t**(-1 - 1/shape) * math.exp(-t**(-1/shape))

def von_mises_distribution(theta, mu, kappa):
    return math.exp(kappa * math.cos(theta - mu)) / (2 * PI * math.iv(0, kappa))

def dirichlet_distribution(x_vector, alpha_vector):
    numerator = math.prod(x**a for x, a in zip(x_vector, alpha_vector))
    denominator = math.prod(math.gamma(a) for a in alpha_vector) / math.gamma(sum(alpha_vector))
    return numerator / denominator

def multinomial_distribution(counts, probabilities):
    n = sum(counts)
    coefficient = math.factorial(n) / math.prod(math.factorial(k) for k in counts)
    probability_term = math.prod(p**k for p, k in zip(probabilities, counts))
    return coefficient * probability_term
