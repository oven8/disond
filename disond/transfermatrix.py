import numpy as np
import static as st

class transfermatrix:
    def __init__(self, n, omega, theta):
        self.n = n
        self.omega = omega
        self.theta = theta
        self.kx = self.kx()
        self.kz = self.kz()
        self.kzratio = self.kzratio(dir=1)

    def kx(self):
        return np.outer(omega / st.C, np.sin(theta))

    def kz(self):
        n_broadcast = self.n[:, np.newaxis, np.newaxis]
        omega_broadcast = self.omega[np.newaxis, :, np.newaxis]
        kx_broadcast = self.kx[np.newaxis, :, :]
        return np.sqrt(((n_broadcast * omega_broadcast) / st.C)**2 - kx_broadcast**2)

    def kzratio(self, dir):
        return self.kz[dir - 1, :, :] / self.kz[dir, :, :]

    def interface(self, kratio):
        M1 = 0.5 * (1 + kratio)
        M2 = 0.5 * (1 - kratio)
        return np.array([[M1, M2],[M2, M1]])

    def propagation():
        return 0

n = np.array([1.4,2.2])
omega = np.array([1,2,3,4,5])
theta = np.array([0.1,0.2,0.3,0.4,0.5])
test = transfermatrix(n,omega,theta)
print(test.kzratio.shape)