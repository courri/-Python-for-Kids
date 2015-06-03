import pickle
f = open('favorites.dat', 'rb')
favorites = pickle.load(f)
print(favorites)