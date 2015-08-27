import re

def alphanumeric(string):
    return re.match(r'^[a-zA-Z0-9]+$', string) != None
    