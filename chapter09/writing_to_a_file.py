f = open('myfile.txt', 'w')
f.write('What is green and loud? A froghorn!')
f.close()

f = open('myfile.txt')
print(f.read())