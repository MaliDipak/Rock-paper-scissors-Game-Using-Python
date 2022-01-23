# Rock Paper Scissors Game

import random


def result(com, ply):
    if com == ply:
        return 0
    elif com == 'p' and ply == 'r':
        return 1
    elif com == 'p' and ply == 's':
        return 2
    elif com == 'r' and ply == 'p':
        return 2
    elif com == 'r' and ply == 's':
        return 1
    elif com == 's' and ply == 'r':
        return 2
    elif com == 's' and ply == 'p':
        return 1
    else:
        return 3


num = random.randint(1, 30)

if num >= 1 and num <= 10:
    com = 'r'
elif num >= 11 and num <= 20:
    com = 'p'
elif num >= 21 and num <= 30:
    com = 's'

print('\nRock_Paper_Scissor Game :)\nChoose your choice,\n[r]Rock\n[p]Paper\n[s]Scissor')
print('Computer = *')
ply = input('Player   = ')

res = result(com, ply)

if com == 'r':
    com = 'Rock'
elif com == 'p':
    com = 'Paper'
else:
    com = 'Scissor'

if ply == 'r':
    ply = 'Rock'
elif ply == 'p':
    ply = 'Paper'
elif ply == 's':
    ply = 'Scissor'

if res == 0:
    print(f'Computer = {com} and You = {ply} : Game_Draw!')
elif res == 1:
    print(f'Computer = {com} and You = {ply} : Computer_Win!')
elif res == 2:
    print(f'Computer = {com} and You = {ply} : You_Win!')
else:
    print(f'Computer = {com} and You = {ply} : Enter Valid Choice...')
print('')
input("Press enter.......")