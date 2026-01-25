import random

options = ("batu", "gunting", "kertas")
playing = True

while playing:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input('Enter a choice (batu, gunting, kertas): ')

        print(f'player: {player}')
        print(f'computer: {computer}')

        if player == computer:
            print("It's a tie!")
        elif player == 'batu' and computer == 'gunting':
            print('You Win!')
        elif player == 'kertas' and computer == 'batu':
            print('You Win!')
        elif player == 'gunting' and computer == 'kertas':
            print('You Win!')
        else:
            print('You Lose!')
        
        if not input('play again? [y/n]: ').lower() == 'y':
            playing = False
            
print('Thanks for playing')
