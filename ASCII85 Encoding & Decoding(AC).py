import re

def toAscii85(s):
    s = list(s)
    i = 0
    n = len(s)
    res = []
    pl = 5
    while i < n:
        val = 0
        pl = 5
        
        j = 0
        while j < 4:
            if i + j < n:
                val = (val << 8) + ord(s[i + j])
                j += 1
            else:
                pl = n - i + 1
                break
        while j < 4:
            val <<= 8
            j += 1
        if val == 0 and pl == 5:
            # All null, but a full segment
            res.append(ord('z'))
            i += 4
            continue
        part = []
        for j in xrange(5):
            part.append(val % 85 + 33)
            val /= 85
        res.extend(part[::-1])
        i += 4
    while pl < 5:
        res.pop()
        pl += 1
    return '<~' + ''.join(map(chr, res)) + '~>'
    
def fromAscii85(s):
    i = 0
    s = re.sub('\s', '', s[2: len(s) - 2])
    n = len(s)
    res = []
    while i < n:
        if s[i] == 'z':
            res.extend([0, 0, 0, 0])
            i += 1
            continue
        pl = min(5, n - i)
        val = 0
        for j in xrange(pl):
            val = val * 85 + ord(s[i + j]) - 33
        for j in xrange(pl, 5):
            val = val * 85 + ord('u') - 33
        part = []
        for j in xrange(4):
            part.append(val & 0xff)
            val >>= 8
        res.extend(part[::-1])
        for j in xrange(pl, 5):
            res.pop()
        i += 5
    return ''.join(map(chr, res))
    
'''    
print(toAscii85('\0\0\0\0\0'))
print(toAscii85('easy'))
print(toAscii85('eas'))
print(toAscii85('moderate'))
print(toAscii85('somewhat difficult'))
print(fromAscii85('<~z!!~>'))
print(fromAscii85('<~ARTY*~>'))
print(fromAscii85('<~ARTW~>'))
print(fromAscii85('<~D/WrrEaa\'$~>'))
print(fromAscii85('<~F)Po,GA(E,+Co1uAnbatCif~>'))
'''