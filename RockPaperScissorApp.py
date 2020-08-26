import random as r

print('Welcome to the Rock, Paper, Scissors App')

rounds = int(input('How many rounds you want to play: '))
p_points = 0
c_points = 0
moves = ['rock', 'paper', 'scissors']
for i in range(1, rounds + 1):
    print(f'Round# {i}\nPlayer score:{p_points}\t\tComputer score: {c_points}')

    c_index = r.randint(0, 2)
    c_choice = moves[c_index]
    p_choice = input('Time to pick.. Rock, Paper or Scissors:').lower().strip()

    if p_choice in moves:
        print(f"Computer' choice: {c_choice}\t\tPlayer\'s choice: {p_choice}")
        if p_choice == c_choice:
            print('It is a tie, player and computer get no point. How boring..!')
        elif p_choice == 'paper' and c_choice == 'rock':
            p_points = +1
            print('Paper covers rock.Player gets a point.')
        elif p_choice == 'scissors' and c_choice == 'rock':
            c_points += 1
            print('Rock smashes the scissors.Computer gets a point.')
        elif p_choice == 'rock' and c_choice == 'paper':
            c_points = +1
            print('Paper covers rock.Computer gets a point.')
        elif p_choice == 'scissors' and c_choice == 'paper':
            p_points += 1
            print('Scissors cut paper.Player gets a point.')
        elif p_choice == 'rock' and c_choice == 'scissors':
            p_points = +1
            print('Rock smashes the scissors.Player gets a point.')
        elif p_choice == 'paper' and c_choice == 'scissors':
            c_points += 1
            print('Scissors cut paper.Computer gets a point.')

    else:
        print(' It is not a valid game option. Computer gets a point')
        c_points += 1

print(f"Game ends.Final scores are as follows:\nPlayer's score:{p_points}\tComputer's score:{c_points}")
if p_points > c_points:
    print('Winner: Player')
elif c_points > p_points:
    print('Winner: Computer')
else:
    print('No winner: The game was a tie.')
