import re
import util

"""
this module is a set of functions to parse salami_chords.txt and extract chords
"""

def ExtractFile(filepath):
    f = open(filepath, 'r')
    raw = f.readlines()
    f.close
    return raw

def ExtractMeta(raw):
    title = re.split('# title: |\n', raw[0])[1]
    artist = re.split('# artist: |\n', raw[1])[1]
    metre = re.split('# metre: |\n', raw[2])[1]
    tonic = re.split('# tonic: |\n', raw[3])[1]

    return (title, artist, metre, tonic)

def ExtractPhrases(raw):
    raw = raw[6:-2]
    phrases = list()
    for row in raw:
        splitted = re.split('\t', row)[1:][0]
        splitted = re.split('\|', splitted)[1:]
        
        if not splitted: continue
        
        phrase = splitted[:-1]

        # check for repeat
        if util.IsRepeat(splitted[-1][1:3]):
            phrase.append(splitted[-1][1:3])

        phrases.append(phrase)
    return phrases

def CleanPhrases(phrases):
    phrases_clean = list()
    for phrase in phrases:
        phrase_clean = [chord.strip() for chord in phrase]
        phrases_clean.append(phrase_clean)
    return phrases_clean
    
def FormatChords(phrases_clean):
    chords = list()
    
    for phrase in phrases_clean:
        # clean non-chords
        phrase_chord = [util.RemoveNoise(chord) for chord in phrase]
        
        # remove blank (noise-only) lines
        if all([not p for p in phrase_chord]): continue

        # check for repeat
        if util.IsRepeat(phrase_chord[-1]):
            repeated = phrase_chord[:-1]
            n_repeat = int(phrase_chord[-1][-1])
            phrase_chord = repeated*n_repeat

        chords.append(phrase_chord)
    # flatten 2d list
    chords = sum(chords, [])

    # split chords into bars
    chords = [chord.split() for chord in chords]

    return chords

def CreateIndex(chords):
    indexs_bar = list()
    for i, bar in enumerate(chords):
        index_bar = [i]*len(bar)
        indexs_bar.append(index_bar)
    return indexs_bar
