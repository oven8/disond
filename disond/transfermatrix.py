import numpy as np
import static as st

class transfermatrix:
    def __init__(self, n, d, omega, theta):
        self.n = n
        self.d = d
        self.omega = np.atleast_1d(omega)
        self.theta = np.atleast_1d(theta)
        self.kx = self.kx()
        self.kz = self.kz()
        
    def kx(self):
        return np.outer(self.omega / st.C, np.sin(self.theta))

    def kz(self):
        n_broadcast = self.n[:, np.newaxis, np.newaxis]
        omega_broadcast = self.omega[np.newaxis, :, np.newaxis]
        kx_broadcast = self.kx[np.newaxis, :, :]
        return np.sqrt(((n_broadcast * omega_broadcast) / st.C)**2 - kx_broadcast**2)

    def kzratio(self, dir):
        return self.kz[dir[1], :, :] / self.kz[dir[0], :, :]

    def interface(self, dir):
        kzratio = self.kzratio(dir)
        M1 = 0.5 * (1 + kzratio)
        M2 = 0.5 * (1 - kzratio)
        return np.array([[M1, M2],[M2, M1]])

    def propagation(self, mat_index):
        exp = np.exp(-1j * self.kz[mat_index, :, :] * self.d[mat_index])
        return np.array([[exp, np.zeros(exp.shape)], [np.zeros(exp.shape), 1/exp]])

class TM_materials(transfermatrix):

    def __init__(self, mat_list, omega, theta):
        materials = st.materials(mat_list)
        n = materials.ref
        d = materials.len
        
        super().__init__(n, d, omega, theta)

#n = np.array([1.4,2.2])
#omega = np.array([1,2,3,4,5])
#theta = np.array([0.1,0.2,0.3,0.4,0.5])
#test = transfermatrix(n,omega,theta)
#print(test.kzratio.shape)
TNM = TM_materials(["Air","SiO2","TiO2"],2,1)
print(TNM.propagation(2).shape)