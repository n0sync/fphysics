import numpy as np


def molecular_orbital_linear_combination(atomic_orbitals, coefficients, position):
    wavefunction_value = 0
    for ao, coeff in zip(atomic_orbitals, coefficients):
        wavefunction_value += coeff * ao.evaluate(position)
    return wavefunction_value


def normalize_coefficients(coefficients):
    norm_squared = sum(c**2 for c in coefficients)
    return [c / np.sqrt(norm_squared) for c in coefficients]


def bond_order(molecular_orbitals, atom1_index, atom2_index):
    bonding_electrons = 0
    antibonding_electrons = 0
    
    for mo in molecular_orbitals:
        if mo['occupation'] > 0:
            if is_bonding_between(mo, atom1_index, atom2_index):
                bonding_electrons += mo['occupation']
            elif is_antibonding_between(mo, atom1_index, atom2_index):
                antibonding_electrons += mo['occupation']
    
    return (bonding_electrons - antibonding_electrons) / 2


def is_bonding_between(mo, atom1_index, atom2_index):
    coeff1 = mo['coefficients'][atom1_index]
    coeff2 = mo['coefficients'][atom2_index]
    return coeff1 * coeff2 > 0


def is_antibonding_between(mo, atom1_index, atom2_index):
    coeff1 = mo['coefficients'][atom1_index]
    coeff2 = mo['coefficients'][atom2_index]
    return coeff1 * coeff2 < 0


def total_molecular_energy(molecular_orbitals, atoms):
    electronic_energy = sum(mo['energy'] * mo['occupation'] for mo in molecular_orbitals)
    nuclear_repulsion = calculate_nuclear_repulsion(atoms)
    return electronic_energy + nuclear_repulsion


def calculate_nuclear_repulsion(atoms):
    repulsion_energy = 0
    for i, atom1 in enumerate(atoms):
        for j, atom2 in enumerate(atoms[i+1:], i+1):
            distance = distance_between_atoms(atom1, atom2)
            repulsion_energy += (atom1['atomic_number'] * atom2['atomic_number']) / distance
    return repulsion_energy


def distance_between_atoms(atom1, atom2):
    return np.sqrt(sum((a - b)**2 for a, b in zip(atom1['position'], atom2['position'])))


def construct_huckel_hamiltonian(n_atoms, bonds, alpha=-1.0, beta=-0.5):
    hamiltonian = np.zeros((n_atoms, n_atoms))
    
    for i in range(n_atoms):
        hamiltonian[i][i] = alpha
        
    for bond in bonds:
        i, j = bond
        hamiltonian[i][j] = beta
        hamiltonian[j][i] = beta
        
    return hamiltonian


def solve_huckel_secular_equation(n_atoms, bonds, alpha=-1.0, beta=-0.5):
    hamiltonian = construct_huckel_hamiltonian(n_atoms, bonds, alpha, beta)
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    
    molecular_orbitals = []
    for i, (energy, coeffs) in enumerate(zip(eigenvalues, eigenvectors.T)):
        mo = {
            'energy': energy,
            'coefficients': coeffs.tolist(),
            'occupation': 0
        }
        molecular_orbitals.append(mo)
        
    return molecular_orbitals


def vibrational_energy_level(frequency, v):
    h = 6.626e-34
    return h * frequency * (v + 0.5)


def harmonic_oscillator_wavefunction(x, v, frequency):
    alpha = 2 * np.pi * frequency / (6.626e-34)
    normalization = (alpha / np.pi)**(1/4) / np.sqrt(2**v * np.math.factorial(v))
    exponential = np.exp(-alpha * x**2 / 2)
    hermite = hermite_polynomial(np.sqrt(alpha) * x, v)
    return normalization * exponential * hermite


def hermite_polynomial(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    else:
        return 2 * x * hermite_polynomial(x, n-1) - 2 * (n-1) * hermite_polynomial(x, n-2)
