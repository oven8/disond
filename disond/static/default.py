import numpy as np
from .constants import MU, KB, C

LAMBDA0 = 0.470e-6
TEMP = 300
THETA = 0
BETA = MU / (KB * TEMP)
OMEGA0 = 2 * np.pi * C / LAMBDA0
OMEGA = OMEGA0