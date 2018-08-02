# from keras.applications import mobilenet
from keras import layers , losses , optimizers , models 
import numpy as np
from functools import *
                                    

class SimpleModel:
    def __init__(self):
        self.l1 = layers.Conv2D(64 , (3,3) , activation = 'elu' , padding = 'same')
        self.l2 = layers.MaxPooling2D((2,2))
        self.l3 = layers.BatchNormalization()
        self.l4 = layers.Conv2D(32 , (3,3) , activation = 'elu' , padding = 'same')
        self.l5 = layers.MaxPooling2D((2,2))
        self.l6 = layers.BatchNormalization()
        self.l7 = layers.Flatten()
        self.l8 = layers.Dense(32 , activation = 'relu' )
        self.layers = [l1,l2,l3,l4,l5,l6,l7,l8]
        
    def Build(self,input):
        alllist = [input ] + self.layers
        net = reduce(lambda f,s : s(f))
        return net

