import re

def parse_molecule (formula):
    f = formula
    f = re.sub('[\[\{]', '(', f)
    f = re.sub('[\]\}]', ')', f)
    
    # Tokenizer
    n = len(f)
    a = []
    i = 0
    while i < n:
        if f[i].isupper():
            a.append(f[i])
            i += 1
        elif f[i].islower():
            a[-1] += f[i]
            i += 1
        elif f[i].isdigit():
            val = 0
            while i < n and f[i].isdigit():
                val = val * 10 + ord(f[i]) - ord('0')
                i += 1
            a.append(val)
        else:
            a.append(f[i])
            i += 1
    res = [{}]
    n = len(a)
    i = 0
    while i < n:
        if re.match(r'^[A-Z][a-z]?$', a[i]):
            elem = a[i]
            if i + 1 < n and isinstance(a[i + 1], int):
                cc = a[i + 1]
                i += 2
            else:
                cc = 1
                i += 1
            if not elem in res[-1]:
                res[-1][elem] = cc
            else:
                res[-1][elem] += cc
        elif a[i] == '(':
            res.append({})
            i += 1
        elif a[i] == ')':
            if i + 1 < n and isinstance(a[i + 1], int):
                cc = a[i + 1]
                i += 2
            else:
                cc = 1
                i += 1
            for k in res[-1]:
                if not k in res[-2]:
                    res[-2][k] = cc * res[-1][k]
                else:
                    res[-2][k] += cc * res[-1][k]
            res.pop()
    return res.pop()
    