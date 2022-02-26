# Creative AI




## Lyric

- [[http://www.mldb.org/song-248319-someone-like-you.html| A lot of songs, more work]]
- [[https://www.kaggle.com/paultimothymooney/poetry|49 songs]]
- [[https://www.kaggle.com/karnikakapoor/lyrics|745 lyrics]]
- [[https://www.kaggle.com/neisse/scrapped-lyrics-from-6-genres?select=lyrics-data.csv|164,790 lyrics]]
- [[http://millionsongdataset.com/pages/getting-dataset/|300gb, no lyrics]]
- [[https://data.mendeley.com/datasets/3t9vbwxgr5/2|~28,000]] (done)
- Manually collect artists I like



## Tuning GPT-2

Download the master branch and try run the "/examples/tensorflow/language-modeling/run_clm.py" with all the options



# Creating music

- Generate lyrics (gpt-2)
- Generate music (musicVAE)
- Extract melody (extractMelody)
- Sing (DiffSinger)


# Running each module

gpt-2:

open main.py and change the starting prompt
run "python main.py"


musicVAE:

run "node 5_save_latent_vector.js"
run "./node_modules/http-server/bin/http-server ."
Change the chords in "6_load_latent_space.js"
run "node 6_load_latent_space.js"
run "midi_to_wav.sh"


Melody extraction:

run "python midi_analyser.py" to get the instrament breakdown and select the 
instrament the singer should sing along with
go into midi_note_extractor.py and change the channel from the above program
run "python midi_note_extractor.py"
run "python midi_duration.py"



diffSinger:

conda activate diffSinger
run "python sing.py --lyrics "<LYRICS>" --notes <NOTES> --dur <DURATION>
