def validBraces(s):
    lb = set(['(', '[', '{'])
    rb = {')': '(', ']': '[', '}': '{'}
    
    st = []
    for ch in s:
        if ch in lb:
            st.append(ch)
        elif len(st) == 0 or rb[ch] != st[-1]:
            return False
        else:
            st.pop()
    return len(st) == 0
    