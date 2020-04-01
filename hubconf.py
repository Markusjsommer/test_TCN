dependencies = ['torch', 'os']

import os

def geneTCN():
    """ Pretrained Temporal Convolutional Network for bacterial gene identification."""
    foo
    dirname = os.path.dirname(__file__)
    checkpoint = os.path.join(dirname, "weights/geneTCN.pt")
    state_dict = torch.load(checkpoint)
    model.load_state_dict(state_dict)
    
    return model