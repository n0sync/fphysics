import numpy as np
from scipy.stats import norm, uniform
import random


def monte_carlo_integration(f, bounds, n_samples=10000):
    dimensions = len(bounds)
    samples = np.random.uniform(
        low=[b[0] for b in bounds],
        high=[b[1] for b in bounds],
        size=(n_samples, dimensions)
    )
    
    function_values = np.array([f(sample) for sample in samples])
    volume = np.prod([b[1] - b[0] for b in bounds])
    
    return volume * np.mean(function_values), volume * np.std(function_values) / np.sqrt(n_samples)


def importance_sampling(f, proposal_dist, target_dist, n_samples=10000):
    samples = proposal_dist.rvs(n_samples)
    weights = target_dist.pdf(samples) / proposal_dist.pdf(samples)
    weighted_values = f(samples) * weights
    
    estimate = np.mean(weighted_values)
    variance = np.var(weighted_values) / n_samples
    
    return estimate, np.sqrt(variance)


def metropolis(log_prob, initial_state, step_size, n_samples=10000, burn_in=1000):
    samples = []
    current_state = initial_state.copy()
    current_log_prob = log_prob(current_state)
    n_accepted = 0
    
    for i in range(n_samples + burn_in):
        proposal = current_state + np.random.normal(0, step_size, size=current_state.shape)
        proposal_log_prob = log_prob(proposal)
        
        log_alpha = proposal_log_prob - current_log_prob
        if np.log(np.random.rand()) < log_alpha:
            current_state = proposal
            current_log_prob = proposal_log_prob
            n_accepted += 1
        
        if i >= burn_in:
            samples.append(current_state.copy())
    
    acceptance_rate = n_accepted / (n_samples + burn_in)
    return np.array(samples), acceptance_rate


def metropolis_hastings(log_prob, proposal_sampler, proposal_log_prob, initial_state, 
                       n_samples=10000, burn_in=1000):
    samples = []
    current_state = initial_state.copy()
    current_log_prob = log_prob(current_state)
    n_accepted = 0
    
    for i in range(n_samples + burn_in):
        proposal = proposal_sampler(current_state)
        proposal_log_prob_val = log_prob(proposal)
        
        log_alpha = (proposal_log_prob_val - current_log_prob + 
                    proposal_log_prob(current_state, proposal) - 
                    proposal_log_prob(proposal, current_state))
        
        if np.log(np.random.rand()) < log_alpha:
            current_state = proposal
            current_log_prob = proposal_log_prob_val
            n_accepted += 1
        
        if i >= burn_in:
            samples.append(current_state.copy())
    
    acceptance_rate = n_accepted / (n_samples + burn_in)
    return np.array(samples), acceptance_rate


def gibbs_sampler(conditional_samplers, initial_state, n_samples=10000, burn_in=1000):
    samples = []
    current_state = initial_state.copy()
    
    for i in range(n_samples + burn_in):
        for j, sampler in enumerate(conditional_samplers):
            current_state[j] = sampler(current_state)
        
        if i >= burn_in:
            samples.append(current_state.copy())
    
    return np.array(samples)


def hamiltonian_monte_carlo(log_prob, grad_log_prob, initial_state, step_size=0.01, 
                           n_steps=10, n_samples=1000, burn_in=100):
    samples = []
    current_q = initial_state.copy()
    n_accepted = 0
    
    for i in range(n_samples + burn_in):
        q = current_q.copy()
        p = np.random.normal(0, 1, size=q.shape)
        current_p = p.copy()
        
        p = p - step_size * grad_log_prob(q) / 2
        
        for _ in range(n_steps):
            q = q + step_size * p
            p = p - step_size * grad_log_prob(q)
        
        p = p - step_size * grad_log_prob(q) / 2
        p = -p
        
        current_U = -log_prob(current_q)
        current_K = np.sum(current_p**2) / 2
        proposed_U = -log_prob(q)
        proposed_K = np.sum(p**2) / 2
        
        if np.random.rand() < np.exp(current_U - proposed_U + current_K - proposed_K):
            current_q = q
            n_accepted += 1
        
        if i >= burn_in:
            samples.append(current_q.copy())
    
    acceptance_rate = n_accepted / (n_samples + burn_in)
    return np.array(samples), acceptance_rate


def simulated_annealing_mc(energy_func, neighbor_func, initial_state, initial_temp=1000,
                          cooling_rate=0.95, min_temp=1e-8, max_iter=10000):
    current_state = initial_state
    current_energy = energy_func(current_state)
    best_state = current_state
    best_energy = current_energy
    
    temp = initial_temp
    states = [current_state]
    energies = [current_energy]
    
    for i in range(max_iter):
        if temp < min_temp:
            break
            
        new_state = neighbor_func(current_state)
        new_energy = energy_func(new_state)
        
        delta_e = new_energy - current_energy
        
        if delta_e < 0 or np.random.rand() < np.exp(-delta_e / temp):
            current_state = new_state
            current_energy = new_energy
            
            if current_energy < best_energy:
                best_state = current_state
                best_energy = current_energy
        
        states.append(current_state)
        energies.append(current_energy)
        temp *= cooling_rate
    
    return best_state, best_energy, states, energies


def bootstrap_sampling(data, statistic_func, n_bootstrap=1000):
    n = len(data)
    bootstrap_stats = []
    
    for _ in range(n_bootstrap):
        bootstrap_sample = np.random.choice(data, size=n, replace=True)
        bootstrap_stats.append(statistic_func(bootstrap_sample))
    
    return np.array(bootstrap_stats)


def jackknife_sampling(data, statistic_func):
    n = len(data)
    jackknife_stats = []
    
    for i in range(n):
        jackknife_sample = np.concatenate([data[:i], data[i+1:]])
        jackknife_stats.append(statistic_func(jackknife_sample))
    
    return np.array(jackknife_stats)


def percolation_2d(p, size):
    grid = np.random.rand(size, size) < p
    
    def flood_fill(i, j, visited):
        if i < 0 or i >= size or j < 0 or j >= size or visited[i, j] or not grid[i, j]:
            return False
        
        visited[i, j] = True
        
        if i == size - 1:
            return True
        
        return (flood_fill(i+1, j, visited) or flood_fill(i-1, j, visited) or
                flood_fill(i, j+1, visited) or flood_fill(i, j-1, visited))
    
    visited = np.zeros((size, size), dtype=bool)
    
    for j in range(size):
        if grid[0, j] and not visited[0, j]:
            if flood_fill(0, j, visited):
                return True
    
    return False


def ising_model_2d(size, temperature, n_steps=10000):
    beta = 1.0 / temperature
    spins = np.random.choice([-1, 1], size=(size, size))
    
    energies = []
    magnetizations = []
    
    for step in range(n_steps):
        i, j = np.random.randint(0, size, 2)
        
        neighbors = (spins[(i+1)%size, j] + spins[(i-1)%size, j] + 
                    spins[i, (j+1)%size] + spins[i, (j-1)%size])
        
        delta_E = 2 * spins[i, j] * neighbors
        
        if delta_E < 0 or np.random.rand() < np.exp(-beta * delta_E):
            spins[i, j] *= -1
        
        if step % 100 == 0:
            energy = -np.sum(spins * (np.roll(spins, 1, axis=0) + np.roll(spins, 1, axis=1)))
            energies.append(energy)
            magnetizations.append(np.abs(np.mean(spins)))
    
    return spins, np.array(energies), np.array(magnetizations)


def random_walk_2d(n_steps, step_size=1):
    x, y = 0, 0
    positions = [(x, y)]
    
    for _ in range(n_steps):
        angle = np.random.uniform(0, 2*np.pi)
        x += step_size * np.cos(angle)
        y += step_size * np.sin(angle)
        positions.append((x, y))
    
    return np.array(positions)


def diffusion_limited_aggregation(n_particles, size):
    grid = np.zeros((size, size), dtype=int)
    center = size // 2
    grid[center, center] = 1
    
    for particle in range(n_particles):
        while True:
            angle = np.random.uniform(0, 2*np.pi)
            radius = size // 3
            x = int(center + radius * np.cos(angle))
            y = int(center + radius * np.sin(angle))
            
            while 0 <= x < size and 0 <= y < size and grid[x, y] == 0:
                neighbors = []
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < size and 0 <= ny < size:
                        neighbors.append(grid[nx, ny])
                
                if any(neighbors):
                    grid[x, y] = 1
                    break
                
                x += np.random.choice([-1, 0, 1])
                y += np.random.choice([-1, 0, 1])
            
            if 0 <= x < size and 0 <= y < size and grid[x, y] == 1:
                break
    
    return grid


def pi_estimation(n_samples=1000000):
    x = np.random.uniform(-1, 1, n_samples)
    y = np.random.uniform(-1, 1, n_samples)
    inside_circle = (x**2 + y**2) <= 1
    pi_estimate = 4 * np.mean(inside_circle)
    error = 4 * np.sqrt(np.var(inside_circle) / n_samples)
    return pi_estimate, error


def rejection_sampling(target_pdf, proposal_sampler, proposal_pdf, M, n_samples=1000):
    samples = []
    n_attempts = 0
    
    while len(samples) < n_samples:
        x = proposal_sampler()
        u = np.random.uniform(0, 1)
        
        if u <= target_pdf(x) / (M * proposal_pdf(x)):
            samples.append(x)
        
        n_attempts += 1
    
    efficiency = len(samples) / n_attempts
    return np.array(samples), efficiency
