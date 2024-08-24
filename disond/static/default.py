import numpy as np
from .constants import MU, KB, C

LAMBDA0 = 0.470e-6
TEMP = 300
THETA = 0
BETA = MU / (KB * TEMP)
W0 = 2 * np.pi * C / LAMBDA0
OMEGA = 1