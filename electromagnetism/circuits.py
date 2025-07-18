import numpy as np
from constants import *

# Ohm's Law
def ohms_law(V=None, I=None, R=None):
    if V is None:
        return I * R
    elif I is None:
        return V / R
    elif R is None:
        return V / I
    else:
        return V, I, R

# Power
def power_dissipation(V=None, I=None, R=None):
    if V is not None and I is not None:
        return V * I
    elif V is not None and R is not None:
        return V**2 / R
    elif I is not None and R is not None:
        return I**2 * R
    else:
        raise ValueError("Provide at least two parameters")

def power_factor(P, S):
    return P / S

def apparent_power(V, I):
    return V * I

def reactive_power(V, I, phi):
    return V * I * np.sin(phi)

def active_power(V, I, phi):
    return V * I * np.cos(phi)

# Resistance
def resistance_series(R_list):
    return np.sum(R_list)

def resistance_parallel(R_list):
    return 1 / np.sum(1 / np.array(R_list))

def resistance_temperature(R0, T, T0, alpha):
    return R0 * (1 + alpha * (T - T0))

def resistivity(R, A, L):
    return R * A / L

def conductance(R):
    return 1 / R

def conductivity(sigma, A, L):
    return sigma * A / L

# Capacitance
def capacitive_reactance(C, f):
    return 1 / (2 * PI * f * C)

def capacitive_time_constant(R, C):
    return R * C

def capacitor_charging(V0, t, R, C):
    return V0 * (1 - np.exp(-t / (R * C)))

def capacitor_discharging(V0, t, R, C):
    return V0 * np.exp(-t / (R * C))

def capacitor_energy(C, V):
    return 0.5 * C * V**2

# Inductance
def inductive_reactance(L, f):
    return 2 * PI * f * L

def inductive_time_constant(L, R):
    return L / R

def inductor_current_rise(I_max, t, L, R):
    return I_max * (1 - np.exp(-R * t / L))

def inductor_current_decay(I0, t, L, R):
    return I0 * np.exp(-R * t / L)

def inductor_energy(L, I):
    return 0.5 * L * I**2

# Impedance
def impedance_magnitude(R, X):
    return np.sqrt(R**2 + X**2)

def impedance_phase(R, X):
    return np.arctan(X / R)

def impedance_complex(R, X):
    return R + 1j * X

def impedance_rl(R, L, omega):
    return R + 1j * omega * L

def impedance_rc(R, C, omega):
    return R + 1j / (omega * C)

def impedance_rlc(R, L, C, omega):
    return R + 1j * (omega * L - 1 / (omega * C))

# AC Circuits
def rms_voltage(V_peak):
    return V_peak / np.sqrt(2)

def rms_current(I_peak):
    return I_peak / np.sqrt(2)

def peak_voltage(V_rms):
    return V_rms * np.sqrt(2)

def peak_current(I_rms):
    return I_rms * np.sqrt(2)

def average_power_ac(V_rms, I_rms, phi):
    return V_rms * I_rms * np.cos(phi)

# Resonance
def resonant_frequency(L, C):
    return 1 / (2 * PI * np.sqrt(L * C))

def quality_factor(omega0, R, L):
    return omega0 * L / R

def bandwidth(omega0, Q):
    return omega0 / Q

def damping_ratio(R, L, C):
    return R / (2 * np.sqrt(L / C))

# Filters
def low_pass_cutoff(R, C):
    return 1 / (2 * PI * R * C)

def high_pass_cutoff(R, C):
    return 1 / (2 * PI * R * C)

def band_pass_center(L, C):
    return 1 / (2 * PI * np.sqrt(L * C))

def filter_gain(omega, omega_c, n):
    return 1 / np.sqrt(1 + (omega / omega_c)**(2 * n))

# Transformers
def transformer_turns_ratio(V1, V2):
    return V1 / V2

def transformer_current_ratio(I1, I2):
    return I2 / I1

def transformer_impedance(Z2, n):
    return Z2 / n**2

def transformer_efficiency(P_out, P_in):
    return P_out / P_in

# Transmission Lines
def characteristic_impedance(L, C):
    return np.sqrt(L / C)

def propagation_constant(R, L, G, C, omega):
    return np.sqrt((R + 1j * omega * L) * (G + 1j * omega * C))

def reflection_coefficient(Z_L, Z_0):
    return (Z_L - Z_0) / (Z_L + Z_0)

def standing_wave_ratio(rho):
    return (1 + abs(rho)) / (1 - abs(rho))

# Three-Phase Circuits
def line_voltage(V_phase):
    return V_phase * np.sqrt(3)

def line_current_delta(I_phase):
    return I_phase * np.sqrt(3)

def power_three_phase(V_L, I_L, phi):
    return np.sqrt(3) * V_L * I_L * np.cos(phi)

# Kirchhoff's Laws
def kirchhoff_current_law(currents):
    return np.sum(currents)

def kirchhoff_voltage_law(voltages):
    return np.sum(voltages)

# Nodal Analysis
def nodal_conductance_matrix(G_matrix):
    return G_matrix

def nodal_current_vector(I_vector):
    return I_vector

def nodal_voltage_solution(G, I):
    return np.linalg.solve(G, I)

# Mesh Analysis
def mesh_resistance_matrix(R_matrix):
    return R_matrix

def mesh_voltage_vector(V_vector):
    return V_vector

def mesh_current_solution(R, V):
    return np.linalg.solve(R, V)

# Thévenin and Norton Equivalents
def thevenin_voltage(V_oc):
    return V_oc

def thevenin_resistance(R_th):
    return R_th

def norton_current(I_sc):
    return I_sc

def norton_resistance(R_n):
    return R_n

def thevenin_to_norton(V_th, R_th):
    return V_th / R_th, R_th

def norton_to_thevenin(I_n, R_n):
    return I_n * R_n, R_n

# Maximum Power Transfer
def maximum_power_transfer(V_th, R_th, R_L):
    return V_th**2 * R_L / (R_th + R_L)**2

def optimal_load_resistance(R_th):
    return R_th

# Superposition
def superposition_voltage(V_sources, responses):
    return np.sum(np.array(V_sources) * np.array(responses))

# Fourier Analysis
def fourier_coefficient_dc(f, T):
    return np.trapz(f, dx=T/len(f)) / T

def fourier_coefficient_an(f, t, n, T):
    return 2/T * np.trapz(f * np.cos(2*PI*n*t/T), dx=T/len(f))

def fourier_coefficient_bn(f, t, n, T):
    return 2/T * np.trapz(f * np.sin(2*PI*n*t/T), dx=T/len(f))

def total_harmonic_distortion(harmonics, fundamental):
    return np.sqrt(np.sum(harmonics[1:]**2)) / harmonics[0]

# Phasor Analysis
def phasor_to_time(magnitude, phase, omega, t):
    return magnitude * np.cos(omega * t + phase)

def time_to_phasor(signal, omega, t):
    return np.trapz(signal * np.exp(-1j * omega * t), t)

# Bode Plots
def magnitude_db(H):
    return 20 * np.log10(abs(H))

def phase_degrees(H):
    return np.angle(H) * 180 / PI

def gain_margin(H, omega):
    phase_180 = np.where(np.angle(H) <= -PI)[0]
    if len(phase_180) > 0:
        return -magnitude_db(H[phase_180[0]])
    return float('inf')

def phase_margin(H, omega):
    unity_gain = np.where(abs(H) <= 1)[0]
    if len(unity_gain) > 0:
        return 180 + phase_degrees(H[unity_gain[0]])
    return float('inf')

# Stability
def routh_hurwitz_stability(coeffs):
    n = len(coeffs)
    routh_table = np.zeros((n, n))
    routh_table[0, :] = coeffs[::2]
    routh_table[1, :] = coeffs[1::2]
    
    for i in range(2, n):
        for j in range(n - i):
            if routh_table[i-1, 0] == 0:
                return False
            routh_table[i, j] = (routh_table[i-1, 0] * routh_table[i-2, j+1] - 
                                routh_table[i-2, 0] * routh_table[i-1, j+1]) / routh_table[i-1, 0]
    
    return np.all(routh_table[:, 0] > 0)

# State Space Analysis
def state_space_solution(A, B, C, D, x0, u, t):
    from scipy.linalg import expm
    n = len(t)
    x = np.zeros((len(x0), n))
    y = np.zeros((C.shape[0], n))
    
    for i in range(n):
        if i == 0:
            dt = 0
        else:
            dt = t[i] - t[i-1]
        
        x[:, i] = expm(A * dt) @ x0 + np.trapz(expm(A * (t[i] - t[:i+1])) @ B @ u[:i+1], t[:i+1])
        y[:, i] = C @ x[:, i] + D @ u[i]
        x0 = x[:, i]
    
    return x, y
