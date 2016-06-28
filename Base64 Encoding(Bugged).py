# https://www.codewars.com/kata/base64-encoding/train/python
'''
Extend the String object to create a function that converts the value of the String to and from Base64 using the ASCII character set.

Usage:

// should return 'dGhpcyBpcyBhIHN0cmluZyEh'
'this is a string!!'.toBase64();

// should return 'this is a string!!'
'dGhpcyBpcyBhIHN0cmluZyEh'.fromBase64();
You can learn more about Base64 encoding and decoding here.
'''

def generate_dict_base64():
    s1 = ''.join(map(lambda x: chr(x + ord('A')), range(26)))
    s2 = s1.lower()
    s3 = ''.join(map(str, range(10)))
    d = s1 + s2 + s3 + '+/'
    rd = {}
    for i in xrange(len(d)):
        rd[d[i]] = i
    return d, rd

dict_base64, reverse_dict_base64 = generate_dict_base64()

def to_base_64(s):
    global dict_base64

    s = map(ord, list(s))
    n = len(s)
    res = []
    for i in xrange(0, n, 3):
        val = 0
        j = 0
        while j < 3:
            if i + j >= n:
                val <<= (3 - j) * 8
                break
            val = (val << 8) + s[i + j]
            j += 1
        tmpres = []
        tmp_len = 0
        for j in xrange(3, -1, -1):
            if val >= (1 << 6 * j):
                tmp_len = j + 1
                break
        for j in xrange(4 - tmp_len):
            val >>= 6
        for j in xrange(tmp_len):
            # big endian here
            tmpres.append(val & ((1 << 6) - 1))
            val >>= 6
        res += tmpres[: : -1]
    res = ''.join(map(lambda x: dict_base64[x], res))
    return res

def from_base_64(s):
    global reverse_dict_base64

    s = map(lambda x: reverse_dict_base64[x], list(s))
    n = len(s)
    res = []
    for i in xrange(0, n, 4):
        val = 0
        for j in xrange(4):
            val = (val << 6) + s[i + j]
        tmpres = []
        for j in xrange(3):
            # big endian here
            tmpres.append(val & ((1 << 8) - 1))
            val >>= 8
        res += tmpres[: : -1]
    while res[-1] == 0:
        res.pop()
    res = ''.join(map(chr, res))
    return res
