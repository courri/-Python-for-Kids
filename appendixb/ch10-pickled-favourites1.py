import pickle
favorites = [ 'PlayStation', 'Fudge', 'Movies', 'Python for Kids' ]
f = open('favorites.dat', 'wb')
pickle.dump(favorites, f)
f.close()