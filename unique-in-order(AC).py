def unique_in_order(iterable):
    a = list(iterable)
    n = len(a)
    i = 0
    b = []
    while i < n:
        j = i + 1
        while j < n and a[i] == a[j]:
            j += 1
        b.append(a[i])
        i = j
    return b
    