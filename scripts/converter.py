"""
this module is a set of functions to convert raw chords in to desired formats, 
such as relative chords and inC chords.
"""

def Raw2Basic(chord_raw):
    root = chord_raw.split(':')[0]
    func = chord_raw.split(':')[1].split('/')[0]
    
    if func[:3]=='maj':
        func = 'maj'
    elif func[:3]=='min':
        func = 'min'
    elif func[:3]=='sus':
        func = func[:4]
    elif func[0]=='1' or func[0]=='5':
        func = '15'
    
    chord_basic = root+':'+func
    return chord_basic

def Raw2Root(chord_raw):
    root = chord_raw.split(':')[0]
    return root

def GetEnharmonic(note):
    if note == 'Db':
        return 'C#'
    elif note == 'Eb':
        return 'D#'
    elif note == 'E#':
        return 'F'
    elif note == 'Fb':
        return 'E'
    elif note == 'Gb':
        return 'F#'
    elif note == 'Ab':
        return 'G#'
    elif note == 'Bb':
        return 'A#'
    elif note == 'B#':
        return 'C'
    elif note == 'Cb':
        return 'B'
    return note

def Abs2RelRoot(chord_root, tonic):
    chromatic = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    relative = ['I', 'I#', 'II', 'II#', 'III', 'IV', 'IV#', 'V', 'V#', 'VI', 'VI#', 'VII']

    tonic = GetEnharmonic(tonic)
    chord_root = GetEnharmonic(chord_root)

    tonic_pos = chromatic.index(tonic)
    chord_root_pos = chromatic.index(chord_root)

    dist = chord_root_pos - tonic_pos
    rel_chord_root = relative[dist]

    return rel_chord_root

def Abs2Rel(chord, tonic):
    splitted = chord.split(':')
    root = splitted[0]
    func = ''
    if len(splitted) > 1:
        func = ':' + splitted[1]
    rel_root = Abs2RelRoot(root, tonic)
    rel_chord = rel_root + func

    return rel_chord

def Rel2InCRoot(root_rel, tonic='C'):
    chromatic = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    relative = ['I', 'I#', 'II', 'II#', 'III', 'IV', 'IV#', 'V', 'V#', 'VI', 'VI#', 'VII']

    chromatic = chromatic[chromatic.index(tonic):] + chromatic[:chromatic.index(tonic)]
    root_inc = chromatic[relative.index(root_rel)]

    return root_inc

def Rel2InC(chord_rel, tonic='C'):
    splitted = chord_rel.split(':')
    root = splitted[0]
    func = ''
    if len(splitted) > 1:
        func = ':' + splitted[1]
    rel_root = Rel2InCRoot(root, tonic)
    rel_chord = rel_root + func

    return rel_chord