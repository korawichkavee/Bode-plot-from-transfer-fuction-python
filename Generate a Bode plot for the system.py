from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
from scipy.signal import bode
import numpy as np

# Transfer function parameters
K = 10      # Gain
zero = 0   
pole1 = 1/2
pole2 = 1

# Create the transfer function
num = [K]  # Numerator coefficients
den = [pole1*pole2, pole1+pole2, 0]  # Denominator coefficients
system = TransferFunction(num, den)

# Generate a Bode plot for the system
frequencies = np.logspace(-1, 2, num=1000)  # rad/s
w, mag, phase = bode(system, frequencies)

# Bode magnitude plot
plt.figure()
plt.semilogx(w, mag)
plt.title('Bode Plot - Magnitude')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Magnitude [dB]')
plt.grid(True, which="both", ls="--")

# Bode phase plot
plt.figure()
plt.semilogx(w, phase)
plt.title('Bode Plot - Phase')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Phase [degrees]')
plt.grid(True, which="both", ls="--")

# Show the plots
plt.show()
