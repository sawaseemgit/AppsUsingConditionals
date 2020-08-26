print('Welcome to the Voter Registration App')
name = input('Please enter your name: ').title().strip()
age = int(input('Enter your age: '))

parties = ['Republican', 'Democratic', 'Independent', 'Green']
if age > 17:
    print('Great. Here is a list of parties to join:')
    for p in parties:
        print(f'\t-{p}')
    party = input('\nWhat party would you like to join:').title().strip()

    if party in parties:
        print(f'Congrats {name}. You have joined the {party} party.')
        if party == 'Republican' or party == 'Democratic':
            print('That is a major party..!')
        elif party == 'Independent':
            print('You are an independent person..!')
        else:
            print('That is not a major party though..!!')

else:
    print(f'Sorry {name}, you are too young to vote. You need to wait {18 - age} '
          f'years more to become eligible to vote.')
