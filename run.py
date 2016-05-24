import games
import heuristica
#game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour()

state = game.initial
mod_game = raw_input("Pulsa 1 para jugar contra la maquina ,2 para jugar humano contra humano y 3 para ver jugar a la maquina: ")

if mod_game == '1':
    mod_dif= raw_input("Pulsa 1 para jugar dificultad dificil  ,2 para jugar dificultad media y 3 para jugar facil : ")


player = 'X'

def maquina(state):
    print "Thinking..."
    # move = games.minimax_decision(state, game)
    # move = games.alphabeta_full_search(state, game)

    if mod_game == '1':
        if mod_dif == '3':
            move = games.alphabeta_search(state, game, eval_fn=heuristica.final)
            state = game.make_move(move, state)
        if mod_dif == '2':
            move = games.alphabeta_search(state, game, eval_fn=heuristica.final)
            state = game.make_move(move, state)
        else:
            move = games.alphabeta_search(state, game, eval_fn=heuristica.final)
            state = game.make_move(move, state)
    return state
def humano(state):
    col_str = raw_input("Movimiento: ")
    coor = int(str(col_str).strip())
    x = coor
    y = -1
    legal_moves = game.legal_moves(state)
    for lm in legal_moves:
        if lm[0] == x:
            y = lm[1]

    state = game.make_move((x, y), state)
    return state



if mod_game == '1':
    while True:
        print "Jugador a mover:", game.to_move(state)
        game.display(state)

        if player == 'O':
            state=humano(state)
            player = 'X'
        else:
            state=maquina(state)
            player = 'O'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break
if mod_game == '2':
    while True:
         print "Jugador a mover:", game.to_move(state)
         game.display(state)

         if player == 'O':
           state = humano(state)
           player = 'X'
         else:
             state = humano(state)
             player = 'O'
             print "-------------------"
         if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break

if mod_game == '3':
    while True:
        print "Jugador a mover:", game.to_move(state)
        game.display(state)

        if player == 'O':
            state = maquina(state)
            player = 'X'
        else:
            state = maquina(state)
            player = 'O'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break

if mod_game > '3':
    print "numero no valido"






'''
player = 'X'
if mod_game == '1':
    while True:
        print "Jugador a mover:", game.to_move(state)
        game.display(state)

        if player == 'O':
            col_str = raw_input("Movimiento: ")
            coor = int(str(col_str).strip())
            x = coor
            y = -1
            legal_moves = game.legal_moves(state)
            for lm in legal_moves:
                if lm[0] == x:
                    y = lm[1]

            state = game.make_move((x, y), state)
            player = 'X'
        else:
            print "Thinking..."
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)
            move = games.alphabeta_search(state, game, eval_fn=heuristica.final)

            state = game.make_move(move, state)
            player = 'O'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break
else:
    if mod_game == '2':
        while True:
            print "Jugador a mover:", game.to_move(state)
            game.display(state)
            col_str = raw_input("Movimiento: ")
            coor = int(str(col_str).strip())
            x = coor
            y = -1
            legal_moves = game.legal_moves(state)
            for lm in legal_moves:
                if lm[0] == x:
                    y = lm[1]

            state = game.make_move((x, y), state)
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
            print "-------------------"
            if game.terminal_test(state):
                game.display(state)
                print "Final de la partida"
                break
    else:
        if mod_game == '3':
            while True:
                print "Jugador a mover:", game.to_move(state)
                game.display(state)


                print "Thinking..."
                # move = games.minimax_decision(state, game)
                # move = games.alphabeta_full_search(state, game)
                move = games.alphabeta_search(state, game, eval_fn=heuristica.final)

                state = game.make_move(move, state)
                player = 'O'
                print "-------------------"
                if game.terminal_test(state):
                    game.display(state)
                    print "Final de la partida"
                    break
        else:
            print "numero no valido"

'''