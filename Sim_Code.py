import math
import numpy as np

# Example Input Variables
d1 = 0.010  # Diameter of section 1 in meters
d2 = 0.005  # Diameter of section 2 in meters
Flow_m3_s = 1/(10 ** 5) # Volumetric flow rate in m³/s

def PiezoHeight(d1,d2,Flow_m3_s):
    Flow_m3_min = Flow_m3_s * 60  # Convert m3/min to m3/s
    Flow_ul_hr = Flow_m3_s * (10**6) * 60 ** 2  # Convert m3/min to ul/hr
    Flow_cm3_s = (Flow_m3_s * 1000)  # Convert m3/min to cm3/s

    a1 = math.pi * ((d1 / 2) ** 2)  # Cross-sectional area of section 1 in m^2 RIGHT
    a2 = math.pi * ((d2 / 2) ** 2)  # Cross-sectional area of section 2 in m^2 RIGHT

    v1 = (Flow_m3_s)/a1   # Convert L/min to m3/s to m/s
    v2 = (Flow_m3_s)/a2  # Convert L/min to m3/s to m/s


    print(f"Flowrate in cm3_s: {Flow_cm3_s} and l_min:{Flow_m3_min} and ul_hr: {Flow_ul_hr} and m3_s: {Flow_m3_s}")
    # print(f"Velocity in section 1: {v1:.6f} m/s and section 2: {v2:.6f} m/s")
    # print(f"Area in Section 1: {a1:.6f} m^2 and Area in Section 2: {a2:.6f} m^2")
    rho_fluid = 1000  # Density of fluid (e.g., water) in kg/m^3

    delta_p = 0.5 * rho_fluid * (v2 ** 2 - v1 ** 2)

    print(f"The pressure difference is: {delta_p} Pa")

    g = 9.81  # Acceleration due to gravity in m/s^2
    delta_h = delta_p / (rho_fluid * g)

    # Calculate the height difference in the piezometer columns
    # Output results
    # print(f"Velocity in section 1: {v1:.6f} m/s")
    # print(f"Velocity in section 2: {v2:.6f} m/s")
    # print(f"Pressure difference: {delta_p:.2f} Pa")
    # print(f"Height difference in piezometer: {(delta_h*1000):.4f} mm")
    return delta_h

