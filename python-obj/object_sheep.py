from object_animals import *

class Sheep(Animals):
    def SetType(self,type='sheep'):
        self.type = type

    def ShowMe(self):
        print '%s is %s ' %(self.name,self.type)

class SheepNew(Animals):
    def __init__(self,name,type):
        self.name=name
        self.type=type
        
    def SetType(self,type='sheep'):
        self.type = type

    def ShowMe(self):
        print '%s is %s ' %(self.name,self.type)

def MySheep(argc):
    if argc == 2:
        test = SheepNew
    if argc == 1 :
        test = Sheep
    print type(test)
    return test
