import random

def generateLevel(n, items):
    level = [['.'] * n for _ in range(n)]


    def distribute(item, quantity):
        print(f"distributing {quantity} {item}s")
        while quantity > 0:
            r, c = random.randint(0, n - 1), random.randint(0, n - 1)
            if level[r][c] == '.':
                level[r][c] = item
                quantity -= 1
        print('finished distribution')  

    for item in items:
        distribute(item, items[item])
    
    return level

    
def printLevel(level, p_x, p_y, l_d):
    for i, row in enumerate(level):
        print(f"  {' -  ' * len(level)}   ") if i != 0 else print(f"  {' =  ' * len(level)}   ")
        player_view = []
        for j, char in enumerate(row):
            if abs(i - p_y) <= l_d and abs(j - p_x) <= l_d:
                player_view.append(char)
            else:
                player_view.append(' ')
        print(f"|| {' | '.join(player_view)} ||")
    print(' ', ' =  ' * len(level))


def playerMoveTo(level, x, y, stats):
    if 0 <= x < len(level) and 0 <= y < len(level):
        if level[y][x] == '.':
            level[player_y][player_x] = '.'
            level[y][x] = 'P'
            return True
        elif level[y][x] == 'c':
            level[player_y][player_x] = '.'
            level[y][x] = 'P'
            stats['coins'] += 1
            return True
        else:
            return False
        
    else:
        return False


def locateCharacter(level, c):
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == c:
                return [i, j]
        


def main():
    print('Welcome to candle game')
    CELLS = 10
    LIGHT_DECAY = 1
    DIFFICULTY = 1

    global player_x
    global player_y

    PLAYER_STATS = {
        'coins' : 0,
        'attack': 1,
        'def'   : 1,
        'health': 5,
        'level' : 0
    }


    ITEMS  = {
        'c' : 5,
        't' : 5,
        '+' : 1,
        'P' : 1,
        's' : 1
    }


    level = generateLevel(CELLS, ITEMS)
    player_y, player_x = locateCharacter(level, 'P')

    while True:
        printLevel(level, player_x, player_y, LIGHT_DECAY)
        print(PLAYER_STATS)
        player_move = input('enter a move: ')
        match player_move:
            case 'w':
                if level[player_y - 1][player_x] == '+':
                    level = generateLevel(CELLS, ITEMS)
                    player_y, player_x = locateCharacter(level, 'P')
                    PLAYER_STATS['level'] += 1
                elif playerMoveTo(level, player_x, player_y - 1, PLAYER_STATS):
                    player_y -= 1
            case 'a':
                if level[player_y][player_x - 1] == '+':
                    level = generateLevel(CELLS, ITEMS)
                    player_y, player_x = locateCharacter(level, 'P')
                    PLAYER_STATS['level'] += 1
                elif playerMoveTo(level, player_x - 1, player_y, PLAYER_STATS):
                    player_x -= 1
            case 's':
                if level[player_y + 1][player_x] == '+':
                    level = generateLevel(CELLS, ITEMS)
                    player_y, player_x = locateCharacter(level, 'P')
                    PLAYER_STATS['level'] += 1
                elif playerMoveTo(level, player_x, player_y + 1, PLAYER_STATS):
                    player_y += 1
            case 'd':
                if level[player_y][player_x + 1] == '+':
                    player_y, player_x = locateCharacter(level, 'P')
                    level = generateLevel(CELLS, ITEMS)
                    PLAYER_STATS['level'] += 1

                    player_x += 1
            case _:
                player_move = input('please enter a valid move')


main()


