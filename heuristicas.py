import random
def h0(state):
    return random.randint(-100,100)
def h1(state):
    board = state.board
    return 1


def display(self, state):
    board = state.board
    for y in range(self.v, 0, -1):
        for x in range(1, self.h+1):
            print board.get((x, y), '.'),
        print
    print "-------------------"
    for n in range(1, self.h+1):
        print n,

def k_in_row(self, board, move, player, (delta_x, delta_y)):
    "Return true if there is a line through move on board for player."
    x, y = move
    n = 0 # n is number of moves in row
    while board.get((x, y)) == player:
        n += 1
        x, y = x + delta_x, y + delta_y
    x, y = move
    while board.get((x, y)) == player:
        n += 1
        x, y = x - delta_x, y - delta_y
    n -= 1 # Because we counted move itself twice
    return n >= self.k