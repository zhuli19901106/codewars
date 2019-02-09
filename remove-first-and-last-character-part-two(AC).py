def array(string):
    a = string.split(',')
    if len(a) > 2:
        return ' '.join(a[1:-1])
    else:
        return None
