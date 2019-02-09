import re

def filter_string(string):
    return int(re.sub(r'\D', '', string))
    