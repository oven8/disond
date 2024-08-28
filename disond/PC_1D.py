import numpy as np
import matplotlib.pyplot as plt
from .transfermatrix import TM_materials
from .static import OMEGA, THETA, LAMBDA0

class bilayer_PC:
    def __init__(self, mat_list, sequence, omega = OMEGA, theta = THETA, lambda0 = LAMBDA0, air = True):
        if len(mat_list) > 2:
            raise ValueError("Bilayer module only supports two materials!")
        self.air = air
        if self.air == True:
            self.mat_list = mat_list + ["Air"]
        self.sequence = sequence
        self.omega = omega
        self.theta = theta
        self.lambda0 = lambda0

    @property
    def __mat_mul(self):
        if self.air == True and self.sequence[0] == 0:
            M = self.MA0
        elif self.air == True and self.sequence[0] == 1:
            M = self.MA1
        for mat_index in range(len(self.sequence)-1):
            if self.sequence[mat_index] == 0 and self.sequence[mat_index+1] == 0:
                M = np.einsum('ijxy,jkxy->ikxy', M, self.M0)
            elif self.sequence[mat_index] == 0 and self.sequence[mat_index+1] == 1:
                M = np.einsum('ijxy,jkxy,klxy->ilxy', M, self.M0, self.M01)
            elif self.sequence[mat_index] == 1 and self.sequence[mat_index+1] == 1:
                M = np.einsum('ijxy,jkxy->ikxy', M, self.M1)
            elif self.sequence[mat_index] == 1 and self.sequence[mat_index+1] == 0:
                M = np.einsum('ijxy,jkxy,klxy->ilxy', M, self.M1, self.M10)
        if self.air == True:
            if self.sequence[-1] == 0:
                M = np.einsum('ijxy,jkxy,klxy->ilxy', M, self.M0, self.M0A)
            elif self.sequence[-1] == 1:
                M = np.einsum('ijxy,jkxy,klxy->ilxy', M, self.M1, self.M1A)
        elif self.air == False:
            if self.sequence[-1] == 0:
                M = np.einsum('ijxy,jkxy->ikxy', M, self.M0)
            elif self.sequence[-1] == 1:
                M = np.einsum('ijxy,jkxy->ikxy', M, self.M1)
        return M

    @property
    def calculate_matrices(self):
        matrix_generate = TM_materials(self.mat_list, self.omega, self.theta, lambda0 = self.lambda0)
        self.M0 = matrix_generate.propagation(0)
        self.M1 = matrix_generate.propagation(1)
        self.M01 = matrix_generate.interface([0, 1])
        self.M10 = matrix_generate.interface([1, 0])
        if self.air == True:
            self.MA0 = matrix_generate.interface([2, 0])
            self.M0A = matrix_generate.interface([0, 2])
            self.MA1 = matrix_generate.interface([2, 1])
            self.M1A = matrix_generate.interface([1, 2])
        self.M = self.__mat_mul

    @property
    def calculate_coefficients(self):
        self.T = np.abs(1/self.M[0,0,:,:])**2
        self.R = np.abs(self.M[1,0,:,:]/self.M[0,0,:,:])**2
        self.MTr = np.einsum('iixy->xy', self.M)
        self.Mdet = self.M[0,0,:,:] * self.M[1,1,:,:] - self.M[0,1,:,:] * self.M[1,0,:,:]

    @property
    def plot_transmission_bands(self):
        theta_grid, omega_grid = np.meshgrid(self.theta, self.omega)
        f1, ax = plt.subplots()
        cs = ax.contourf(theta_grid, omega_grid, self.T) #'LineColor', 'none')
        cbar = f1.colorbar(cs)
        cbar.set_label('T')
        ax.set_xlabel('theta')
        ax.set_ylabel('omega')
        plt.show()