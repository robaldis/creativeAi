import random

def main(corpus):
    words = corpus.split(" ")
    trans = dict()

    for i in range(len(words)-1):
        if words[i] not in trans:
            trans[words[i]] = []
        trans[words[i]].append(words[i+1])

    return trans


def predict(model, length=10):
    s = random.choice(list(model.keys()))
    output = ""
    for i in range(length):
        if s not in model:
            break
        s = random.choice(model[s])
        output = output + " " + s

    return output


if __name__ == "__main__":
    sent = "the dog went up the tree"


    with open("input.txt", "r") as f:
        sent = f.read()
        sent = sent.replace("\n", " ")
        sent = sent.lower()

    print(main(sent))
    model = main(sent)
    print(predict(model, 50))
