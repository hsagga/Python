'''
Created on Sep 7, 2017

@author: lil_h
'''

class pets():
    
    def __init__(self, breedIn, nameIn):
        self.breed = breedIn
        self.name = nameIn
        
        
    def getName(self):
        return self.name
    
    def setName(self, nameIn):
        self.name = nameIn