import pandas as pd
import numpy as np
import glob
import parsetxt, converter

datadir = "../data/McGill-Billboard/"
filepaths = glob.glob(datadir+'[0-9][0-9][0-9][0-9]/salami_chords.txt')

for i, filepath in enumerate(filepaths):
  if i%1==0: print("{}/{} th file is processed".format(i, len(filepaths)))
  print(filepath)

  csvpath = '/'.join(filepath.split('/')[:-1]) + '/chords.csv'

  raw = parsetxt.ExtractFile(filepath)
  (title, artist, metre, tonic) = parsetxt.ExtractMeta(raw)

  phrases = parsetxt.ExtractPhrases(raw)
  phrases_clean = parsetxt.CleanPhrases(phrases)
  chords = parsetxt.FormatChords(phrases_clean)

  chords_index = parsetxt.CreateIndex(chords)

  df_chords = pd.DataFrame()
  df_chords['bar'] = sum(chords_index, [])
  df_chords['chords'] = sum(chords, [])
  df_chords['chords_basic'] = df_chords['chords'].apply(converter.Raw2Basic)
  df_chords['chords_root'] = df_chords['chords'].apply(converter.Raw2Root)

  df_chords['chords_rel'] = df_chords['chords'].apply(converter.Abs2Rel, tonic=tonic)
  df_chords['chords_basic_rel'] = df_chords['chords_basic'].apply(converter.Abs2Rel, tonic=tonic)
  df_chords['chords_root_rel'] = df_chords['chords_root'].apply(converter.Abs2Rel, tonic=tonic)

  df_chords['chords_inC'] = df_chords['chords_rel'].apply(converter.Rel2InC)
  df_chords['chords_basic_inC'] = df_chords['chords_basic_rel'].apply(converter.Rel2InC)
  df_chords['chords_root_inC'] = df_chords['chords_root_rel'].apply(converter.Rel2InC)

  df_chords['meta'] = ['title: '+title, 'artist: '+artist, 'metre: '+metre, 'tonic: '+tonic] + [np.nan] * (len(df_chords)-4)

  df_chords.to_csv(csvpath, index=False)