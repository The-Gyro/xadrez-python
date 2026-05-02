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

# flags para roque
rei_branco_moveu=False
rei_preto_moveu=False

torre_a1_moveu=False
torre_h1_moveu=False

torre_a8_moveu=False
torre_h8_moveu=False


def mostrar_tabuleiro():
    for i,linha in enumerate(board):
        print(8-i,*linha)
    print("  a b c d e f g h")


def coordenada_valida(pos):
    if len(pos)!=2:
        return False
    if pos[0] not in "abcdefgh":
        return False
    if pos[1] not in "12345678":
        return False
    return True


def converter(pos):
    c=ord(pos[0])-97
    l=8-int(pos[1])
    return l,c


def caminho_livre_torre(l1,c1,l2,c2):

    if l1==l2:

        passo=1 if c2>c1 else -1

        for c in range(
            c1+passo,
            c2,
            passo
        ):
            if board[l1][c]!=".":
                return False

        return True


    if c1==c2:

        passo=1 if l2>l1 else -1

        for l in range(
            l1+passo,
            l2,
            passo
        ):
            if board[l][c1]!=".":
                return False

        return True


    return False



def caminho_livre_bispo(
    l1,c1,l2,c2
):

    if abs(l2-l1)!=abs(c2-c1):
        return False


    passos=abs(l2-l1)

    dir_l=1 if l2>l1 else -1
    dir_c=1 if c2>c1 else -1


    for i in range(
        1,
        passos
    ):

        l=l1+i*dir_l
        c=c1+i*dir_c

        if board[l][c]!=".":
            return False

    return True



def roque_valido(
    peca,l1,c1,l2,c2
):

    global rei_branco_moveu
    global rei_preto_moveu

    global torre_a1_moveu
    global torre_h1_moveu
    global torre_a8_moveu
    global torre_h8_moveu


    if (
        peca=="K"
        and (l1,c1)==(7,4)
        and (l2,c2)==(7,6)
    ):

        if rei_branco_moveu:
            return False

        if torre_h1_moveu:
            return False

        if board[7][5]!=".":
            return False

        if board[7][6]!=".":
            return False

        return True



    if (
        peca=="K"
        and (l1,c1)==(7,4)
        and (l2,c2)==(7,2)
    ):

        if rei_branco_moveu:
            return False

        if torre_a1_moveu:
            return False

        if (
            board[7][1]!="."
            or board[7][2]!="."
            or board[7][3]!="."
        ):
            return False

        return True



    if (
        peca=="k"
        and (l1,c1)==(0,4)
        and (l2,c2)==(0,6)
    ):

        if rei_preto_moveu:
            return False

        if torre_h8_moveu:
            return False

        if (
            board[0][5]!="."
            or board[0][6]!="."
        ):
            return False

        return True



    if (
        peca=="k"
        and (l1,c1)==(0,4)
        and (l2,c2)==(0,2)
    ):

        if rei_preto_moveu:
            return False

        if torre_a8_moveu:
            return False

        if (
            board[0][1]!="."
            or board[0][2]!="."
            or board[0][3]!="."
        ):
            return False

        return True


    return False




def movimento_valido(
    peca,l1,c1,l2,c2
):

    destino=board[l2][c2]


    if peca=="P":

        if (
            l2==l1-1
            and c1==c2
            and destino=="."
        ):
            return True


        if (
            l1==6
            and l2==4
            and c1==c2
            and board[5][c1]=="."
            and destino=="."
        ):
            return True


        if (
            l2==l1-1
            and abs(c2-c1)==1
            and destino!="."
            and destino.islower()
        ):
            return True

        return False




    if peca=="p":

        if (
            l2==l1+1
            and c1==c2
            and destino=="."
        ):
            return True


        if (
            l1==1
            and l2==3
            and c1==c2
            and board[2][c1]=="."
            and destino=="."
        ):
            return True


        if (
            l2==l1+1
            and abs(c2-c1)==1
            and destino!="."
            and destino.isupper()
        ):
            return True

        return False




    if peca in ["N","n"]:

        dl=abs(l2-l1)
        dc=abs(c2-c1)

        return (
            (dl==2 and dc==1)
            or
            (dl==1 and dc==2)
        )



    if peca in ["R","r"]:
        return caminho_livre_torre(
            l1,c1,l2,c2
        )



    if peca in ["B","b"]:
        return caminho_livre_bispo(
            l1,c1,l2,c2
        )



    if peca in ["Q","q"]:

        return (
            caminho_livre_torre(
                l1,c1,l2,c2
            )
            or
            caminho_livre_bispo(
                l1,c1,l2,c2
            )
        )



    if peca in ["K","k"]:

        if max(
            abs(l2-l1),
            abs(c2-c1)
        )==1:
            return True


        if roque_valido(
            peca,l1,c1,l2,c2
        ):
            return True


        return False


    return False




def achar_rei(cor):

    alvo="K" if cor=="brancas" else "k"

    for l in range(8):
        for c in range(8):

            if board[l][c]==alvo:
                return l,c




def em_xeque(cor):

    rei_l,rei_c=achar_rei(cor)

    for l in range(8):
        for c in range(8):

            peca=board[l][c]

            if peca==".":
                continue


            if (
                cor=="pretas"
                and peca.isupper()
            ):

                if movimento_valido(
                    peca,l,c,
                    rei_l,rei_c
                ):
                    return True



            if (
                cor=="brancas"
                and peca.islower()
            ):

                if movimento_valido(
                    peca,l,c,
                    rei_l,rei_c
                ):
                    return True


    return False




def deixa_em_xeque(
    peca,l1,c1,l2,c2
):

    capturada=board[l2][c2]

    board[l2][c2]=peca
    board[l1][c1]="."


    if peca.isupper():
        em_perigo=em_xeque(
            "brancas"
        )
    else:
        em_perigo=em_xeque(
            "pretas"
        )


    board[l1][c1]=peca
    board[l2][c2]=capturada

    return em_perigo




def xeque_mate(cor):

    if not em_xeque(cor):
        return False


    for l1 in range(8):
        for c1 in range(8):

            peca=board[l1][c1]

            if peca==".":
                continue


            if (
                cor=="brancas"
                and not peca.isupper()
            ):
                continue


            if (
                cor=="pretas"
                and not peca.islower()
            ):
                continue



            for l2 in range(8):
                for c2 in range(8):

                    destino=board[l2][c2]


                    if destino!=".":

                        if (
                            peca.isupper()
                            and destino.isupper()
                        ):
                            continue


                        if (
                            peca.islower()
                            and destino.islower()
                        ):
                            continue



                    if not movimento_valido(
                        peca,
                        l1,c1,
                        l2,c2
                    ):
                        continue


                    if deixa_em_xeque(
                        peca,
                        l1,c1,
                        l2,c2
                    ):
                        continue


                    return False


    return True



def iniciar_jogo():
    global turno

    while True:

        mostrar_tabuleiro()
        print("Turno:", turno)

        jogada = input("Digite jogada ou sair: ")

        if jogada.lower() == "sair":
            break

        partes = jogada.split()

        if len(partes) != 2:
            print("Use formato: e2 e4")
            continue

        origem, destino = partes

        if (
            not coordenada_valida(origem)
            or not coordenada_valida(destino)
        ):
            print("Coordenadas inválidas.")
            continue

        l1, c1 = converter(origem)
        l2, c2 = converter(destino)

        peca = board[l1][c1]

        if peca == ".":
            print("Sem peça.")
            continue

        destino_peca = board[l2][c2]

        if destino_peca != ".":
            if peca.isupper() and destino_peca.isupper():
                print("Peça própria bloqueando.")
                continue

            if peca.islower() and destino_peca.islower():
                print("Peça própria bloqueando.")
                continue

        if turno == "brancas" and not peca.isupper():
            print("Turno das brancas.")
            continue

        if turno == "pretas" and not peca.islower():
            print("Turno das pretas.")
            continue

        if not movimento_valido(peca, l1, c1, l2, c2):
            print("Movimento inválido.")
            continue

        if deixa_em_xeque(peca, l1, c1, l2, c2):
            print("Seu rei ficaria em xeque.")
            continue

        # movimento
        board[l2][c2] = peca
        board[l1][c1] = "."

        # promoção
        if peca == "P" and l2 == 0:
            board[l2][c2] = "Q"
            print("Peão promovido para Rainha.")

        if peca == "p" and l2 == 7:
            board[l2][c2] = "q"
            print("Peão promovido para Rainha.")

        # turno e xeque
        if turno == "brancas":

            if xeque_mate("pretas"):
                print("XEQUE-MATE!")
                print("Brancas vencem.")
                break

            elif em_xeque("pretas"):
                print("XEQUE!")

            turno = "pretas"

        else:

            if xeque_mate("brancas"):
                print("XEQUE-MATE!")
                print("Pretas vencem.")
                break

            elif em_xeque("brancas"):
                print("XEQUE!")

            turno = "brancas"


if __name__ == "__main__":
    iniciar_jogo()


def processar_jogada(origem, destino):
    global turno

    partes = [origem, destino]

    if len(partes) != 2:
        return {"erro": "Formato inválido"}

    if (
        not coordenada_valida(origem)
        or not coordenada_valida(destino)
    ):
        return {"erro": "Coordenadas inválidas"}

    l1, c1 = converter(origem)
    l2, c2 = converter(destino)

    peca = board[l1][c1]

    if peca == ".":
        return {"erro": "Sem peça"}

    if turno == "brancas" and not peca.isupper():
        return {"erro": "Turno das brancas"}

    if turno == "pretas" and not peca.islower():
        return {"erro": "Turno das pretas"}

    if not movimento_valido(peca, l1, c1, l2, c2):
        return {"erro": "Movimento inválido"}

    if deixa_em_xeque(peca, l1, c1, l2, c2):
        return {"erro": "Seu rei ficaria em xeque"}

    board[l2][c2] = peca
    board[l1][c1] = "."

    turno = "pretas" if turno == "brancas" else "brancas"

    return {
        "board": board,
        "turno": turno
    }    

def resetar_jogo():
    global board, turno

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