import re

doc = open('oTexto')
lista = []

for linha in doc:
    linha = linha.rstrip()
    # print(linha)
    dado = re.findall('[0-9]+', linha)
    # print(dado)
    for numero in dado:
        lista.append(numero)
    # print(lista)

intList = []
for num in lista:
    intList.append(int(num))

print(sum(intList))
