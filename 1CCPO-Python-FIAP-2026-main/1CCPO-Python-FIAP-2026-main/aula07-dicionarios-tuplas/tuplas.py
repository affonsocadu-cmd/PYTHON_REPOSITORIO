from shlex import split

t = ('a', 'b', 'c')
print(t)

t1 = 'A',
print(t1)

# ATRIBUIÇÃO DE TUPLA
a = 5
b = 10

a, b = b, a
print(a, b)

email = "fulano@gmail.com"
username, dominio = email.split("@")
print(username)
print(dominio)