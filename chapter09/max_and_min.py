numbers = [ 5, 4, 10, 30, 22 ]
print(max(numbers))

strings = 's,t,r,i,n,g,S,T,R,I,N,G'
print(max(strings))

print(max(10, 300, 450, 50, 90))

numbers = [ 5, 4, 10, 30, 22 ]
print(min(numbers))

guess_this_number = 61
player_guesses = [ 12, 15, 70, 45 ]
if max(player_guesses) > guess_this_number:
    print('Boom! You all lose')
else:
    print('You win')