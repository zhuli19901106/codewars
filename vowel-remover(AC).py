import re

def shortcut(s):
    return re.sub('[aeiou]', '', s)
    