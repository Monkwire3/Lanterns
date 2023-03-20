import random
import math

print('Welcome to candle game')
CELLS = 10
LIGHT_DECAY = 5
DIFFICULTY = 1

ITEMS  = {
    'c' : 5,
    't' : 5,
    'f' : 4
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
    print('   ', ' = ' * 2 * len(level))
    for row in level:
        print(f"  {' -  ' * len(level)}   ")
        print(f"|| {' | '.join(row)} ||")
    print('   ', ' = ' * 2 * len(level))



level = generateLevel()
printLevel(level)



