import numpy as np

class Atom:
    def __init__(self, atomic_number, mass_number):
        self.atomic_number = atomic_number
        self.mass_number = mass_number
        self.electrons = atomic_number
        self.protons = atomic_number
        self.neutrons = mass_number - atomic_number

    def bohr_radius(self, n=1):
        a0 = 5.29e-11
        return n**2 * a0

    def energy_level(self, n):
        rydberg_constant = 13.6
        return -rydberg_constant / n**2

    def transition_energy(self, n_initial, n_final):
        return self.energy_level(n_final) - self.energy_level(n_initial)

    def wavelength_from_transition(self, n_initial, n_final):
        h = 6.626e-34
        c = 3e8
        energy_joules = self.transition_energy(n_initial, n_final) * 1.602e-19
        return h * c / abs(energy_joules)

class HydrogenAtom(Atom):
    def __init__(self):
        super().__init__(1, 1)

    def radial_wavefunction(self, r, n, l):
        a0 = self.bohr_radius()
        rho = 2 * r / (n * a0)
        normalization = np.sqrt((2/(n*a0))**3 * np.math.factorial(n-l-1)/(2*n*np.math.factorial(n+l)))
        exponential = np.exp(-rho/2)
        laguerre = self._laguerre_polynomial(rho, n-l-1, 2*l+1)
        return normalization * (rho**l) * exponential * laguerre

    def _laguerre_polynomial(self, x, n, alpha):
        if n == 0:
            return 1
        elif n == 1:
            return 1 + alpha - x
        else:
            return ((2*n - 1 + alpha - x) * self._laguerre_polynomial(x, n-1, alpha) - 
                   (n - 1 + alpha) * self._laguerre_polynomial(x, n-2, alpha)) / n

class AtomicSpectrum:
    def __init__(self, atom):
        self.atom = atom
        self.observed_lines = []

    def add_spectral_line(self, wavelength, intensity, transition):
        self.observed_lines.append({
            'wavelength': wavelength,
            'intensity': intensity,
            'transition': transition
        })

    def rydberg_formula(self, n1, n2, z=1):
        rydberg_constant = 1.097e7
        return rydberg_constant * z**2 * (1/n1**2 - 1/n2**2)

    def fine_structure_constant(self):
        return 7.297e-3

    def spin_orbit_splitting(self, n, j, l):
        alpha = self.fine_structure_constant()
        z = self.atom.atomic_number
        return (alpha**2 * z**4 / n**3) * (1/j - 1/(l+0.5)) if l != 0 else 0
