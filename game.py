import random
import math

print('Welcome to candle game')
CELLS = 10
LIGHT_DECAY = 5
DIFFICULTY = 1

ITEMS  = {
    'c' : 5,
    't' : 5,
    'f' : 4,
    'd' : 2,
    'P' : 1,
    'T' : 1
}



def generateLevel():
    level = [['.'] * CELLS for _ in range(CELLS)]


    def distribute(item, quantity):
        print(f"distributing {quantity} {item}s")
        while quantity > 0:
            r, c = random.randint(0, CELLS - 1), random.randint(0, CELLS - 1)
            if level[r][c] == '.':
                level[r][c] = item
                quantity -= 1
        print('finished distribution')  
    for item in ITEMS:
        distribute(item, ITEMS[item])
    return level
    
def printLevel(level):
    for i, row in enumerate(level):
        print(f"  {' -  ' * len(level)}   ") if i != 0 else print(f"  {' =  ' * len(level)}   ")
        print(f"|| {' | '.join(row)} ||")
    print(' ', ' =  ' * len(level))



level = generateLevel()
printLevel(level)



