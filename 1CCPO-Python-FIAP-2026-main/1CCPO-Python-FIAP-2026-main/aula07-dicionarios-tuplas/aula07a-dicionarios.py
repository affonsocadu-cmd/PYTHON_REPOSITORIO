eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {
    'one': 'uno',
    'two': 'dos'
}
print(eng2sp)
print(eng2sp['two'])

print('two' in eng2sp)

# CONTAGEM DE LETRAS
def count_letters(s):
    d = dict() # {}
    for c in s: # s = ovo | c = "o"
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

dict_contagem = count_letters("ovo")
print(dict_contagem)