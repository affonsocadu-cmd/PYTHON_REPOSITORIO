# 0 --> sair do program
# 1 --> entrar no programa
# ----> erro!!
escolha_usuario = 1123

match escolha_usuario:
    case 0:
        print("Sair do programa")
    case 1:
        print("Entrar no programa")
    case _:
        print("Erro!!")