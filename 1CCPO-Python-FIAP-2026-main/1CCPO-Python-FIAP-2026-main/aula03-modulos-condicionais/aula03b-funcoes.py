# FUNÇÃO SEM RETORNO E SEM PARAMETRO
def print_lyrics():
    print("I ain't gonna live forever")
    print("I just want to live while I'm alive")

print_lyrics()
print_lyrics()

# FUNÇÃO SEM RETORNO E COM PARAMETRO
def boas_vindas(nome):
    print(f"Olá, {nome}!!! Seja bem-vindo!!")

nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado)

# FUNÇÃO COM RETORNO E COM PARAMETRO
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado_soma = soma(2,10)
print(resultado_soma)
