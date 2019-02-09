def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    return sorted(map(lambda x: x ** 2, array1)) == sorted(array2)
    