import re

def tokenize(expression):
    if expression == "":
        return []
    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]
    
class Interpreter:
    def __init__(self):
        self.var = {}
        self.fun = {}
        self.pre = {}
        
        pc = -1
        
        self.pre['('] = pc
        pc += 1
        
        self.pre['='] = pc
        pc += 1
        
        self.pre['+'] = pc
        self.pre['-'] = pc
        pc += 1
        
        self.pre['*'] = pc
        self.pre['/'] = pc
        self.pre['%'] = pc
        pc += 1
        
        self.fun['='] = self.assign
        self.fun['+'] = lambda x, y: x + y
        self.fun['-'] = lambda x, y: x - y
        self.fun['*'] = lambda x, y: x * y
        self.fun['/'] = lambda x, y: x / y
        self.fun['%'] = lambda x, y: x % y
    
    def assign(self, x, y):
        self.var[x] = y
        return self.var[x]
        
    def calc(self, param, op):
        oper = op.pop()
        n2 = param.pop()
        if isinstance(n2, str):
            if n2 not in self.var:
                raise Exception
            n2 = self.var[n2]
        n1 = param.pop()
        if isinstance(n1, str) and oper != '=':
            if n1 not in self.var:
                raise Exception
            n1 = self.var[n1]
        param.append(self.fun[oper](n1, n2))
        
    def input(self, expression):
        tokens = tokenize(expression)
        n = len(tokens)
        if n == 0:
            return ''
            
        param = []
        op = []
        for tk in tokens:
            if re.match(r'^[+\-]?\d+[\.\d+]?$', tk):
                # numeric
                param.append(float(tk))
            elif re.match(r'[A-Za-z]\w*', tk):
                # identifier
                param.append(tk)
            elif tk == '(':
                op.append(tk)
            elif tk == ')':
                while len(op) > 0 and op[-1] != '(':
                    self.calc(param, op)
                if len(op) == 0:
                    raise Exception
                op.pop()
            else:
                while len(op) > 0 and self.pre[op[-1]] >= self.pre[tk]:
                    self.calc(param, op)
                op.append(tk)
        while len(op) > 0:
            self.calc(param, op)
        res = param.pop()
        if isinstance(res, str):
            if res not in self.var:
                raise Exception
            res = self.var[res]
        if len(param) != 0:
            raise Exception
        return res
        