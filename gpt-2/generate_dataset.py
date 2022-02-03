import pandas as pd

def main():
    data = pd.read_csv('dataset/tcc_ceds_music.csv', header=0)

    lyrics = data['lyrics']
    lyrics.to_csv('dataset/lyrics.csv', index=False, header=False)


if __name__ == "__main__":
    main()
