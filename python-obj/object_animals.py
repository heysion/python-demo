class Animals:
    def __init__(self):
        self.type = "animals"
        print 'animals 1'

    def __init__(self,name='AnimalsName',type='AnimalsType'):
        self.name = name
        self.type = type
        print 'animals 2'

    def __init__(self,name):
        self.type = "animals"
        self.name = name
        print 'animals 3'

