import numpy as np
import transfermatrix as TM
import static as st

class bilayer_PC:
    def __init__(self, mat_list, sequence, omega = st.OMEGA, theta = st.THETA, lambda0 = st.LAMBDA0, air = True):
        if mat_list.len() > 2:
            raise ValueError("Bilayer module only supports two materials!")
        if air is True:
            self.mat_list = mat_list + ["Air"]
        self.sequence = sequence
        self.omega = omega
        self.theta = theta
        self.lambda0 = lambda0
        self.TM = TM.TM_materials(mat_list, mat_list, omega, theta, lambda0 = lambda0)
        self.M0 = self.TM.propagation(0)
        self.M1 = self.TM.propagation(1)
        self.M01 = self.TM.interface([0, 1])
        self.M10 = self.TM.interface([1, 0])
        if air is True:
            self.MA0 = self.TM.interface([2, 0])
            self.M0A = self.TM.interface([0, 2])
            self.MA1 = self.TM.interface([2, 1])
            self.M1A = self.TM.interface([1, 2])
