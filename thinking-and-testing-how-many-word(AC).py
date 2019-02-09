import re

def testit(s):
    s = s.lower()
    s = re.sub('[^word]', '', s)
    return len(re.findall('w.*?o.*?r.*?d', s))
