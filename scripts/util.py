import re

"""
this module if a set of utility functions
"""

def IsRepeat(str):
    if re.match(r'x\d', str):
        return True
    else:
        return False

def RemoveNoise(chord):
    chord_clean = re.sub(r'\.|\*|\(\d+/\d+\)|N|&pause', '', chord)
    chord_clean = chord_clean.split()
    chord_clean = ' '.join(chord_clean)
    return chord_clean