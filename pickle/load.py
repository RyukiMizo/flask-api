import pickle

with open("singer.pickle", "rb") as f:
    singer = pickle.load(f)

singer.sing()