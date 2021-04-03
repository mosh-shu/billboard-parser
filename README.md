# Billboard Parser

This is a python project to parse the billboard dataset and export it to `.csv`.

The output `.csv` file should look like
1st col: bar number
2nd col: chord name
3rd col: chord name (basic): excludes tension chords and on-chords i.e.) maj, min, sus2, sus4, 15 (root only or power chord)
4th col: chord name (root)
5th col: chord number relative to the tonic
6th col: chord number (basic) relative to the tonic
7th col: chord number (root) relative to the tonic
8th col: chord number in C
9th col: chord number (basic) in C
10th col: chord number (root) in C
11th col: meta-info: title, artist, tonic, metre