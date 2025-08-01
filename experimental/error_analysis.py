import numpy as np

def uncertainty_addition_uncorrelated(*uncertainties):
    """Propagate uncertainties when adding uncorrelated variables."""
    return np.sqrt(sum(u**2 for u in uncertainties))

def uncertainty_product_relative(values, uncertainties):
    """Propagate uncertainties for a product of variables."""
    rel_uncertainties = [u / v for u, v in zip(uncertainties, values)]
    total_rel_uncertainty = np.sqrt(sum(rel_u**2 for rel_u in rel_uncertainties))
    return total_rel_uncertainty

def uncertainty_division_relative(value1, value2, uncertainty1, uncertainty2):
    """Calculate relative uncertainty for division."""
    rel_uncertainty = np.sqrt((uncertainty1 / value1)**2 + (uncertainty2 / value2)**2)
    return rel_uncertainty

def uncertainty_power(value, uncertainty, exponent):
    """Propagate uncertainty for power expressions."""
    return abs(exponent) * (uncertainty / value)

def uncertainty_exponential(value, uncertainty):
    """Propagate uncertainty through exponential function."""
    return np.exp(value) * uncertainty

def uncertainty_logarithm(value, uncertainty):
    """Propagate uncertainty through logarithm function."""
    return uncertainty / value

def uncertainty_sine(value, uncertainty):
    """Propagate uncertainty through sine function."""
    return np.abs(np.cos(value) * uncertainty)

def uncertainty_cosine(value, uncertainty):
    """Propagate uncertainty through cosine function."""
    return np.abs(np.sin(value) * uncertainty)

def uncertainty_tangent(value, uncertainty):
    """Propagate uncertainty through tangent function."""
    return np.abs((1 / (np.cos(value)**2)) * uncertainty)

def propagate_uncertainties(func, values, uncertainties):
    """General function to propagate uncertainties using a given function."""
    partial_derivatives = np.array([_numerical_partial(func, values, i) for i in range(len(values))])
    propagated = np.sqrt(np.sum((partial_derivatives * uncertainties)**2))
    return propagated

def _numerical_partial(func, values, index, delta=1e-5):
    perturbed = values.copy()
    perturbed[index] += delta
    return (func(*perturbed) - func(*values)) / delta
  
# Usage example
# def example_func(x, y, z):
#     return x * y**2 - np.sin(z)
# x, y, z = 2.0, 3.0, 0.1
# ux, uy, uz = 0.1, 0.1, 0.01
# uncertainty_result = propagate_uncertainties(example_func, [x, y, z], [ux, uy, uz])
