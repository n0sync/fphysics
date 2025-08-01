import numpy as np
from scipy.optimize import minimize


def gradient_descent(f, grad_f, x0, learning_rate=0.01, tol=1e-6, max_iter=10000):
    x = x0.copy()
    history = [x.copy()]
    
    for i in range(max_iter):
        grad = grad_f(x)
        x_new = x - learning_rate * grad
        
        if np.linalg.norm(x_new - x) < tol:
            break
            
        x = x_new
        history.append(x.copy())
    
    return x, history


def gradient_descent_adaptive(f, grad_f, x0, initial_lr=0.01, tol=1e-6, max_iter=10000, 
                             decay_rate=0.9, increase_factor=1.1):
    x = x0.copy()
    learning_rate = initial_lr
    history = [x.copy()]
    prev_f = f(x)
    
    for i in range(max_iter):
        grad = grad_f(x)
        x_new = x - learning_rate * grad
        current_f = f(x_new)
        
        if current_f < prev_f:
            learning_rate *= increase_factor
        else:
            learning_rate *= decay_rate
        
        if np.linalg.norm(x_new - x) < tol:
            break
            
        x = x_new
        prev_f = current_f
        history.append(x.copy())
    
    return x, history


def momentum_gradient_descent(f, grad_f, x0, learning_rate=0.01, momentum=0.9, 
                             tol=1e-6, max_iter=10000):
    x = x0.copy()
    velocity = np.zeros_like(x)
    history = [x.copy()]
    
    for i in range(max_iter):
        grad = grad_f(x)
        velocity = momentum * velocity - learning_rate * grad
        x_new = x + velocity
        
        if np.linalg.norm(x_new - x) < tol:
            break
            
        x = x_new
        history.append(x.copy())
    
    return x, history


def adam_optimizer(f, grad_f, x0, learning_rate=0.001, beta1=0.9, beta2=0.999, 
                   epsilon=1e-8, tol=1e-6, max_iter=10000):
    x = x0.copy()
    m = np.zeros_like(x)
    v = np.zeros_like(x)
    history = [x.copy()]
    
    for i in range(1, max_iter + 1):
        grad = grad_f(x)
        
        m = beta1 * m + (1 - beta1) * grad
        v = beta2 * v + (1 - beta2) * grad**2
        
        m_hat = m / (1 - beta1**i)
        v_hat = v / (1 - beta2**i)
        
        x_new = x - learning_rate * m_hat / (np.sqrt(v_hat) + epsilon)
        
        if np.linalg.norm(x_new - x) < tol:
            break
            
        x = x_new
        history.append(x.copy())
    
    return x, history


def conjugate_gradient(A, b, x0=None, tol=1e-6, max_iter=None):
    n = len(b)
    if x0 is None:
        x = np.zeros(n)
    else:
        x = x0.copy()
    
    if max_iter is None:
        max_iter = n
    
    r = b - A @ x
    p = r.copy()
    rsold = r @ r
    
    for i in range(max_iter):
        Ap = A @ p
        alpha = rsold / (p @ Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rsnew = r @ r
        
        if np.sqrt(rsnew) < tol:
            break
        
        beta = rsnew / rsold
        p = r + beta * p
        rsold = rsnew
    
    return x


def nelder_mead(f, x0, alpha=1.0, gamma=2.0, rho=0.5, sigma=0.5, tol=1e-6, max_iter=10000):
    n = len(x0)
    simplex = np.zeros((n + 1, n))
    simplex[0] = x0
    
    for i in range(1, n + 1):
        simplex[i] = x0.copy()
        simplex[i, i-1] += 0.05 if x0[i-1] != 0 else 0.00025
    
    f_values = np.array([f(x) for x in simplex])
    
    for iteration in range(max_iter):
        indices = np.argsort(f_values)
        simplex = simplex[indices]
        f_values = f_values[indices]
        
        if np.max([np.linalg.norm(simplex[i] - simplex[0]) for i in range(1, n + 1)]) < tol:
            break
        
        centroid = np.mean(simplex[:-1], axis=0)
        
        reflected = centroid + alpha * (centroid - simplex[-1])
        f_reflected = f(reflected)
        
        if f_values[0] <= f_reflected < f_values[-2]:
            simplex[-1] = reflected
            f_values[-1] = f_reflected
        elif f_reflected < f_values[0]:
            expanded = centroid + gamma * (reflected - centroid)
            f_expanded = f(expanded)
            if f_expanded < f_reflected:
                simplex[-1] = expanded
                f_values[-1] = f_expanded
            else:
                simplex[-1] = reflected
                f_values[-1] = f_reflected
        else:
            contracted = centroid + rho * (simplex[-1] - centroid)
            f_contracted = f(contracted)
            if f_contracted < f_values[-1]:
                simplex[-1] = contracted
                f_values[-1] = f_contracted
            else:
                for i in range(1, n + 1):
                    simplex[i] = simplex[0] + sigma * (simplex[i] - simplex[0])
                    f_values[i] = f(simplex[i])
    
    return simplex[0]


def simulated_annealing(f, x0, neighbor_func, initial_temp=1000, cooling_rate=0.95, 
                       min_temp=1e-8, max_iter=10000):
    current_x = x0.copy()
    current_f = f(current_x)
    best_x = current_x.copy()
    best_f = current_f
    
    temp = initial_temp
    history = [(current_x.copy(), current_f)]
    
    for i in range(max_iter):
        if temp < min_temp:
            break
        
        new_x = neighbor_func(current_x)
        new_f = f(new_x)
        
        delta_f = new_f - current_f
        
        if delta_f < 0 or np.random.rand() < np.exp(-delta_f / temp):
            current_x = new_x
            current_f = new_f
            
            if current_f < best_f:
                best_x = current_x.copy()
                best_f = current_f
        
        history.append((current_x.copy(), current_f))
        temp *= cooling_rate
    
    return best_x, best_f, history


def genetic_algorithm(f, bounds, population_size=50, generations=1000, 
                     mutation_rate=0.1, crossover_rate=0.8, elitism=0.1):
    n_vars = len(bounds)
    n_elite = int(elitism * population_size)
    
    population = np.random.uniform(
        low=[b[0] for b in bounds],
        high=[b[1] for b in bounds],
        size=(population_size, n_vars)
    )
    
    for generation in range(generations):
        fitness = np.array([f(individual) for individual in population])
        sorted_indices = np.argsort(fitness)
        
        elite = population[sorted_indices[:n_elite]]
        
        new_population = list(elite)
        
        while len(new_population) < population_size:
            parent1_idx = tournament_selection(fitness, k=3)
            parent2_idx = tournament_selection(fitness, k=3)
            
            parent1 = population[parent1_idx]
            parent2 = population[parent2_idx]
            
            if np.random.rand() < crossover_rate:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1.copy(), parent2.copy()
            
            if np.random.rand() < mutation_rate:
                child1 = mutate(child1, bounds)
            if np.random.rand() < mutation_rate:
                child2 = mutate(child2, bounds)
            
            new_population.extend([child1, child2])
        
        population = np.array(new_population[:population_size])
    
    fitness = np.array([f(individual) for individual in population])
    best_idx = np.argmin(fitness)
    
    return population[best_idx], fitness[best_idx]


def tournament_selection(fitness, k=3):
    tournament_indices = np.random.choice(len(fitness), k, replace=False)
    tournament_fitness = fitness[tournament_indices]
    winner_idx = tournament_indices[np.argmin(tournament_fitness)]
    return winner_idx


def crossover(parent1, parent2):
    alpha = np.random.rand()
    child1 = alpha * parent1 + (1 - alpha) * parent2
    child2 = (1 - alpha) * parent1 + alpha * parent2
    return child1, child2


def mutate(individual, bounds, mutation_strength=0.1):
    mutated = individual.copy()
    for i in range(len(individual)):
        if np.random.rand() < 0.1:
            mutation = np.random.normal(0, mutation_strength * (bounds[i][1] - bounds[i][0]))
            mutated[i] = np.clip(mutated[i] + mutation, bounds[i][0], bounds[i][1])
    return mutated


def particle_swarm_optimization(f, bounds, n_particles=30, max_iter=1000, 
                               w=0.729, c1=1.494, c2=1.494):
    n_vars = len(bounds)
    
    positions = np.random.uniform(
        low=[b[0] for b in bounds],
        high=[b[1] for b in bounds],
        size=(n_particles, n_vars)
    )
    
    velocities = np.random.uniform(-1, 1, size=(n_particles, n_vars))
    
    personal_best_positions = positions.copy()
    personal_best_fitness = np.array([f(p) for p in positions])
    
    global_best_idx = np.argmin(personal_best_fitness)
    global_best_position = personal_best_positions[global_best_idx].copy()
    global_best_fitness = personal_best_fitness[global_best_idx]
    
    for iteration in range(max_iter):
        for i in range(n_particles):
            r1, r2 = np.random.rand(2)
            
            velocities[i] = (w * velocities[i] + 
                           c1 * r1 * (personal_best_positions[i] - positions[i]) + 
                           c2 * r2 * (global_best_position - positions[i]))
            
            positions[i] += velocities[i]
            
            for j in range(n_vars):
                positions[i, j] = np.clip(positions[i, j], bounds[j][0], bounds[j][1])
            
            fitness = f(positions[i])
            
            if fitness < personal_best_fitness[i]:
                personal_best_positions[i] = positions[i].copy()
                personal_best_fitness[i] = fitness
                
                if fitness < global_best_fitness:
                    global_best_position = positions[i].copy()
                    global_best_fitness = fitness
    
    return global_best_position, global_best_fitness


def differential_evolution(f, bounds, population_size=15, max_iter=1000, 
                          F=0.5, CR=0.7):
    n_vars = len(bounds)
    
    population = np.random.uniform(
        low=[b[0] for b in bounds],
        high=[b[1] for b in bounds],
        size=(population_size, n_vars)
    )
    
    fitness = np.array([f(individual) for individual in population])
    
    for generation in range(max_iter):
        for i in range(population_size):
            indices = list(range(population_size))
            indices.remove(i)
            a, b, c = np.random.choice(indices, 3, replace=False)
            
            mutant = population[a] + F * (population[b] - population[c])
            
            for j in range(n_vars):
                mutant[j] = np.clip(mutant[j], bounds[j][0], bounds[j][1])
            
            trial = population[i].copy()
            j_rand = np.random.randint(n_vars)
            
            for j in range(n_vars):
                if np.random.rand() < CR or j == j_rand:
                    trial[j] = mutant[j]
            
            trial_fitness = f(trial)
            
            if trial_fitness < fitness[i]:
                population[i] = trial
                fitness[i] = trial_fitness
    
    best_idx = np.argmin(fitness)
    return population[best_idx], fitness[best_idx]


def bfgs_optimization(f, grad_f, x0, tol=1e-6, max_iter=1000):
    n = len(x0)
    x = x0.copy()
    H = np.eye(n)
    
    for i in range(max_iter):
        grad = grad_f(x)
        
        if np.linalg.norm(grad) < tol:
            break
        
        p = -H @ grad
        
        alpha = line_search(f, grad_f, x, p)
        
        s = alpha * p
        x_new = x + s
        y = grad_f(x_new) - grad
        
        if s @ y > 1e-10:
            rho = 1.0 / (y @ s)
            I = np.eye(n)
            H = (I - rho * np.outer(s, y)) @ H @ (I - rho * np.outer(y, s)) + rho * np.outer(s, s)
        
        x = x_new
    
    return x


def line_search(f, grad_f, x, p, alpha0=1.0, c1=1e-4, c2=0.9, max_iter=20):
    alpha = alpha0
    phi0 = f(x)
    dphi0 = grad_f(x) @ p
    
    for i in range(max_iter):
        phi_alpha = f(x + alpha * p)
        
        if phi_alpha <= phi0 + c1 * alpha * dphi0:
            dphi_alpha = grad_f(x + alpha * p) @ p
            if dphi_alpha >= c2 * dphi0:
                return alpha
        
        alpha *= 0.5
    
    return alpha
