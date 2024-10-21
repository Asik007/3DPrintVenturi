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



def surface_plot(func, x_range, y_range,t_range, resolution=50):
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
    t = np.linspace(t_range[0], t_range[1], 10)
    X, Y, T = np.meshgrid(x, y, t)

    # Compute Z values using the function
    Z = func(X, Y, T)

    print(Z)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    mask = Z <= 0.1
    X_filtered = X[mask]
    Y_filtered = Y[mask]
    Z_filtered = T[mask]
    F_filtered = Z[mask]
    # Plot the surface
    sc = ax.scatter(X_filtered, Y_filtered, Z_filtered, c=F_filtered, cmap='viridis')
    # Add a color bar
    plt.colorbar(sc)
    # Show the plot
    plt.show()

# Example usage:
# surface_plot(lambda x, y: np.sin(np.sqrt(x**2 + y**2)), (-5, 5), (-5, 5))
surface_plot(PiezoHeight, d1, d2, Flow_m3_s)