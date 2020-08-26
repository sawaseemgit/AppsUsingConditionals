import random as r

print('Welcome to Coin Toss App.\nA coin will be flipped a set number of times.')
flips = int(input("Enter the number of times the coin will be flipped:"))
choice = input('Would you like to see the result of each flip? (y/n): ').lower()

print('Flipping the coin now:')
heads = 0
tails = 0
for flip in range(flips):
    side = r.randint(0, 1)
    if side == 1:
        heads += 1
        if choice.startswith('y'):
            print('Heads')
    else:
        tails += 1
        if choice.startswith('y'):
            print('Tails')
    if heads == tails:
        print(f'At {flip + 1} flips, number of heads and tails were equal at {heads}')
heads_per = round(100 * heads / flips, 2)
tails_per = round(100 * tails / flips, 2)
print(f'Results of FLipping a coin {flips} times:\nSide\tCount\tPercentage')
print(f'Heads\t{heads}\t{heads_per}')
print(f'Tails\t{tails}\t{tails_per}')
