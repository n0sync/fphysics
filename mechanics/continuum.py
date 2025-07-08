import math
from constants import *

def strain_tensor_2d(u_x_x, u_y_y, u_x_y, u_y_x):
    epsilon_xx = u_x_x
    epsilon_yy = u_y_y
    epsilon_xy = 0.5 * (u_x_y + u_y_x)
    return [[epsilon_xx, epsilon_xy], [epsilon_xy, epsilon_yy]]

def stress_tensor_plane_stress(epsilon_xx, epsilon_yy, epsilon_xy, elastic_modulus, poissons_ratio):
    factor = elastic_modulus / (1 - poissons_ratio**2)
    sigma_xx = factor * (epsilon_xx + poissons_ratio * epsilon_yy)
    sigma_yy = factor * (epsilon_yy + poissons_ratio * epsilon_xx)
    sigma_xy = factor * (1 - poissons_ratio) * epsilon_xy / 2
    return [[sigma_xx, sigma_xy], [sigma_xy, sigma_yy]]

def stress_tensor_plane_strain(epsilon_xx, epsilon_yy, epsilon_xy, elastic_modulus, poissons_ratio):
    factor = elastic_modulus / ((1 + poissons_ratio) * (1 - 2 * poissons_ratio))
    sigma_xx = factor * ((1 - poissons_ratio) * epsilon_xx + poissons_ratio * epsilon_yy)
    sigma_yy = factor * ((1 - poissons_ratio) * epsilon_yy + poissons_ratio * epsilon_xx)
    sigma_xy = factor * (1 - 2 * poissons_ratio) * epsilon_xy / 2
    return [[sigma_xx, sigma_xy], [sigma_xy, sigma_yy]]

def deformation_gradient_2d(dx_dX, dx_dY, dy_dX, dy_dY):
    return [[dx_dX, dx_dY], [dy_dX, dy_dY]]

def green_lagrange_strain_2d(F):
    F_T = [[F[0][0], F[1][0]], [F[0][1], F[1][1]]]
    C = [[F_T[0][0]*F[0][0] + F_T[0][1]*F[1][0], F_T[0][0]*F[0][1] + F_T[0][1]*F[1][1]],
         [F_T[1][0]*F[0][0] + F_T[1][1]*F[1][0], F_T[1][0]*F[0][1] + F_T[1][1]*F[1][1]]]
    E = [[0.5*(C[0][0] - 1), 0.5*C[0][1]], [0.5*C[1][0], 0.5*(C[1][1] - 1)]]
    return E

def infinitesimal_strain_tensor(displacement_gradients):
    u_x_x, u_x_y, u_y_x, u_y_y = displacement_gradients
    return [[u_x_x, 0.5*(u_x_y + u_y_x)], [0.5*(u_x_y + u_y_x), u_y_y]]

def volumetric_strain(epsilon_xx, epsilon_yy, epsilon_zz=0):
    return epsilon_xx + epsilon_yy + epsilon_zz

def deviatoric_strain_2d(epsilon_xx, epsilon_yy, epsilon_xy):
    mean_strain = (epsilon_xx + epsilon_yy) / 3
    return [[epsilon_xx - mean_strain, epsilon_xy], [epsilon_xy, epsilon_yy - mean_strain]]

def strain_invariants_2d(epsilon_xx, epsilon_yy, epsilon_xy):
    I1 = epsilon_xx + epsilon_yy
    I2 = epsilon_xx * epsilon_yy - epsilon_xy**2
    return I1, I2

def stress_invariants_2d(sigma_xx, sigma_yy, sigma_xy):
    I1 = sigma_xx + sigma_yy
    I2 = sigma_xx * sigma_yy - sigma_xy**2
    return I1, I2

def compatibility_equation_2d(epsilon_xx_yy, epsilon_yy_xx, epsilon_xy_xy):
    return epsilon_xx_yy + epsilon_yy_xx - 2 * epsilon_xy_xy

def equilibrium_equation_2d_x(sigma_xx_x, sigma_xy_y, body_force_x):
    return sigma_xx_x + sigma_xy_y + body_force_x

def equilibrium_equation_2d_y(sigma_xy_x, sigma_yy_y, body_force_y):
    return sigma_xy_x + sigma_yy_y + body_force_y

def constitutive_isotropic_2d(strain_tensor, elastic_modulus, poissons_ratio):
    E, nu = elastic_modulus, poissons_ratio
    lambda_param = (E * nu) / ((1 + nu) * (1 - 2 * nu))
    mu = E / (2 * (1 + nu))
    
    epsilon_xx, epsilon_yy = strain_tensor[0][0], strain_tensor[1][1]
    epsilon_xy = strain_tensor[0][1]
    
    trace_strain = epsilon_xx + epsilon_yy
    sigma_xx = lambda_param * trace_strain + 2 * mu * epsilon_xx
    sigma_yy = lambda_param * trace_strain + 2 * mu * epsilon_yy
    sigma_xy = 2 * mu * epsilon_xy
    
    return [[sigma_xx, sigma_xy], [sigma_xy, sigma_yy]]

def lame_parameters(elastic_modulus, poissons_ratio):
    E, nu = elastic_modulus, poissons_ratio
    lambda_param = (E * nu) / ((1 + nu) * (1 - 2 * nu))
    mu = E / (2 * (1 + nu))
    return lambda_param, mu

def bulk_modulus_from_lame(lambda_param, mu):
    return lambda_param + (2 * mu) / 3

def elastic_wave_speed_longitudinal(lambda_param, mu, density):
    return math.sqrt((lambda_param + 2 * mu) / density)

def elastic_wave_speed_transverse(mu, density):
    return math.sqrt(mu / density)

def rayleigh_wave_speed(mu, density, poissons_ratio):
    eta = (1 - poissons_ratio) / (1 - 2 * poissons_ratio)
    return math.sqrt(mu / density) * math.sqrt((2 - 2 * eta) / (2 - eta))

def strain_energy_density_elastic(stress_tensor, strain_tensor):
    sigma_xx, sigma_yy = stress_tensor[0][0], stress_tensor[1][1]
    sigma_xy = stress_tensor[0][1]
    epsilon_xx, epsilon_yy = strain_tensor[0][0], strain_tensor[1][1]
    epsilon_xy = strain_tensor[0][1]
    
    return 0.5 * (sigma_xx * epsilon_xx + sigma_yy * epsilon_yy + 2 * sigma_xy * epsilon_xy)

def airy_stress_function_compatibility(phi_xxxx, phi_yyyy, phi_xxyy):
    return phi_xxxx + 2 * phi_xxyy + phi_yyyy

def polar_stress_components(sigma_r, sigma_theta, tau_r_theta):
    return [[sigma_r, tau_r_theta], [tau_r_theta, sigma_theta]]

def polar_strain_components(epsilon_r, epsilon_theta, gamma_r_theta):
    return [[epsilon_r, gamma_r_theta/2], [gamma_r_theta/2, epsilon_theta]]

def transformation_matrix_2d(theta):
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    return [[cos_theta, -sin_theta], [sin_theta, cos_theta]]

def tensor_transformation_2d(tensor, transformation_matrix):
    T = transformation_matrix
    T_T = [[T[0][0], T[1][0]], [T[0][1], T[1][1]]]
    
    temp = [[T_T[0][0]*tensor[0][0] + T_T[0][1]*tensor[1][0], T_T[0][0]*tensor[0][1] + T_T[0][1]*tensor[1][1]],
            [T_T[1][0]*tensor[0][0] + T_T[1][1]*tensor[1][0], T_T[1][0]*tensor[0][1] + T_T[1][1]*tensor[1][1]]]
    
    result = [[temp[0][0]*T[0][0] + temp[0][1]*T[1][0], temp[0][0]*T[0][1] + temp[0][1]*T[1][1]],
              [temp[1][0]*T[0][0] + temp[1][1]*T[1][0], temp[1][0]*T[0][1] + temp[1][1]*T[1][1]]]
    
    return result

def volumetric_stress(epsilon_xx, epsilon_yy, epsilon_zz, lam, mu):
    return lam * (epsilon_xx + epsilon_yy + epsilon_zz) + 2 * mu * epsilon_xx

def deviatoric_stress(sigma_xx, sigma_yy, sigma_zz):
    mean_stress = (sigma_xx + sigma_yy + sigma_zz) / 3
    return [[sigma_xx - mean_stress, 0, 0], [0, sigma_yy - mean_stress, 0], [0, 0, sigma_zz - mean_stress]]

def elasticity_tensor_2d(elastic_modulus, poissons_ratio):
    E, nu = elastic_modulus, poissons_ratio
    factor = E / (1 - nu**2)
    return [[factor, factor * nu, 0], [factor * nu, factor, 0], [0, 0, factor * (1 - nu) / 2]]

def hydrostatic_press_strain(volumetric_strain, bulk_modulus):
    return bulk_modulus * volumetric_strain

def creep_constitutive_law(stress, A, n, m, time):
    return A * stress**n * time**m

def stress_deviator_invariant_j2(stress_tensor):
    s11, s22, s33 = stress_tensor[0][0], stress_tensor[1][1], stress_tensor[2][2]
    s12, s13, s23 = stress_tensor[0][1], stress_tensor[0][2], stress_tensor[1][2]
    mean_stress = (s11 + s22 + s33) / 3
    return ((s11 - mean_stress)**2 + (s22 - mean_stress)**2 + (s33 - mean_stress)**2) / 2 + s12**2 + s13**2 + s23**2

def octahedral_shear_stress(j2_invariant):
    return math.sqrt(2 * j2_invariant / 3)

def strain_rate_tensor(velocity_gradients):
    return [[velocity_gradients[0][0], 0.5 * (velocity_gradients[0][1] + velocity_gradients[1][0])],
            [0.5 * (velocity_gradients[0][1] + velocity_gradients[1][0]), velocity_gradients[1][1]]]

def vorticity_tensor(velocity_gradients):
    return [[0, 0.5 * (velocity_gradients[0][1] - velocity_gradients[1][0])],
            [0.5 * (velocity_gradients[1][0] - velocity_gradients[0][1]), 0]]
