name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
colecao = dict()

for linha in handle:
    if not linha.startswith('From '):
        continue
    listaLinha = linha.rstrip().split()
    print(listaLinha)
    for palavra in listaLinha:
        if palavra == listaLinha[1]:
            print(palavra)
            colecao[palavra] = colecao.get(palavra, 0) + 1

print(colecao)
contador = None
palavraMaior = None

for key, value in colecao.items():
    if contador is None or value > contador:
        contador = value
        palavraMaior = key

print(palavraMaior, contador)
