import numpy as np

class MolecularOrbital:
    def __init__(self, atomic_orbitals, coefficients):
        self.atomic_orbitals = atomic_orbitals
        self.coefficients = coefficients
        self.energy = None
        self.occupation = 0

    def linear_combination(self, position):
        wavefunction_value = 0
        for ao, coeff in zip(self.atomic_orbitals, self.coefficients):
            wavefunction_value += coeff * ao.evaluate(position)
        return wavefunction_value

    def normalize(self):
        norm_squared = sum(c**2 for c in self.coefficients)
        self.coefficients = [c / np.sqrt(norm_squared) for c in self.coefficients]

class Molecule:
    def __init__(self, atoms, bonds):
        self.atoms = atoms
        self.bonds = bonds
        self.molecular_orbitals = []
        self.total_electrons = sum(atom.electrons for atom in atoms)

    def add_molecular_orbital(self, orbital):
        self.molecular_orbitals.append(orbital)

    def bond_order(self, atom1_index, atom2_index):
        bonding_electrons = 0
        antibonding_electrons = 0
        
        for mo in self.molecular_orbitals:
            if mo.occupation > 0:
                if self._is_bonding_between(mo, atom1_index, atom2_index):
                    bonding_electrons += mo.occupation
                elif self._is_antibonding_between(mo, atom1_index, atom2_index):
                    antibonding_electrons += mo.occupation
        
        return (bonding_electrons - antibonding_electrons) / 2

    def _is_bonding_between(self, mo, atom1_index, atom2_index):
        coeff1 = mo.coefficients[atom1_index]
        coeff2 = mo.coefficients[atom2_index]
        return coeff1 * coeff2 > 0

    def _is_antibonding_between(self, mo, atom1_index, atom2_index):
        coeff1 = mo.coefficients[atom1_index]
        coeff2 = mo.coefficients[atom2_index]
        return coeff1 * coeff2 < 0

    def total_energy(self):
        electronic_energy = sum(mo.energy * mo.occupation for mo in self.molecular_orbitals)
        nuclear_repulsion = self._calculate_nuclear_repulsion()
        return electronic_energy + nuclear_repulsion

    def _calculate_nuclear_repulsion(self):
        repulsion_energy = 0
        for i, atom1 in enumerate(self.atoms):
            for j, atom2 in enumerate(self.atoms[i+1:], i+1):
                distance = self._distance_between_atoms(atom1, atom2)
                repulsion_energy += (atom1.atomic_number * atom2.atomic_number) / distance
        return repulsion_energy

    def _distance_between_atoms(self, atom1, atom2):
        return np.sqrt(sum((a - b)**2 for a, b in zip(atom1.position, atom2.position)))

class HuckelMethod:
    def __init__(self, molecule):
        self.molecule = molecule
        self.alpha = -1.0
        self.beta = -0.5

    def construct_hamiltonian_matrix(self):
        n_atoms = len(self.molecule.atoms)
        hamiltonian = np.zeros((n_atoms, n_atoms))
        
        for i in range(n_atoms):
            hamiltonian[i][i] = self.alpha
            
        for bond in self.molecule.bonds:
            i, j = bond
            hamiltonian[i][j] = self.beta
            hamiltonian[j][i] = self.beta
            
        return hamiltonian

    def solve_secular_equation(self):
        hamiltonian = self.construct_hamiltonian_matrix()
        eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
        
        molecular_orbitals = []
        for i, (energy, coeffs) in enumerate(zip(eigenvalues, eigenvectors.T)):
            mo = MolecularOrbital([], coeffs.tolist())
            mo.energy = energy
            molecular_orbitals.append(mo)
            
        return molecular_orbitals

class VibrationalMode:
    def __init__(self, frequency, displacement_vectors):
        self.frequency = frequency
        self.displacement_vectors = displacement_vectors
        self.quantum_number = 0

    def energy_level(self, v):
        h = 6.626e-34
        return h * self.frequency * (v + 0.5)

    def harmonic_oscillator_wavefunction(self, x, v):
        alpha = 2 * np.pi * self.frequency / (6.626e-34)
        normalization = (alpha / np.pi)**(1/4) / np.sqrt(2**v * np.math.factorial(v))
        exponential = np.exp(-alpha * x**2 / 2)
        hermite = self._hermite_polynomial(np.sqrt(alpha) * x, v)
        return normalization * exponential * hermite

    def _hermite_polynomial(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return 2 * x
        else:
            return 2 * x * self._hermite_polynomial(x, n-1) - 2 * (n-1) * self._hermite_polynomial(x, n-2)
