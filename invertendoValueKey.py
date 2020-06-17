arquivo = open('qualquer.txt')
aurelio = dict()

# Criando o dicionário
for linha in arquivo:
    palavras = linha.rstrip().split()
    for palavra in palavras:
        aurelio[palavra] = aurelio.get(palavra, 0) + 1

lista = []
# Cria um dicionario com VALUE, KEY diferente do original que é KEY, VALUE
for chave, valor in aurelio.items():
    tupla = (valor, chave)
    lista.append(tupla)

lista = sorted(lista, reverse=True)  #  Vai deixar do maior ao menor
# print(lista)
# print(aurelio)
for val, cha in lista[:10]:
    print(cha, val)
