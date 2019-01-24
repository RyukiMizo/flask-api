import pickle
from Singer import Singer

singer = Singer("AAA")

with open("singer.pickle", "wb") as f:
    pickle.dump(singer, f)