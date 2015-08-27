class Plugboard(object):
    __m__ = {}
    
    def __init__(self, wires = ''):
        n = len(wires)
        if n & 1 or n > 20:
            raise Exception
        if len(set(list(wires))) < n:
            raise Exception
        self.__m__ = {}
        for i in xrange(0, n, 2):
            self.__m__[wires[i]] = wires[i + 1]
            self.__m__[wires[i + 1]] = wires[i]
            
    def process(self, c):
        return self.__m__[c] if c in self.__m__.keys() else c
        