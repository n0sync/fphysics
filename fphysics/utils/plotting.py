import math

def plot_function(func, x_range, num_points=100, title=None, xlabel='x', ylabel='y'):
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        x = np.linspace(x_range[0], x_range[1], num_points)
        y = [func(xi) for xi in x]
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'b-', linewidth=2)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title or f'Function Plot')
        plt.grid(True, alpha=0.3)
        plt.show()
        
    except ImportError:
        print("Matplotlib not available. Install with: pip install matplotlib")
        return None

def plot_vector_field(func, x_range, y_range, num_points=20, title=None):
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        x = np.linspace(x_range[0], x_range[1], num_points)
        y = np.linspace(y_range[0], y_range[1], num_points)
        X, Y = np.meshgrid(x, y)
        
        U, V = func(X, Y)
        
        plt.figure(figsize=(10, 8))
        plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(title or 'Vector Field')
        plt.grid(True, alpha=0.3)
        plt.axis('equal')
        plt.show()
        
    except ImportError:
        print("Matplotlib not available. Install with: pip install matplotlib")
        return None

def plot_phase_portrait(dx_dt, dy_dt, x_range, y_range, num_points=20, title=None):
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        x = np.linspace(x_range[0], x_range[1], num_points)
        y = np.linspace(y_range[0], y_range[1], num_points)
        X, Y = np.meshgrid(x, y)
        
        DX = dx_dt(X, Y)
        DY = dy_dt(X, Y)
        
        M = np.sqrt(DX**2 + DY**2)
        M[M == 0] = 1
        DX_norm, DY_norm = DX/M, DY/M
        
        plt.figure(figsize=(10, 8))
        plt.quiver(X, Y, DX_norm, DY_norm, M, cmap='viridis')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(title or 'Phase Portrait')
        plt.colorbar(label='Magnitude')
        plt.grid(True, alpha=0.3)
        plt.show()
        
    except ImportError:
        print("Matplotlib not available. Install with: pip install matplotlib")
        return None

def plot_motion_diagram(positions, velocities=None, accelerations=None, time_steps=None, title=None):
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        if time_steps is None:
            time_steps = list(range(len(positions)))
        
        x_pos = [pos[0] for pos in positions]
        y_pos = [pos[1] for pos in positions]
        
        plt.figure(figsize=(12, 8))
        
        plt.subplot(2, 2, 1)
        plt.plot(x_pos, y_pos, 'b-o', markersize=4)
        plt.xlabel('x position')
        plt.ylabel('y position')
        plt.title('Trajectory')
        plt.grid(True, alpha=0.3)
        
        plt.subplot(2, 2, 2)
        plt.plot(time_steps, x_pos, 'r-', label='x')
        plt.plot(time_steps, y_pos, 'g-', label='y')
        plt.xlabel('Time')
        plt.ylabel('Position')
        plt.title('Position vs Time')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        if velocities:
            vx = [vel[0] for vel in velocities]
            vy = [vel[1] for vel in velocities]
            
            plt.subplot(2, 2, 3)
            plt.plot(time_steps, vx, 'r-', label='vx')
            plt.plot(time_steps, vy, 'g-', label='vy')
            plt.xlabel('Time')
            plt.ylabel('Velocity')
            plt.title('Velocity vs Time')
            plt.legend()
            plt.grid(True, alpha=0.3)
        
        if accelerations:
            ax = [acc[0] for acc in accelerations]
            ay = [acc[1] for acc in accelerations]
            
            plt.subplot(2, 2, 4)
            plt.plot(time_steps, ax, 'r-', label='ax')
            plt.plot(time_steps, ay, 'g-', label='ay')
            plt.xlabel('Time')
            plt.ylabel('Acceleration')
            plt.title('Acceleration vs Time')
            plt.legend()
            plt.grid(True, alpha=0.3)
        
        plt.suptitle(title or 'Motion Diagram')
        plt.tight_layout()
        plt.show()
        
    except ImportError:
        print("Matplotlib not available. Install with: pip install matplotlib")
        return None

def plot_energy_diagram(kinetic_energy, potential_energy, time_steps=None, title=None):
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        if time_steps is None:
            time_steps = list(range(len(kinetic_energy)))
        
        total_energy = [k + p for k, p in zip(kinetic_energy, potential_energy)]
        
        plt.figure(figsize=(12, 6))
        plt.plot(time_steps, kinetic_energy, 'r-', label='Kinetic Energy', linewidth=2)
        plt.plot(time_steps, potential_energy, 'b-', label='Potential Energy', linewidth=2)
        plt.plot(time_steps, total_energy, 'g--', label='Total Energy', linewidth=2)
        plt.xlabel('Time')
        plt.ylabel('Energy')
        plt.title(title or 'Energy vs Time')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
        
    except ImportError:
        print("Matplotlib not available. Install with: pip install matplotlib")
        return None

def plot_wave(wave_func, x_range, time_values, title=None):
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        x = np.linspace(x_range[0], x_range[1], 200)
        
        plt.figure(figsize=(12, 8))
        
        for i, t in enumerate(time_values):
            y = [wave_func(xi, t) for xi in x]
            plt.plot(x, y, label=f't = {t:.2f}')
        
        plt.xlabel('Position')
        plt.ylabel('Amplitude')
        plt.title(title or 'Wave Propagation')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
        
    except ImportError:
        print("Matplotlib not available. Install with: pip install matplotlib")
        return None

def plot_pendulum(angles, times, title=None):
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        plt.figure(figsize=(12, 8))
        
        plt.subplot(2, 1, 1)
        plt.plot(times, angles, 'b-', linewidth=2)
        plt.xlabel('Time (s)')
        plt.ylabel('Angle (rad)')
        plt.title('Pendulum Angle vs Time')
        plt.grid(True, alpha=0.3)
        
        plt.subplot(2, 1, 2)
        x_pos = [math.sin(angle) for angle in angles]
        y_pos = [-math.cos(angle) for angle in angles]
        plt.plot(x_pos, y_pos, 'r-', alpha=0.7)
        plt.plot(0, 0, 'ko', markersize=8)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Pendulum Trajectory')
        plt.axis('equal')
        plt.grid(True, alpha=0.3)
        
        plt.suptitle(title or 'Pendulum Motion')
        plt.tight_layout()
        plt.show()
        
    except ImportError:
        print("Matplotlib not available. Install with: pip install matplotlib")
        return None

def plot_frequency_spectrum(amplitudes, frequencies, title=None):
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        plt.figure(figsize=(12, 6))
        plt.plot(frequencies, amplitudes, 'b-', linewidth=2)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude')
        plt.title(title or 'Frequency Spectrum')
        plt.grid(True, alpha=0.3)
        plt.show()
        
    except ImportError:
        print("Matplotlib not available. Install with: pip install matplotlib")
        return None

def plot_stress_strain(stress, strain, title=None):
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        plt.figure(figsize=(10, 6))
        plt.plot(strain, stress, 'b-', linewidth=2)
        plt.xlabel('Strain')
        plt.ylabel('Stress (Pa)')
        plt.title(title or 'Stress-Strain Curve')
        plt.grid(True, alpha=0.3)
        plt.show()
        
    except ImportError:
        print("Matplotlib not available. Install with: pip install matplotlib")
        return None

def plot_3d_surface(func, x_range, y_range, num_points=50, title=None):
    try:
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        import numpy as np
        
        x = np.linspace(x_range[0], x_range[1], num_points)
        y = np.linspace(y_range[0], y_range[1], num_points)
        X, Y = np.meshgrid(x, y)
        Z = func(X, Y)
        
        fig = plt.figure(figsize=(12, 9))
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(title or '3D Surface Plot')
        fig.colorbar(surf)
        plt.show()
        
    except ImportError:
        print("Matplotlib not available. Install with: pip install matplotlib")
        return None

def plot_contour(func, x_range, y_range, num_points=100, title=None):
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        x = np.linspace(x_range[0], x_range[1], num_points)
        y = np.linspace(y_range[0], y_range[1], num_points)
        X, Y = np.meshgrid(x, y)
        Z = func(X, Y)
        
        plt.figure(figsize=(10, 8))
        contour = plt.contour(X, Y, Z, levels=20)
        plt.clabel(contour, inline=True, fontsize=8)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(title or 'Contour Plot')
        plt.colorbar()
        plt.grid(True, alpha=0.3)
        plt.show()
        
    except ImportError:
        print("Matplotlib not available. Install with: pip install matplotlib")
        return None
