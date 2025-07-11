from math import exp, cos

def clausius_clapeyron(L, T, delta_V):
    return L / (T * delta_V)

def van_der_waals(P, n, V, a, b, R, T):
    term1 = P + a * (n / V)**2
    term2 = (V / n) - b
    return term1 * term2 == R * T

def gibbs_free_energy(delta_H, T, delta_S):
    return delta_H - T * delta_S

def triple_point(P, T):
    return P, T

def latent_heat(m, L):
    return m * L

def heat_capacity_ratio(Cp, Cv):
    return Cp / Cv

def critical_pressure(a, b, R, Tc):
    return a / (27 * b**2)

def critical_temperature(a, b):
    return a / (27 * b * R)

def enthalpy(H1, H2, n):
    return (H2 - H1) / n

def entropy(S1, S2, n):
    return (S2 - S1) / n

def helmholtz_free_energy(U, T, S):
    return U - T * S

def maxwell_relations(F, G, U, H, S, T, P, V):
    return (F, G, U, H, S, T, P, V)

def phase_equilibrium(mu1, mu2):
    return mu1 == mu2

def chemical_potential(G, n):
    return G / n

def fugacity(P, phi):
    return P * phi

def activity(gamma, x):
    return gamma * x

def vapor_pressure(P0, delta_H, R, T1, T2):
    return P0 * exp(delta_H / R * (1/T1 - 1/T2))

def raoults_law(P, x, P0):
    return P == x * P0

def henrys_law(P, k, x):
    return P == k * x

def boiling_point_elevation(delta_T, Kb, m):
    return delta_T == Kb * m

def freezing_point_depression(delta_T, Kf, m):
    return delta_T == Kf * m

def osmotic_pressure(Pi, n, R, T, V):
    return Pi == (n * R * T) / V

def saturation_pressure(P0, A, T):
    return P0 * exp(A / T)

def critical_volume(b):
    return 3 * b

def reduced_pressure(P, Pc):
    return P / Pc

def reduced_temperature(T, Tc):
    return T / Tc

def reduced_volume(V, Vc):
    return V / Vc

def compressibility_factor(P, V, n, R, T):
    return (P * V) / (n * R * T)

def phase_rule(F, C, P):
    return F == C - P + 2

def heat_of_vaporization(H_vapor, H_liquid):
    return H_vapor - H_liquid

def heat_of_fusion(H_liquid, H_solid):
    return H_liquid - H_solid

def heat_of_sublimation(H_vapor, H_solid):
    return H_vapor - H_solid

def specific_heat_capacity(Q, m, delta_T):
    return Q / (m * delta_T)

def thermal_expansion(delta_V, V0, alpha, delta_T):
    return delta_V == V0 * alpha * delta_T

def bulk_modulus(P, V, delta_V):
    return -V * (P / delta_V)

def surface_tension(F, L):
    return F / L

def contact_angle(gamma_sv, gamma_sl, gamma_lv):
    return (gamma_sv - gamma_sl) / gamma_lv

def capillary_rise(h, gamma, theta, rho, g, r):
    return h == (2 * gamma * cos(theta)) / (rho * g * r)

def nucleation_rate(A, delta_G, k, T):
    return A * exp(-delta_G / (k * T))

def crystal_growth_rate(v, k, delta_mu, T):
    return v == k * exp(-delta_mu / (k * T))
