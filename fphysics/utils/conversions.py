import math
from ..constants import *

LENGTH_CONVERSIONS = {
    'm': 1.0,
    'km': 1000.0,
    'cm': 0.01,
    'mm': 0.001,
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mi': 1609.344,
    'nm': 1e-9,
    'μm': 1e-6,
    'pm': 1e-12,
    'ly': 9.461e15,
    'au': 1.496e11,
    'bohr': 5.29177210903e-11,
    'planck': 1.616255e-35,
    'Å': 1e-10
}

MASS_CONVERSIONS = {
    'kg': 1.0,
    'g': 0.001,
    'mg': 1e-6,
    'lb': 0.453592,
    'oz': 0.0283495,
    'ton': 1000.0,
    'slug': 14.5939,
    'u': 1.66054e-27,
    'MeV/c²': ELECTRON_VOLT * 1e6 / SPEED_OF_LIGHT**2,
    'electron_mass': 9.1093837015e-31,
    'proton_mass': 1.67262192369e-27
}

TIME_CONVERSIONS = {
    's': 1.0,
    'ms': 0.001,
    'μs': 1e-6,
    'ns': 1e-9,
    'min': 60.0,
    'h': 3600.0,
    'day': 86400.0,
    'week': 604800.0,
    'year': 31557600.0
}

TEMPERATURE_CONVERSIONS = {
    'K': {'K': lambda x: x, 'C': lambda x: x - 273.15, 'F': lambda x: (x - 273.15) * 9/5 + 32, 'R': lambda x: x * 9/5},
    'C': {'K': lambda x: x + 273.15, 'C': lambda x: x, 'F': lambda x: x * 9/5 + 32, 'R': lambda x: (x + 273.15) * 9/5},
    'F': {'K': lambda x: (x - 32) * 5/9 + 273.15, 'C': lambda x: (x - 32) * 5/9, 'F': lambda x: x, 'R': lambda x: x + 459.67},
    'R': {'K': lambda x: x * 5/9, 'C': lambda x: x * 5/9 - 273.15, 'F': lambda x: x - 459.67, 'R': lambda x: x}
}

ENERGY_CONVERSIONS = {
    'J': 1.0,
    'kJ': 1000.0,
    'MJ': 1e6,
    'cal': 4.184,
    'kcal': 4184.0,
    'BTU': 1055.06,
    'eV': 1.602e-19,
    'keV': 1.602e-16,
    'MeV': 1.602e-13,
    'kWh': 3.6e6,
    'erg': 1e-7,
    'ft_lb': 1.35582,
    'Hartree': 4.3597447222071e-18,
    'Rydberg': 2.17987236110355e-18
}

POWER_CONVERSIONS = {
    'W': 1.0,
    'kW': 1000.0,
    'MW': 1e6,
    'hp': 745.7,
    'BTU/h': 0.293071,
    'cal/s': 4.184,
    'erg/s': 1e-7
}

PRESSURE_CONVERSIONS = {
    'Pa': 1.0,
    'kPa': 1000.0,
    'MPa': 1e6,
    'GPa': 1e9,
    'bar': 1e5,
    'atm': 101325.0,
    'psi': 6894.76,
    'mmHg': 133.322,
    'torr': 133.322,
    'inHg': 3386.39
}

ANGLE_CONVERSIONS = {
    'rad': 1.0,
    'deg': math.pi / 180.0,
    'grad': math.pi / 200.0,
    'rev': 2 * math.pi,
    'mrad': 0.001,
    'arcsec': math.pi / 648000.0,
    'arcmin': math.pi / 10800.0
}

def length_conversion(value, from_unit, to_unit):
    if from_unit not in LENGTH_CONVERSIONS or to_unit not in LENGTH_CONVERSIONS:
        raise ValueError(f"Unsupported length unit: {from_unit} or {to_unit}")
    meters = value * LENGTH_CONVERSIONS[from_unit]
    return meters / LENGTH_CONVERSIONS[to_unit]

def mass_conversion(value, from_unit, to_unit):
    if from_unit not in MASS_CONVERSIONS or to_unit not in MASS_CONVERSIONS:
        raise ValueError(f"Unsupported mass unit: {from_unit} or {to_unit}")
    kg = value * MASS_CONVERSIONS[from_unit]
    return kg / MASS_CONVERSIONS[to_unit]

def time_conversion(value, from_unit, to_unit):
    if from_unit not in TIME_CONVERSIONS or to_unit not in TIME_CONVERSIONS:
        raise ValueError(f"Unsupported time unit: {from_unit} or {to_unit}")
    seconds = value * TIME_CONVERSIONS[from_unit]
    return seconds / TIME_CONVERSIONS[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit not in TEMPERATURE_CONVERSIONS or to_unit not in TEMPERATURE_CONVERSIONS:
        raise ValueError(f"Unsupported temperature unit: {from_unit} or {to_unit}")
    
    # Convert to Kelvin first to check for absolute zero
    if from_unit == 'K' and value < 0:
        raise ValueError("Temperature cannot be below absolute zero")
    elif from_unit == 'C' and value < -273.15:
        raise ValueError("Temperature cannot be below absolute zero")
    elif from_unit == 'F' and value < -459.67:
        raise ValueError("Temperature cannot be below absolute zero")
    elif from_unit == 'R' and value < 0:
        raise ValueError("Temperature cannot be below absolute zero")
    
    return TEMPERATURE_CONVERSIONS[from_unit][to_unit](value)

def energy_conversion(value, from_unit, to_unit):
    if from_unit not in ENERGY_CONVERSIONS or to_unit not in ENERGY_CONVERSIONS:
        raise ValueError(f"Unsupported energy unit: {from_unit} or {to_unit}")
    joules = value * ENERGY_CONVERSIONS[from_unit]
    return joules / ENERGY_CONVERSIONS[to_unit]

def power_conversion(value, from_unit, to_unit):
    if from_unit not in POWER_CONVERSIONS or to_unit not in POWER_CONVERSIONS:
        raise ValueError(f"Unsupported power unit: {from_unit} or {to_unit}")
    watts = value * POWER_CONVERSIONS[from_unit]
    return watts / POWER_CONVERSIONS[to_unit]

def pressure_conversion(value, from_unit, to_unit):
    if from_unit not in PRESSURE_CONVERSIONS or to_unit not in PRESSURE_CONVERSIONS:
        raise ValueError(f"Unsupported pressure unit: {from_unit} or {to_unit}")
    pascals = value * PRESSURE_CONVERSIONS[from_unit]
    return pascals / PRESSURE_CONVERSIONS[to_unit]

def angle_conversion(value, from_unit, to_unit):
    if from_unit not in ANGLE_CONVERSIONS or to_unit not in ANGLE_CONVERSIONS:
        raise ValueError(f"Unsupported angle unit: {from_unit} or {to_unit}")
    radians = value * ANGLE_CONVERSIONS[from_unit]
    return radians / ANGLE_CONVERSIONS[to_unit]

def voltage_conversion(value, from_unit, to_unit):
    conversions = {
        'V': 1.0,
        'mV': 1e-3,
        'kV': 1e3,
        'MV': 1e6
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported voltage unit: {from_unit} or {to_unit}")
    volts = value * conversions[from_unit]
    return volts / conversions[to_unit]

def current_conversion(value, from_unit, to_unit):
    conversions = {
        'A': 1.0,
        'mA': 1e-3,
        'μA': 1e-6,
        'kA': 1e3
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported current unit: {from_unit} or {to_unit}")
    amperes = value * conversions[from_unit]
    return amperes / conversions[to_unit]

def frequency_conversion(value, from_unit, to_unit):
    conversions = {
        'Hz': 1.0,
        'kHz': 1000.0,
        'MHz': 1e6,
        'GHz': 1e9,
        'THz': 1e12,
        'rpm': 1/60.0,
        'rps': 1.0
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported frequency unit: {from_unit} or {to_unit}")
    hz = value * conversions[from_unit]
    return hz / conversions[to_unit]

def force_conversion(value, from_unit, to_unit):
    conversions = {
        'N': 1.0,
        'kN': 1000.0,
        'MN': 1e6,
        'dyne': 1e-5,
        'lbf': 4.44822,
        'kgf': 9.80665,
        'pdl': 0.138255
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported force unit: {from_unit} or {to_unit}")
    newtons = value * conversions[from_unit]
    return newtons / conversions[to_unit]

def velocity_conversion(value, from_unit, to_unit):
    conversions = {
        'm/s': 1.0,
        'km/h': 1/3.6,
        'mph': 0.44704,
        'ft/s': 0.3048,
        'knot': 0.514444,
        'c': 299792458.0
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported velocity unit: {from_unit} or {to_unit}")
    mps = value * conversions[from_unit]
    return mps / conversions[to_unit]

def acceleration_conversion(value, from_unit, to_unit):
    conversions = {
        'm/s²': 1.0,
        'km/h²': 1/12960.0,
        'ft/s²': 0.3048,
        'g': 9.80665,
        'gal': 0.01
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported acceleration unit: {from_unit} or {to_unit}")
    mps2 = value * conversions[from_unit]
    return mps2 / conversions[to_unit]

def volume_conversion(value, from_unit, to_unit):
    conversions = {
        'm³': 1.0,
        'L': 0.001,
        'mL': 1e-6,
        'cm³': 1e-6,
        'ft³': 0.0283168,
        'in³': 1.63871e-5,
        'gal': 0.00378541,
        'qt': 0.000946353,
        'pt': 0.000473176
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported volume unit: {from_unit} or {to_unit}")
    m3 = value * conversions[from_unit]
    return m3 / conversions[to_unit]

def area_conversion(value, from_unit, to_unit):
    conversions = {
        'm²': 1.0,
        'cm²': 1e-4,
        'mm²': 1e-6,
        'km²': 1e6,
        'ft²': 0.092903,
        'in²': 0.00064516,
        'acre': 4046.86,
        'hectare': 10000.0
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported area unit: {from_unit} or {to_unit}")
    m2 = value * conversions[from_unit]
    return m2 / conversions[to_unit]

def density_conversion(value, from_unit, to_unit):
    conversions = {
        'kg/m³': 1.0,
        'g/cm³': 1000.0,
        'g/mL': 1000.0,
        'lb/ft³': 16.0185,
        'lb/in³': 27679.9,
        'kg/L': 1000.0
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported density unit: {from_unit} or {to_unit}")
    kgm3 = value * conversions[from_unit]
    return kgm3 / conversions[to_unit]


def charge_conversion(value, from_unit, to_unit):
    conversions = {
        'C': 1.0,
        'mC': 1e-3,
        'μC': 1e-6,
        'nC': 1e-9,
        'e': 1.602176634e-19
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported charge unit: {from_unit} or {to_unit}")
    coulombs = value * conversions[from_unit]
    return coulombs / conversions[to_unit]

def magnetic_field_conversion(value, from_unit, to_unit):
    conversions = {
        'T': 1.0,
        'G': 1e-4
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported magnetic field unit: {from_unit} or {to_unit}")
    tesla = value * conversions[from_unit]
    return tesla / conversions[to_unit]

def capacitance_conversion(value, from_unit, to_unit):
    conversions = {
        'F': 1.0,
        'mF': 1e-3,
        'μF': 1e-6,
        'nF': 1e-9,
        'pF': 1e-12
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported capacitance unit: {from_unit} or {to_unit}")
    farads = value * conversions[from_unit]
    return farads / conversions[to_unit]

def inductance_conversion(value, from_unit, to_unit):
    conversions = {
        'H': 1.0,
        'mH': 1e-3,
        'μH': 1e-6,
        'nH': 1e-9
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported inductance unit: {from_unit} or {to_unit}")
    henries = value * conversions[from_unit]
    return henries / conversions[to_unit]

def resistance_conversion(value, from_unit, to_unit):
    conversions = {
        'Ω': 1.0,
        'mΩ': 1e-3,
        'kΩ': 1e3,
        'MΩ': 1e6
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported resistance unit: {from_unit} or {to_unit}")
    ohms = value * conversions[from_unit]
    return ohms / conversions[to_unit]


