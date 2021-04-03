import re

def IsRepeat(str):
    if re.match(r'x\d', str):
        return True
    else:
        return False

def RemoveNoise(chord):
    chord_clean = re.sub(r'\.|\*|\(\d+/\d+\)|N', '', chord)
    chord_clean = chord_clean.split()
    chord_clean = ' '.join(chord_clean)
    return chord_clean