import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider
import numpy as np
from ..constants import PI

def create_plot(title="Physics Plot", figsize=(10, 6)):
    figure, axes = plt.subplots(figsize=figsize)
    axes.set_title(title)
    return figure, axes

def plot_line_data(axes, x_data, y_data, label=None, color=None, linestyle='-'):
    line = axes.plot(x_data, y_data, label=label, color=color, linestyle=linestyle)[0]
    if label:
        axes.legend()
    return line

def plot_scatter_data(axes, x_data, y_data, label=None, color=None, marker='o', size=50):
    scatter = axes.scatter(x_data, y_data, label=label, color=color, marker=marker, s=size)
    if label:
        axes.legend()
    return scatter

def plot_vector_field(axes, X, Y, U, V, title="Vector Field"):
    axes.quiver(X, Y, U, V, scale=None)
    axes.set_title(title)
    axes.set_aspect('equal')

def plot_heatmap(axes, data, extent=None, title="Heatmap", cmap='viridis'):
    im = axes.imshow(data, extent=extent, cmap=cmap, origin='lower')
    axes.set_title(title)
    return im

def create_animation(figure, axes, frames_data, interval=50, repeat=True):
    lines = []
    
    def animate_frame(frame_idx):
        axes.clear()
        frame = frames_data[frame_idx]
        
        if 'title' in frame:
            axes.set_title(frame['title'])
        if 'xlim' in frame:
            axes.set_xlim(frame['xlim'])
        if 'ylim' in frame:
            axes.set_ylim(frame['ylim'])
            
        for plot_data in frame.get('plots', []):
            x_data = plot_data['x']
            y_data = plot_data['y']
            label = plot_data.get('label')
            color = plot_data.get('color')
            
            axes.plot(x_data, y_data, label=label, color=color)
            
        if any('label' in plot for plot in frame.get('plots', [])):
            axes.legend()
    
    anim = animation.FuncAnimation(figure, animate_frame, frames=len(frames_data), 
                                 interval=interval, repeat=repeat)
    return anim

def create_interactive_plot(data_func, param_ranges, title="Interactive Plot"):
    figure, axes = plt.subplots(figsize=(12, 8))
    plt.subplots_adjust(bottom=0.3)
    
    sliders = {}
    slider_height = 0.03
    slider_spacing = 0.04
    
    for i, (param_name, (min_val, max_val, default)) in enumerate(param_ranges.items()):
        slider_ax = plt.axes([0.2, 0.02 + i * slider_spacing, 0.6, slider_height])
        slider = Slider(slider_ax, param_name, min_val, max_val, valinit=default)
        sliders[param_name] = slider
    
    def update_plot(val):
        params = {name: slider.val for name, slider in sliders.items()}
        x_data, y_data = data_func(**params)
        
        axes.clear()
        axes.plot(x_data, y_data)
        axes.set_title(title)
        figure.canvas.draw()
    
    for slider in sliders.values():
        slider.on_changed(update_plot)
    
    params = {name: ranges[2] for name, ranges in param_ranges.items()}
    x_data, y_data = data_func(**params)
    axes.plot(x_data, y_data)
    axes.set_title(title)
    
    return figure, axes, sliders

def plot_projectile_trajectory(positions, title="Projectile Motion"):
    figure, axes = create_plot(title)
    
    x_coords = [pos[0] for pos in positions]
    y_coords = [pos[1] for pos in positions]
    
    plot_line_data(axes, x_coords, y_coords, label="Trajectory", color='blue')
    axes.set_xlabel("Horizontal Distance (m)")
    axes.set_ylabel("Height (m)")
    axes.grid(True)
    
    return figure, axes

def plot_wave_animation(x_points, wave_data, times, title="Wave Propagation"):
    figure, axes = create_plot(title)
    
    line, = axes.plot(x_points, wave_data[0])
    axes.set_ylim(-max(np.abs(wave_data[0])) * 1.2, max(np.abs(wave_data[0])) * 1.2)
    axes.set_xlabel("Position")
    axes.set_ylabel("Amplitude")
    
    def animate_wave(frame):
        line.set_ydata(wave_data[frame])
        axes.set_title(f"{title} - t = {times[frame]:.2f}s")
        return line,
    
    anim = animation.FuncAnimation(figure, animate_wave, frames=len(wave_data), 
                                 interval=50, blit=True, repeat=True)
    return figure, axes, anim

def plot_phase_space(positions, velocities, title="Phase Space"):
    figure, axes = create_plot(title)
    
    plot_line_data(axes, positions, velocities, color='red', linewidth=2)
    axes.set_xlabel("Position")
    axes.set_ylabel("Velocity")
    axes.grid(True)
    
    return figure, axes

def plot_energy_conservation(times, kinetic_energy, potential_energy, title="Energy Conservation"):
    figure, axes = create_plot(title)
    
    total_energy = np.array(kinetic_energy) + np.array(potential_energy)
    
    plot_line_data(axes, times, kinetic_energy, label="Kinetic Energy", color='red')
    plot_line_data(axes, times, potential_energy, label="Potential Energy", color='blue')
    plot_line_data(axes, times, total_energy, label="Total Energy", color='black', linestyle='--')
    
    axes.set_xlabel("Time (s)")
    axes.set_ylabel("Energy (J)")
    axes.grid(True)
    
    return figure, axes

def save_plot(figure, filename, dpi=300, bbox_inches='tight'):
    figure.savefig(filename, dpi=dpi, bbox_inches=bbox_inches)

def show_plot():
    plt.show()
