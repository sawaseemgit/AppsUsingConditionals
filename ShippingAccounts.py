print('Welcome to the Shipping Accounts Program')
users = ['ramon', 'ann', 'bob', 'allen']
name = input('What is your username:').lower().strip()
if name in users:
    print(f'Hello {name}. Welcome back to your account.\nCurrent shipping prices are'
          f' as follows:\n')
    print('Shipping orders 0 to 100:\t$5.10 each')
    print('Shipping orders 101 to 500:\t$5.00 each')
    print('Shipping orders 501 to 1000:\t$4.95 each')
    print('Shipping orders over 1000 :\t$4.80 each')

    quantity = int(input('How many items would you like to ship: '))
    if quantity < 100:
        cost = 5.10
    elif quantity < 500:
        cost = 5.00
    elif quantity < 1000:
        cost = 4.95
    else:
        cost = 4.80
    bill = round((quantity * cost), 2)
    print(f'To ship {quantity} items, it will cost you ${bill} at {cost} per item')
    confirm = input('Would you like to place this order (y/n):').lower().strip()
    if confirm.startswith('y'):
        print(f'Ok. Shipping your {quantity} items.')
    else:
        print('Ok,  No items will be shipped.')

else:
    print('Sorry, you do not have an account with us. Goodbye.')
