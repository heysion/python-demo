import random
import pdb
class TestSingleton(object):
    def __init__(self):
        self._random = random.random()
        pass

    @classmethod
    def instance(cls):
        if not hasattr(cls,"_inst"):
            cls._inst = cls()
        return cls._inst

    def printd(self):
#        pdb.set_trace()
        print self._random

    def __new__(cls):
        if not hasattr(cls,"_inst"):
            cls._inst = cls
        if not hasattr(cls,"_random"):
            setattr(cls._inst,"_random",random.random())
        cls._inst.random = random.random()
        return cls._inst


if __name__ == "__main__":
    a = TestSingleton()
    b = TestSingleton()
    print id(a),id(b)
    print a._random
    print b._random
    pass
