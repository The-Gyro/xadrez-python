board = [
["r","n","b","q","k","b","n","r"],
["p","p","p","p","p","p","p","p"],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],
["P","P","P","P","P","P","P","P"],
["R","N","B","Q","K","B","N","R"]
]

turno = "brancas"


def mostrar_tabuleiro():
    for i, linha in enumerate(board):
        print(8-i, *linha)

    print("  a b c d e f g h")


def converter(pos):
    coluna = ord(pos[0]) - 97
    linha = 8 - int(pos[1])

    return linha, coluna


while True:

    mostrar_tabuleiro()

    print("Turno:", turno)

    jogada = input("Digite jogada (ex: e2 e4) ou sair: ")

    if jogada.lower() == "sair":
        break

    try:
        origem, destino = jogada.split()
    except:
        print("Formato inválido.")
        continue


    l1,c1 = converter(origem)
    l2,c2 = converter(destino)

    peca = board[l1][c1]

    if peca==".":
        print("inválido.")
        continue


    # impedir capturar peça do mesmo lado
    destino_peca = board[l2][c2]

    if destino_peca != ".":

        if peca.isupper() and destino_peca.isupper():
            print("Você não pode capturar sua própria peça.")
            continue

        if peca.islower() and destino_peca.islower():
            print("Você não pode capturar sua própria peça.")
            continue


    # controle turnos
    if turno=="brancas" and not peca.isupper():
        print("É turno das brancas.")
        continue

    if turno=="pretas" and not peca.islower():
        print("É turno das pretas.")
        continue


    # peões brancos
    if peca=="P":

        if l2==l1-1 and c1==c2:
            pass

        elif l1==6 and l2==4 and c1==c2:
            pass

        else:
            print("Movimento inválido.")
            continue


    # peões pretos
    if peca=="p":

        if l2==l1+1 and c1==c2:
            pass

        elif l1==1 and l2==3 and c1==c2:
            pass

        else:
            print("Movimento inválido.")
            continue


    # cavalos
    if peca in ["N","n"]:

        dl = abs(l2-l1)
        dc = abs(c2-c1)

        if not ((dl==2 and dc==1) or (dl==1 and dc==2)):
            print("Movimento inválido para cavalo.")
            continue


    # mover peça
    board[l2][c2] = peca
    board[l1][c1] = "."


    # trocar turno
    if turno=="brancas":
        turno="pretas"
    else:
        turno="brancas"