import re

def DNAtoRNA(dna):
    return re.sub('T', 'U', dna)
    