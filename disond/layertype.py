from .static import LAMBDA0, materials

class defect:
    def __init__(self, mat_type, def_len, lambda0 = LAMBDA0):
        self.mat_type = mat_type
        self.len = def_len
        mat = materials([self.mat_type], lambda0)
        self.ref = mat.ref

class quarterwave:
    def __init__(self, mat_type, lambda0 = LAMBDA0):
        self.mat_type = mat_type
        mat = materials([self.mat_type], lambda0)
        self.ref = mat.ref
        self.len = mat.qw_len

class halfwave:
    def __init__(self, mat_type, lambda0 = LAMBDA0):
        self.mat_type = mat_type
        mat = materials([self.mat_type], lambda0)
        self.ref = mat.ref
        self.len = mat.hw_len

class layer_list:
    def __init__(self, layer_list):
        self.layer_list = layer_list
        self.mat_type = [obj.mat_type for obj in layer_list]
        self.ref = np.array([obj.ref for obj in layer_list])
        self.len = np.array([obj.len for obj in layer_list])

    def __str__(self):
        return str(self.layer_list)