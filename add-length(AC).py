import re

def add_length(s):
    return [val + ' ' + str(len(val)) for val in re.split('\s+', s)]
    