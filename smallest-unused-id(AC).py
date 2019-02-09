def next_id(arr):
    s = set(arr)
    i = 0
    while i in s:
        i += 1
    return i
