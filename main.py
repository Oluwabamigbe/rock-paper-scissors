import random

gameList = ['R', 'P', 'S']

user = str(input('Enter your name: ')).upper()

userInput = input('Pick an OPTION between "R", "P" or "S" : ').upper()

cpuInput = random.choice(gameList)

def rps(userInput, cpuInput):
    print('Player: ' + userInput + ' CPU: ' + cpuInput)

    if userInput in gameList:
        if userInput=='R' and cpuInput == 'S':
            print(user + ' wins')
        elif userInput=='P' and cpuInput == 'R':
            print(user + ' wins')
        elif userInput=='S' and cpuInput == 'P':
            print(user + ' wins')
        elif userInput=='S' and cpuInput == 'R':
            print('CPU wins')
        elif userInput=='R' and cpuInput == 'P': 
            print('CPU wins')
        elif userInput=='P' and cpuInput == 'S':
            print('CPU wins')
    else:
        print ('ERROR: TRY INPUTING ONE OF THE LISTED OPTIONS')
        userInput = input('Enter choice again: ')
        rps(userInput, cpuInput)
        

    if(userInput==cpuInput):
        print('RESTART THE GAME')
        input('You both chose the same thing, pick again: ')
        rps(userInput, cpuInput)

rps(userInput, cpuInput)
