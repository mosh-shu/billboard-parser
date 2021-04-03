# McGill Billboard Dataset Parser for chord extraction

This is a python project to parse the [billboard dataset](https://ddmal.music.mcgill.ca/research/The_McGill_Billboard_Project_(Chord_Analysis_Dataset)/) and export it to `.csv`.  
The main objective is to extract chord events and export them as `.csv` files.

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

- `parse.ipynb` is just for playing around and testing code, while the `.py` codes are there for execution.  
- The billboard dataset, should have files that are named `salami_chords.txt` under a four-digit directory, such as `0000` or `1297`.  
- Please run `main.py` with appropriate data path in order to complete conversion to `.csv`.  
The final `.csv` will be exported in to the same directory as the `salami_chords.txt`, under the name of `chords.csv`.