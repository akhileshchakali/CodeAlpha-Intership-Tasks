import random

levels=['''
    +---+
    |   |
    0   |
   /|\\  |
   / \\  |
        |
---------
''',
'''
    +---+
    |   |
    0   |
   /|\\  |
   /    |
        |
---------
''',
'''
    +---+
    |   |
    0   |
   /|\\  |
        |
        |
---------
''',
'''
    +---+
    |   |
    0   |
   /|   |
        |
        |
---------
''',
'''
    +---+
    |   |
    0   |
   /    |
        |
        |
---------
''',
'''
    +---+
    |   |
    0   |
        |
        |
        |
---------
'''
]

print('\tHangman Game')
print('******************************')
print('Guess Country Name')
print('\n')
names=['india','america','bangladesh','nepal','pakistan','china','russia','ukraine','london','dubai','england','germany']
word=random.choice(names)
c=6
dashed_lines=['_']*len(word)
print(*dashed_lines)
                            
while True:
    guess=input('Enter a word :').lower()
                            
    if guess not in word:
        c-=1
        print(levels[c])
        if c==0:
            print('You Lose!😢')
            print(f'correct Word is : {word}')
            break
    else:
        for i in range(len(word)):
            if word[i]==guess:
                dashed_lines[i]=guess
    print(*dashed_lines)
    print('\n\n')
                                

    if '_' not in dashed_lines:
        print('🎉👏You Win!🎉👏')
        break
