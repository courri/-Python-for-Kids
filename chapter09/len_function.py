len('this is a test string')

creature_list = [ 'unicorn', 'cyclops', 'fairy', 'elf', 'dragon', 'troll' ]
print(len(creature_list))

enemies_map = { 'Batman' : 'Joker', 'Superman' : 'Lex Luther', 'Spiderman' : 'Green Goblin' }
print(len(enemies_map))

fruit = [ 'apple', 'banana', 'clementine', 'dragon fruit' ]
length = len(fruit)
for x in range(0, length):
    print('the item at index %s is %s' % (x, fruit[x]))