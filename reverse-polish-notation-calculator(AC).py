import re

def calc(expr):
    op = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    
    if len(expr) == 0:
        return 0
    a = re.split('\s+', expr)
    st = []
    for val in a:
        if re.match('^\d+(.\d+)?$', val):
            st.append(float(val))
        else:
            v2 = st.pop()
            v1 = st.pop()
            st.append(op[val](v1, v2))
    return st.pop()
    