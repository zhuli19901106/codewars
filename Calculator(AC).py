import re

class Calculator(object):
    __pre__ = {}
    __op__ = {}
    
    def __init__(self):
        i = -1
        
        self.__pre__['('] = i
        i += 1
        
        self.__pre__['+'] = i
        self.__pre__['-'] = i
        i += 1
        
        self.__pre__['*'] = i
        self.__pre__['/'] = i
        i += 1
        
        self.__op__['+'] = lambda x, y: x + y
        self.__op__['-'] = lambda x, y: x - y
        self.__op__['*'] = lambda x, y: x * y
        self.__op__['/'] = lambda x, y: x / y
    
    def calc(self, num, op):
        n2 = num.pop()
        n1 = num.pop()
        oper = op.pop()
        num.append(self.__op__[oper](n1, n2))
        
    def evaluate(self, string):
        s = string
        a = re.split(r'\s+', s)
        num = []
        op = []
        n = len(a)
        for i in xrange(n):
            if re.match(r'^[+\-]?\d+(\.\d+)?$', a[i]):
                num.append(float(a[i]))
            elif a[i] == '(':
                op.append(a[i])
            elif a[i] == ')':
                while op[-1] != '(':
                    self.calc(num, op)
                op.pop()
            else:
                while len(op) > 0 and self.__pre__[op[-1]] >= self.__pre__[a[i]]:
                    self.calc(num, op)
                op.append(a[i])
        
        while len(op) > 0:
            self.calc(num, op)
        
        return round(num[0], 10) if len(a) > 0 else 0
        