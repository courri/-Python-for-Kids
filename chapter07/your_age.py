def your_age():
    print('How old are you?')
    age = int(sys.stdin.readline())
    if age >= 10 and age <= 13:
        print('What is 13 + 49 + 84 + 155 + 97? A headache!')
    else:
        print('Huh?')
        
your_age()