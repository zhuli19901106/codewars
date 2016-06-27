def next_permutation(s):
    n = len(s)
    if n < 2:
        return False
    i = n - 1
    while i > 0:
        if s[i - 1] < s[i]:
            break
        i -= 1
    if i == 0:
        return False
    j = i
    while j < n and s[j] > s[i - 1]:
        j += 1
    s[i - 1], s[j - 1] = s[j - 1], s[i - 1]
    s[i: ] = s[i: ][: : -1]
    return True
    
def permutations(s):
    s = sorted(list(s))
    has_next = True
    p = []
    while has_next:
        p.append(''.join(s))
        has_next = next_permutation(s)
    return p

'''
print permutations('ab')
print permutations('abab')
'''
