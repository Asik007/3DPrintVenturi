import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Example Input Variables
d1 = (0.000, 0.0254)  # Diameter of section 1 in meters
d2 = (0.000, 0.0254)  # Diameter of section 2 in meters
Flow_m3_s = [(1/(10 ** 8)), (1/60)] # Volumetric flow rate in m³/s

def PiezoHeight(d1, d2, Flow_m3_s):
    delta_h = (Flow_m3_s**2 * (1/(np.pi * (d2 / 2)**2)**2 - 1/(np.pi * (d1 / 2)**2)**2)) / (2 * 9.81)
    return delta_h



def surface_plot(func, x_range, y_range,t = Flow_m3_s, resolution=50):
    """
    Creates a surface plot of a function of two variables.

    Parameters:
    - func: The function to plot. Should take two arguments (x and y).
    - x_range: A tuple (x_min, x_max) specifying the range of x values.
    - y_range: A tuple (y_min, y_max) specifying the range of y values.
    - resolution: Number of points to sample in each direction (default is 50).

    Example usage:
    surface_plot(lambda x, y: np.sin(np.sqrt(x**2 + y**2)), (-5, 5), (-5, 5))
    """
    # Generate mesh grid for x and y
    x = np.linspace(x_range[0], x_range[1], resolution)
    y = np.linspace(y_range[0], y_range[1], resolution)
    X, Y = np.meshgrid(x, y)

    # Compute Z values using the function
    Z = func(X, Y, t)

    print(Z)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    # Plot the surface
    ax.plot_surface(X, Y, Z, cmap='viridis')
    # Show the plot
    plt.show()

# Example usage:
# surface_plot(lambda x, y: np.sin(np.sqrt(x**2 + y**2)), (-5, 5), (-5, 5))
surface_plot(PiezoHeight, d1, d2)