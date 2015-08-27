# This problem has Unicode test cases.
class VigenereCipher (object):
    _alpha = 0
    _al = 0
    _key = 0
    _kl = 0
    _pos = 0
    
    DEFAULT_ENCODING = 'utf8'
    
    def __init__(self, key, alphabet):
        self._alpha = alphabet.decode(self.DEFAULT_ENCODING)
        self._al = len(self._alpha)
        self._key = key.decode(self.DEFAULT_ENCODING)
        self._kl = len(self._key)
        self._pos = {}
        for i in xrange(self._al):
            self._pos[self._alpha[i]] = i
            
    def encode(self, s):
        s = s.decode(self.DEFAULT_ENCODING)
        n = len(s)
        res = []
        for i in xrange(n):
            if not s[i] in self._pos:
                res.append(s[i])
            else:
                res.append(self._alpha[(self._pos[s[i]] + self._pos[self._key[i % self._kl]]) % self._al])
                pass
        return ''.join(res).encode(self.DEFAULT_ENCODING)
        
    def decode(self, s):
        s = s.decode(self.DEFAULT_ENCODING)
        n = len(s)
        res = []
        for i in xrange(n):
            if not s[i] in self._pos:
                res.append(s[i])
            else:
                res.append(self._alpha[(self._pos[s[i]] + self._al - self._pos[self._key[i % self._kl]]) % self._al])
                pass
        return ''.join(res).encode(self.DEFAULT_ENCODING)
        