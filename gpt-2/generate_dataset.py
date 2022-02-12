import pandas as pd

def main():
    # dataset_1()
    dataset_2()

def dataset_1():
    data = pd.read_csv('dataset/tcc_ceds_music.csv', header=0)

    lyrics = data['lyrics']
    lyrics.to_csv('dataset/lyrics_1.csv', index=False, header=False)

def dataset_2():
    data = pd.read_csv('dataset/Songs.csv', header=0)

    lyrics = data['Lyrics']
    lyrics.to_csv('dataset/lyrics_2.csv', index=False, header=False)


if __name__ == "__main__":
    main()
