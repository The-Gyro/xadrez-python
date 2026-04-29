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

turno="brancas"


def mostrar_tabuleiro():
    for i,linha in enumerate(board):
        print(8-i,*linha)
    print("  a b c d e f g h")


def converter(pos):
    c=ord(pos[0])-97
    l=8-int(pos[1])
    return l,c


def caminho_livre_torre(l1,c1,l2,c2):

    if l1==l2:
        passo=1 if c2>c1 else -1

        for c in range(c1+passo,c2,passo):
            if board[l1][c]!=".":
                return False
        return True


    if c1==c2:
        passo=1 if l2>l1 else -1

        for l in range(l1+passo,l2,passo):
            if board[l][c1]!=".":
                return False
        return True

    return False



def caminho_livre_bispo(l1,c1,l2,c2):

    # precisa ser diagonal
    if abs(l2-l1) != abs(c2-c1):
        return False

    passos = abs(l2-l1)

    dir_l = 1 if l2 > l1 else -1
    dir_c = 1 if c2 > c1 else -1

    # verifica TODAS as casas entre origem e destino
    for i in range(1, passos):

        l = l1 + i*dir_l
        c = c1 + i*dir_c

        if board[l][c] != ".":
            return False

    return True



while True:

    mostrar_tabuleiro()
    print("Turno:",turno)

    jogada=input("Digite jogada ou sair: ")

    if jogada.lower()=="sair":
        break

    origem,destino=jogada.split()

    l1,c1=converter(origem)
    l2,c2=converter(destino)

    peca=board[l1][c1]

    if peca==".":
        print("Sem peça.")
        continue


    destino_peca=board[l2][c2]

    if destino_peca!=".":

        if peca.isupper() and destino_peca.isupper():
            print("Peça própria bloqueando.")
            continue

        if peca.islower() and destino_peca.islower():
            print("Peça própria bloqueando.")
            continue


    if turno=="brancas" and not peca.isupper():
        print("Turno das brancas.")
        continue

    if turno=="pretas" and not peca.islower():
        print("Turno das pretas.")
        continue


    if peca=="P":

        if not(
            (l2==l1-1 and c1==c2)
            or
            (l1==6 and l2==4 and c1==c2)
        ):
            print("Movimento inválido.")
            continue


    if peca=="p":

        if not(
            (l2==l1+1 and c1==c2)
            or
            (l1==1 and l2==3 and c1==c2)
        ):
            print("Movimento inválido.")
            continue


    if peca in ["N","n"]:

        dl=abs(l2-l1)
        dc=abs(c2-c1)

        if not((dl==2 and dc==1) or (dl==1 and dc==2)):
            print("Movimento inválido.")
            continue


    if peca in ["R","r"]:

        if not caminho_livre_torre(l1,c1,l2,c2):
            print("Movimento inválido.")
            continue


    if peca in ["B","b"]:

        if not caminho_livre_bispo(l1,c1,l2,c2):
            print("Movimento inválido.")
            continue


    board[l2][c2]=peca
    board[l1][c1]="."


    if turno=="brancas":
        turno="pretas"
    else:
        turno="brancas"