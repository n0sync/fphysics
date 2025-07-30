import numpy as np

def membrane_potential(voltage, time, g_ion, e_ion):
    return g_ion * (voltage - e_ion)

def hodgkin_huxley_model(voltage, n, m, h):
    cm = 1.0
    g_na = 120.0
    g_k = 36.0
    g_l = 0.3
    e_na = 50.0
    e_k = -77.0
    e_l = -54.387
    
    ina = g_na * (m ** 3) * h * (voltage - e_na)
    ik = g_k * (n ** 4) * (voltage - e_k)
    il = g_l * (voltage - e_l)
    
    dvdt = - (ina + ik + il) / cm
    return dvdt

def fitzhugh_nagumo(voltage, recovery, I_ext):
    a = 0.7
    b = 0.8
    c = 3.0
    
    dvdt = c * (voltage - (voltage ** 3) / 3 + recovery + I_ext)
    dwdt = - (voltage - a + b * recovery) / c
    
    return dvdt, dwdt

def izhikevich_model(voltage, recovery, I_ext, a=0.02, b=0.2, c=-65, d=6):
    dvdt = 0.04 * voltage ** 2 + 5 * voltage + 140 - recovery + I_ext
    dwdt = a * (b * voltage - recovery)
    
    return dvdt, dwdt

def conductance_based_model(neuron_params, synapse_params, current_input):
    g_syn = synapse_params['g_syn']
    v_syn = synapse_params['v_syn']
    
    g_leak = neuron_params['g_leak']
    v_leak = neuron_params['v_leak']
    
    voltage = neuron_params['voltage']
    
    i_syn = g_syn * (voltage - v_syn)
    i_leak = g_leak * (voltage - v_leak)
    
    dvdt = - (i_syn + i_leak + current_input)
    return dvdt

def spike_timing_dependent_plasticity(pre_spike_time, post_spike_time, A_plus, A_minus, tau_plus, tau_minus):
    dt = post_spike_time - pre_spike_time
    if dt > 0:
        delta_w = A_plus * np.exp(-dt / tau_plus)
    else:
        delta_w = A_minus * np.exp(dt / tau_minus)
    return delta_w
def synaptic_release_probability(calcium_concentration, p_max, K_d):
    return p_max * (calcium_concentration ** 2) / (K_d ** 2 + calcium_concentration ** 2)

def neuron_population_dynamics(neuron_params, dt, input_current):
    membrane_potential = neuron_params['membrane_potential']
    recovery_variable = neuron_params['recovery_variable']
    
    voltage = membrane_potential + dt * input_current
    recovery = recovery_variable + dt * (neuron_params['a'] * (neuron_params['b'] * voltage - recovery_variable))
    
    return voltage, recovery

def dendritic_integration(branch_voltages, weights):
    return np.dot(branch_voltages, weights)

