import re

def tokenize(expression):
    if expression == "":
        return []
    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]
    
def isid(s):
    return re.match(r'[A-Za-z]\w*', s)
        
def isnum(s):
    return re.match(r'^[+\-]?\d+[\.\d+]?$', s)
        
class Interpreter:
    MAX_PRE = 1000000
    idx = []
    
    def __init__(self):
        self.var = {}
        self.fun = {}
        self.pre = {}
        self.arg = {}
        
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
        # There're not supposed to be function in param[] or op[].
        oper = op.pop()
        n2 = param.pop()
        if isid(n2):
            if n2 in self.fun:
                raise Exception
            if n2 not in self.var:
                raise Exception
            n2 = self.var[n2]
        n1 = param.pop()
        if isid(n1):
            if n1 in self.fun:
                raise Exception
            if oper != '=':
                if n1 not in self.var:
                    raise Exception
                n1 = self.var[n1]
        if oper != '=':
            n1 = float(n1)
        n2 = float(n2)
        param.append(str(self.fun[oper](n1, n2)))
        if oper == '=' and len(op) > 0 and op[-1] == '=':
            self.calc(param, op)
        
    def input(self, expression):
        tokens = tokenize(expression)
        n = len(tokens)
        if n == 0:
            return ''
        if tokens[0] == 'fn':
            return self.declFunc(tokens)
        else:
            return float(self.eval(tokens))
            
    def declFunc(self, tokens):
        fname = tokens[1]
        if fname == 'fn' or fname in self.var:
            raise Exception
        i = tokens.index('=>')
        arg = tokens[2: i]
        sarg = set(arg)
        if len(sarg) < len(arg):
            # parameter is duplicated
            raise Exception
        expr = tokens[i + 1:]
        for term in expr:
            # validate the function definition
            if isid(term) and not term in sarg:
                raise Exception
        self.arg[fname] = arg
        self.fun[fname] = expr
        self.pre[fname] = self.MAX_PRE
        return ''
        
    def calcFunc(self, tokens):
        param = []
        op = []
        fname = tokens[self.idx[-1]]
        self.idx[-1] += 1
        while len(param) < len(self.arg[fname]):
            tk = tokens[self.idx[-1]]
            if self.idx[-1] >= len(tokens):
                raise Exception
            if isnum(tk):
                param.append(tk)
                self.idx[-1] += 1
            elif isid(tk):
                if tk in self.fun:
                    param.append(self.calcFunc(tokens))
                else:
                    if tk not in self.var:
                        # parameter not defined
                        raise Exception
                    param.append(self.var[tk])
                    self.idx[-1] += 1
            elif tk == '(':
                op.append(tk)
                self.idx[-1] += 1
            elif tk == ')':
                while len(op) > 0 and op[-1] != '(':
                    self.calc(param, op)
                if len(op) == 0:
                    raise Exception
                op.pop()
                self.idx[-1] += 1
            else:
                while len(op) > 0 and self.pre[op[-1]] >= self.pre[tk]:
                    if op[-1] == '=':
                        break
                    self.calc(param, op)
                op.append(tk)
                self.idx[-1] += 1
        arglist = {}
        arg = self.arg[fname]
        for i in xrange(len(arg)):
            arglist[arg[i]] = param[i]
        expr = self.fun[fname][:]
        for i in xrange(len(expr)):
            if expr[i] in arglist:
                expr[i] = arglist[expr[i]]
        return self.eval(expr)
        
    def eval(self, tokens):
        param = []
        op = []
        n = len(tokens)
        self.idx.append(0)
        while self.idx[-1] < n:
            tk = tokens[self.idx[-1]]
            if isnum(tk):
                # numeric
                param.append(tk)
                self.idx[-1] += 1
            elif isid(tk):
                # identifier
                if tk in self.fun:
                    # a function
                    if self.idx[-1] < n - 1 and tokens[self.idx[-1] + 1] == '=':
                        raise Exception
                    param.append(self.calcFunc(tokens))
                else:
                    param.append(tk)
                    self.idx[-1] += 1
            elif tk == '(':
                op.append(tk)
                self.idx[-1] += 1
            elif tk == ')':
                while len(op) > 0 and op[-1] != '(':
                    self.calc(param, op)
                if len(op) == 0:
                    raise Exception
                op.pop()
                self.idx[-1] += 1
            else:
                while len(op) > 0 and self.pre[op[-1]] >= self.pre[tk]:
                    if op[-1] == '=':
                        break
                    self.calc(param, op)
                op.append(tk)
                self.idx[-1] += 1
        while len(op) > 0:
            self.calc(param, op)
        res = param.pop()
        if isid(res):
            if res not in self.var:
                raise Exception
            res = self.var[res]
        if len(param) > 0:
            raise Exception
        self.idx.pop()
        return res
        