import math
from ..constants import *

def sound_speed_air(temperature):
    return 331.3 * math.sqrt(1 + temperature / 273.15)

def sound_speed_medium(bulk_modulus, density):
    return math.sqrt(bulk_modulus / density)

def doppler_effect_moving_source(frequency, source_velocity, sound_speed):
    return frequency * sound_speed / (sound_speed - source_velocity)

def doppler_effect_moving_observer(frequency, observer_velocity, sound_speed):
    return frequency * (sound_speed + observer_velocity) / sound_speed

def doppler_effect_both_moving(frequency, source_velocity, observer_velocity, sound_speed):
    return frequency * (sound_speed + observer_velocity) / (sound_speed - source_velocity)

def beat_frequency(frequency1, frequency2):
    return abs(frequency1 - frequency2)

def sound_intensity(power, area):
    return power / area

def sound_intensity_level_db(intensity, reference_intensity=1e-12):
    return 10 * math.log10(intensity / reference_intensity)

def sound_pressure_level(pressure, reference_pressure=2e-5):
    return 20 * math.log10(pressure / reference_pressure)

def wavelength_from_frequency(frequency, speed):
    return speed / frequency

def resonance_frequency_open_pipe(length, harmonic, sound_speed):
    return harmonic * sound_speed / (2 * length)

def resonance_frequency_closed_pipe(length, harmonic, sound_speed):
    return (2 * harmonic - 1) * sound_speed / (4 * length)

def standing_wave_amplitude(amplitude1, amplitude2):
    return amplitude1 + amplitude2

def acoustic_impedance(density, sound_speed):
    return density * sound_speed

def reflection_coefficient(impedance1, impedance2):
    return (impedance2 - impedance1) / (impedance2 + impedance1)

def transmission_coefficient(impedance1, impedance2):
    return 2 * impedance2 / (impedance2 + impedance1)

def reverberation_time(room_volume, absorption_coefficient, surface_area):
    return 0.161 * room_volume / (absorption_coefficient * surface_area)

def sound_absorption_coefficient(incident_energy, absorbed_energy):
    return absorbed_energy / incident_energy

def acoustic_power(intensity, area):
    return intensity * area

def sound_frequency_from_wavelength(wavelength, speed):
    return speed / wavelength

def harmonic_frequency(fundamental_frequency, harmonic_number):
    return harmonic_number * fundamental_frequency

def sound_attenuation_distance(initial_intensity, distance):
    return initial_intensity / (4 * PI * distance**2)

def mach_number(velocity, sound_speed):
    return velocity / sound_speed

def shock_wave_angle(mach_number):
    return math.asin(1 / mach_number)

def acoustic_energy_density(pressure_amplitude, bulk_modulus):
    return pressure_amplitude**2 / (2 * bulk_modulus)

def sound_particle_velocity(pressure_amplitude, acoustic_impedance):
    return pressure_amplitude / acoustic_impedance

def acoustic_streaming_velocity(intensity, density, sound_speed):
    return intensity / (density * sound_speed**2)

def rayleigh_scattering_cross_section(frequency, particle_radius, sound_speed):
    wavelength = sound_speed / frequency
    return (2 * PI / 3) * (particle_radius / wavelength)**4

def sound_decay_exponential(initial_amplitude, decay_constant, time):
    return initial_amplitude * math.exp(-decay_constant * time)

def resonance_quality_factor(resonance_frequency, bandwidth):
    return resonance_frequency / bandwidth

def helmholtz_resonator_frequency(neck_area, neck_length, cavity_volume, sound_speed):
    return sound_speed / (2 * PI) * math.sqrt(neck_area / (neck_length * cavity_volume))

def acoustic_coupling_coefficient(mutual_impedance, self_impedance):
    return mutual_impedance / math.sqrt(self_impedance**2)

