import math
from constants import *

def hodgkin_huxley_sodium_m(voltage):
    alpha_m = 0.1 * (voltage + 40) / (1 - math.exp(-(voltage + 40) / 10))
    beta_m = 4 * math.exp(-(voltage + 65) / 18)
    return alpha_m, beta_m

def hodgkin_huxley_sodium_h(voltage):
    alpha_h = 0.07 * math.exp(-(voltage + 65) / 20)
    beta_h = 1 / (1 + math.exp(-(voltage + 35) / 10))
    return alpha_h, beta_h

def hodgkin_huxley_potassium_n(voltage):
    alpha_n = 0.01 * (voltage + 55) / (1 - math.exp(-(voltage + 55) / 10))
    beta_n = 0.125 * math.exp(-(voltage + 65) / 80)
    return alpha_n, beta_n

def cable_equation_steady_state(initial_voltage, distance, length_constant):
    return initial_voltage * math.exp(-distance / length_constant)

def length_constant(membrane_resistance, axial_resistance):
    return math.sqrt(membrane_resistance / axial_resistance)

def synaptic_potential_reversal(synaptic_current, synaptic_conductance, reversal_potential):
    return reversal_potential + synaptic_current / synaptic_conductance

def firing_rate_izhikevich(voltage, recovery, a, b):
    if voltage >= 30:
        return 1
    return 0

def calcium_concentration_dynamics(initial_ca, influx_rate, efflux_time_constant, time):
    return initial_ca + influx_rate * (1 - math.exp(-time / efflux_time_constant))

def network_synchrony_index(spike_times, num_neurons):
    cross_corr = 0
    for i in range(num_neurons):
        for j in range(i + 1, num_neurons):
            cross_corr += len(set(spike_times[i]) & set(spike_times[j]))
    return cross_corr / (num_neurons * (num_neurons - 1) / 2)

def neural_plasticity_stdp(delta_t, a_plus, tau_plus, a_minus, tau_minus):
    if delta_t > 0:
        return a_plus * math.exp(-delta_t / tau_plus)
    else:
        return -a_minus * math.exp(delta_t / tau_minus)

def information_entropy_spike_train(spike_probabilities):
    entropy = 0
    for p in spike_probabilities:
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

def brain_connectivity_matrix(correlation_matrix, threshold):
    return [[1 if abs(corr) > threshold else 0 for corr in row] for row in correlation_matrix]
