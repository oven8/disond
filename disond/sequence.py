from .layertype import layer_list

def layertype_list(layer_sequence):
    layertype_list = list(set(layer_sequence))
    return layer_list(layertype_list)

def periodic_sequence(layertype_list, period):
    return layer_list(layertype_list * period)

def fabry_perot_sequence(layertype_list, left_period, right_period):
    return layer_list(layertype_list * left_period + layertype_list[::-1] * right_period)

