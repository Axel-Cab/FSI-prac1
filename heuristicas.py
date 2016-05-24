import random
import utils


def memoize(f):
    memo = {}

    def helper(state, player):
        iden = hash(frozenset(state.board.items()))
        if iden not in memo:
            memo[iden] = f(state, player)
        return memo[iden]
    return helper


def h0(state, player):
    return random.randint(-100, 100)


@memoize
def h1(state, player, h=7, v=6, k=4):
    if player == 'X':
        enemy = 'O'
    else:
        enemy = 'X'

    if state.utility != 0:
        if player == 'X':
            return utils.infinity * state.utility
        return -(utils.infinity * state.utility)

    legal = legal_moves(state)
    board = state.board.copy()
    computed = 0
    for move in legal:
        computed += compute_utility(move, player, board, (h, v, k))
        computed -= compute_utility(move, enemy, board, (h, v, k))
    return computed


def compute_utility(move, player, board, (h, v, k)):
    acum = k_in_row(board, move, player, (0, 1), (h, v, k))
    acum += k_in_row(board, move, player, (1, 0), (h, v, k))
    acum += k_in_row(board, move, player, (1, -1), (h, v, k))
    acum += k_in_row(board, move, player, (1, 1), (h, v, k))
    return acum


def k_in_row(board, move, player, (delta_x, delta_y), (h, v, k)):
    if player == 'X':
        enemy = 'O'
    else:
        enemy = 'X'
    pos = 0
    computed = 0

    t_pos, t_computed = count(board, (delta_x, delta_y), player, enemy, move, (h, v))
    pos += t_pos
    computed += t_computed

    t_pos, t_computed = count(board, (-delta_x, -delta_y), player, enemy, move, (h, v))
    pos += t_pos
    computed += t_computed

    if pos-1 < k:
        return 0

    return computed-1


def count(board, (delta_x, delta_y), player, enemy, move, (h, v)):
    computed = 0
    pos = 0
    x, y = move
    while board.get((x, y)) != enemy:
        if not (0 < x <= h) or not (0 < y <= v):
            break
        if board.get((x, y)) == player:
            computed += 5
        else:
            computed += 0.5
        x, y = x + delta_x, y + delta_y
        pos += 1
    return pos, computed


def legal_moves(state):
    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]
