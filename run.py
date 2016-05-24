import games
import heuristicas
#game = games.TicTacToe(h=3,v=3,k=3)

mod_game = raw_input("Pulsa 1 para jugar contra la maquina ,2 para jugar humano contra humano y 3 para ver jugar a la maquina: ")

if mod_game == '1':
    mod_dif= raw_input("Pulsa 1 para jugar dificultad dificil  ,2 para jugar dificultad media y 3 para jugar facil : ")
    select_player = raw_input("Pulse 1 para que empieze la maquina, pulse otro numero para que juege usted primero :")

    if select_player == '1':
        player = 'X'
        game = games.ConnectFour(player1=player)
        state = game.initial
    else:
        player = 'O'
        game = games.ConnectFour(player1=player)
        state = game.initial1


if mod_game == '3':
    mod_dif = raw_input("Pulsa 1 para maquina1 dificultad dificil  ,2 para maquina1 dificultad media y 3 para maquina1 facil : ")
    mod_dif2 = raw_input("Pulsa 1 para maquina2 dificultad dificil  ,2 para maquina2 dificultad media y 3 para maquina2 facil : ")




def maquina(state,player,dif):
    print "Thinking..."
    if dif == '1':
        move = games.alphabeta_search(state, game, d=5, eval_fn=heuristicas.h1,player=player)
        state = game.make_move(move, state)
    elif dif == '2':
        move = games.alphabeta_search(state, game, d=4, eval_fn=heuristicas.h1,player=player)
        state = game.make_move(move, state)
    else:
        move = games.alphabeta_search(state, game, eval_fn=heuristicas.h0,player=player)
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
            state=maquina(state,player,mod_dif)
            player = 'O'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break
if mod_game == '2':
    game = games.ConnectFour(jugador='X')
    state = game.initial
    player = 'X'
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
    game = games.ConnectFour(jugador='X')
    state = game.initial
    player = 'X'
    while True:
        print "Jugador a mover:", game.to_move(state)
        game.display(state)

        if player == 'O':
            state = maquina(state,player,mod_dif)
            player = 'X'
        else:
            state = maquina(state,player,mod_dif2)
            player = 'O'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break

if mod_game > '3':
    print "numero no valido"





