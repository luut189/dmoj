current = 1
move = None
quit = False

while current < 100 and not quit:
    move = int(input())
    if move == 0:
        quit = True
    elif current + move > 100:
        print("You are now on square", current)
    else:
        current += move
        
        #Ladder
        if current == 9: current = 34
        if current == 40: current = 64
        if current == 67: current = 86
        
        #Snake
        if current == 54: current = 19
        if current == 90: current = 48
        if current == 99: current = 77

        #Print status
        print("You are now on square", current)


if current == 100:
    print("You Win!")
elif quit:
    print("You Quit!")
