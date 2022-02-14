import os
import vlc

class Sample():

    def __init__(self, name):
        self.path = '../songs/' + name
        self.name = name
        self.comment = ""
        self.accept = False


def main():
    # Read in all the songs
    sample_names = os.listdir('../songs/')
    Samples = [Sample(x) for x in sample_names if '.wav' in x]
    accepted = []

    for sample in Samples:
        # Play the file
        track = vlc.MediaPlayer(sample.path)
        track.play()
        # Was it a good sample
        sample.accept = bool(input(f"Playing {sample.name}. Accept? "))

        if sample.accept:
            sample.comment = input("comment: ")
            accepted.append(sample)
            track.stop()
        else:
            track.stop()

    print("Done!!")

    with open("accepted.txt", "w+") as f:
        lines = [f"{a.name}, {a.comment}" for a in accepted]
        for line in lines:
            f.write(line + "\n")





if __name__ == "__main__":
    main()
