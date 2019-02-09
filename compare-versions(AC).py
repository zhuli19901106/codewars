import re

def compare_versions(v1, v2):
    v1 = map(int, re.split('\.', v1))
    v2 = map(int, re.split('\.', v2))
    i = 0
    while True:
        if i >= len(v2):
            return True
        elif i >= len(v1):
            return False
        elif v1[i] == v2[i]:
            i += 1
            continue
        else:
            return True if v1[i] > v2[i] else False
            