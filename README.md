# FSI-prac1
Conecta 4
Esta práctica ha sido realizada por mi compañero Carlos Lorenzos Campos Rodríguez y por mi (Axel Cabrera Rodríguez).
En ella hemos modificado el código aportado por el rpfesor Cayetano Guerra Artal, para que por un lado permita tanto el juego
humano contra máquina, el juego humano contra humano y la competición entre máquinas. Aparte de ello hemos añadido una serie de
heurísticas para permitir la implementación de un algoritmo minimax. Una de ellas la h0 añadida en clase es muy simple y solo 
devuelve un valor aletorio entre -100 y 100, además tenemos la h1 que es una heurísica más compleja que busca en las posiciones
disponibles para jugar (legales), por filas, columnas y diagonales. Sumando las posiciones ocupadas por las piezas de nuestro
jugador como más 5 y los vacios con más 0.5 (se valorará 0 si no hay opción de tres e raya). Además si el programa hubiese
computado que el último movimiento es terminal, al iniciar la heurística su cálculo devolverá infinito si nos es faavorable
y - inifinito si no lo es (se toma por inifinito el valor infinity suministrado en el archivo utils.py que es igual a 1.0e400).
