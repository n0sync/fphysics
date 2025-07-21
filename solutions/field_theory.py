import numpy as np
import cmath

class QuantumField:
    def __init__(self, field_type, dimensions, mass=0):
        self.field_type = field_type
        self.dimensions = dimensions
        self.mass = mass
        self.creation_operators = {}
        self.annihilation_operators = {}

    def add_mode(self, momentum, energy):
        self.creation_operators[momentum] = CreationOperator(momentum, energy)
        self.annihilation_operators[momentum] = AnnihilationOperator(momentum, energy)

    def field_operator(self, position, time):
        field_value = 0
        volume = np.prod(self.dimensions)
        
        for p, a_op in self.annihilation_operators.items():
            energy = a_op.energy
            phase = cmath.exp(1j * (np.dot(p, position) - energy * time))
            normalization = 1 / np.sqrt(2 * energy * volume)
            field_value += normalization * phase * a_op.state
            
        for p, a_dag_op in self.creation_operators.items():
            energy = a_dag_op.energy
            phase = cmath.exp(-1j * (np.dot(p, position) - energy * time))
            normalization = 1 / np.sqrt(2 * energy * volume)
            field_value += normalization * phase * a_dag_op.state
            
        return field_value

    def momentum_operator(self, position, time):
        momentum_density = 0
        for p, a_op in self.annihilation_operators.items():
            energy = a_op.energy
            phase_derivative = -1j * energy * cmath.exp(1j * (np.dot(p, position) - energy * time))
            momentum_density += phase_derivative * a_op.state
        return momentum_density

class CreationOperator:
    def __init__(self, momentum, energy):
        self.momentum = momentum
        self.energy = energy
        self.state = 1

    def commute_with_annihilation(self, other_momentum):
        if np.allclose(self.momentum, other_momentum):
            return 1
        return 0

    def act_on_vacuum(self):
        return FockState([self.momentum])

class AnnihilationOperator:
    def __init__(self, momentum, energy):
        self.momentum = momentum
        self.energy = energy
        self.state = 1

    def commute_with_creation(self, other_momentum):
        if np.allclose(self.momentum, other_momentum):
            return 1
        return 0

    def act_on_vacuum(self):
        return 0

class FockState:
    def __init__(self, occupation_numbers):
        self.occupation_numbers = occupation_numbers
        self.norm_squared = 1

    def particle_number(self):
        return len(self.occupation_numbers)

    def energy(self):
        total_energy = 0
        for momentum in self.occupation_numbers:
            energy = np.sqrt(np.dot(momentum, momentum) + self.mass**2)
            total_energy += energy
        return total_energy

    def normalize(self):
        n = self.particle_number()
        self.norm_squared = np.math.factorial(n)

class ScalarField(QuantumField):
    def __init__(self, dimensions, mass=0):
        super().__init__('scalar', dimensions, mass)

    def klein_gordon_equation(self, phi, position, time):
        laplacian = self._laplacian(phi, position)
        time_derivative_squared = self._second_time_derivative(phi, time)
        return time_derivative_squared - laplacian + self.mass**2 * phi

    def _laplacian(self, phi, position):
        laplacian = 0
        h = 1e-6
        for i, x in enumerate(position):
            pos_plus = position.copy()
            pos_minus = position.copy()
            pos_plus[i] += h
            pos_minus[i] -= h
            second_derivative = (phi(pos_plus) - 2*phi(position) + phi(pos_minus)) / h**2
            laplacian += second_derivative
        return laplacian

    def _second_time_derivative(self, phi, time):
        h = 1e-6
        return (phi(time + h) - 2*phi(time) + phi(time - h)) / h**2

class DiracField(QuantumField):
    def __init__(self, dimensions, mass=0):
        super().__init__('fermion', dimensions, mass)
        self.gamma_matrices = self._initialize_gamma_matrices()

    def _initialize_gamma_matrices(self):
        gamma0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
        gamma1 = np.array([[0, 0, 0, 1], [0, 0, 1, 0], [0, -1, 0, 0], [-1, 0, 0, 0]])
        gamma2 = np.array([[0, 0, 0, -1j], [0, 0, 1j, 0], [0, 1j, 0, 0], [-1j, 0, 0, 0]])
        gamma3 = np.array([[0, 0, 1, 0], [0, 0, 0, -1], [-1, 0, 0, 0], [0, 1, 0, 0]])
        return [gamma0, gamma1, gamma2, gamma3]

    def dirac_equation(self, psi, momentum):
        gamma_dot_p = sum(gamma * p for gamma, p in zip(self.gamma_matrices[1:], momentum))
        return (1j * self.gamma_matrices[0] @ gamma_dot_p + self.mass) @ psi

    def dirac_spinor(self, momentum, spin):
        energy = np.sqrt(np.dot(momentum, momentum) + self.mass**2)
        if spin == 1:
            u = np.array([1, 0, momentum[2]/(energy + self.mass), 
                         (momentum[0] + 1j*momentum[1])/(energy + self.mass)])
        else:
            u = np.array([0, 1, (momentum[0] - 1j*momentum[1])/(energy + self.mass), 
                         -momentum[2]/(energy + self.mass)])
        
        normalization = np.sqrt((energy + self.mass) / (2 * energy))
        return normalization * u

class FeynmanDiagram:
    def __init__(self):
        self.vertices = []
        self.propagators = []
        self.external_lines = []

    def add_vertex(self, position, vertex_type, coupling_constant=1):
        vertex = {
            'position': position,
            'type': vertex_type,
            'coupling': coupling_constant
        }
        self.vertices.append(vertex)

    def add_propagator(self, start_vertex, end_vertex, particle_type, momentum):
        propagator = {
            'start': start_vertex,
            'end': end_vertex,
            'type': particle_type,
            'momentum': momentum
        }
        self.propagators.append(propagator)

    def add_external_line(self, vertex, particle_type, momentum, incoming=True):
        external_line = {
            'vertex': vertex,
            'type': particle_type,
            'momentum': momentum,
            'incoming': incoming
        }
        self.external_lines.append(external_line)

    def calculate_amplitude(self):
        amplitude = 1
        
        for vertex in self.vertices:
            amplitude *= vertex['coupling']
            
        for propagator in self.propagators:
            if propagator['type'] == 'scalar':
                p_squared = np.dot(propagator['momentum'], propagator['momentum'])
                amplitude *= 1 / (p_squared - self.mass**2)
            elif propagator['type'] == 'fermion':
                amplitude *= self._fermion_propagator(propagator['momentum'])
                
        return amplitude

    def _fermion_propagator(self, momentum):
        gamma_dot_p = sum(gamma * p for gamma, p in zip(self.gamma_matrices[1:], momentum))
        numerator = self.gamma_matrices[0] * momentum[0] - gamma_dot_p + self.mass * np.eye(4)
        p_squared = np.dot(momentum, momentum)
        return numerator / (p_squared - self.mass**2)

class VacuumState:
    def __init__(self):
        self.energy = 0
        self.particle_number = 0

    def vacuum_expectation_value(self, operator):
        return operator.vacuum_matrix_element()

    def casimir_energy(self, plate_separation, dimensions=3):
        if dimensions == 1:
            return -np.pi**2 / (24 * plate_separation**2)
        elif dimensions == 3:
            return -np.pi**2 / (240 * plate_separation**4)
        else:
            return 0

class SecondQuantization:
    def __init__(self, single_particle_states):
        self.single_particle_states = single_particle_states
        self.fock_space_basis = []

    def create_fock_space(self, max_particles):
        for n in range(max_particles + 1):
            for occupation in self._generate_occupations(n):
                self.fock_space_basis.append(FockState(occupation))

    def _generate_occupations(self, n_particles):
        if n_particles == 0:
            return [[]]
        
        occupations = []
        for i in range(len(self.single_particle_states)):
            for sub_occupation in self._generate_occupations(n_particles - 1):
                new_occupation = [i] + sub_occupation
                occupations.append(new_occupation)
        return occupations

    def many_body_hamiltonian(self, single_particle_energies, interaction_matrix):
        hamiltonian = np.zeros((len(self.fock_space_basis), len(self.fock_space_basis)))
        
        for i, state_i in enumerate(self.fock_space_basis):
            for j, state_j in enumerate(self.fock_space_basis):
                if i == j:
                    for particle in state_i.occupation_numbers:
                        hamiltonian[i][j] += single_particle_energies[particle]
                        
        return hamiltonian
