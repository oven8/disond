import numpy as np
from .default import LAMBDA0

class materials:
    def __init__(self, mat_list, lambda0 = LAMBDA0):
        self.lambda0 = lambda0
        self.mat_list = mat_list
        self.ref = self.mat_ref()
        self.len = self.mat_len()
    
    def mat_ref(self):
        mat = {
            'Air' : 1.0,
            'SiO2' : np.sqrt(1+0.6961663/(1-(0.0684043/(self.lambda0*10**6))**2)+0.4079426/(1-(0.1162414/(self.lambda0*10**6))**2)+0.8974794/(1-(9.896161/(self.lambda0*10**6))**2)),
            'TiO2' : np.sqrt(5.913+0.2441/((self.lambda0*10**6)**2-0.0803))
        }
        result = []
        for material in self.mat_list:
            if material in mat:
                result.append(mat[material])
            else:
                raise ValueError("Material not found!")
    
        return np.array(result)

    def mat_len(self):
        width = (self.lambda0/4)/np.real(self.ref)
        return width

#mat = materials(['SiO2','TiO2'])
#print(mat.ref)