def char_concat(word):
    n = len(word)
    i = 0
    j = n - 1
    k = 1
    ans = []
    while i < j:
        ans.append(word[i])
        ans.append(word[j])
        ans.append(str(k))
        i += 1
        j -= 1
        k += 1
    return ''.join(ans)
    