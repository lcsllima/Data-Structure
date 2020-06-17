docAb = open('texto.txt')
coleção = dict()

for linha in docAb:
    linha = linha.rstrip().split() # linha = linha.split()

    print(linha)
    for palavra in linha:
        # print(palavra)
        coleção[palavra] = coleção.get(palavra, 0) + 1
        # print(palavra)
print(coleção)

maiorValor = None
palavraValor = None

for palavra, contador in coleção.items():
    if maiorValor is None or contador > maiorValor:
        palavraMaior = palavra
        maiorValor = contador

print(palavraMaior, maiorValor)