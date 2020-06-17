dNome = input('Insira o nome do Doc: ')
if len(dNome) < 1:
    dNome = 'texto2.txt'

portal = open(dNome)
aurelio = dict()

for linha in portal:
    linha = linha.rstrip()
    # print(linha)
    palavras = linha.split()
    # print(palavras)
    for palavra in palavras:
        # print('-'*30)
        # print('**',palavra, aurelio.get(palavra, -99))

        # Se não tiver nada, vai coontar como 0, se tiver, usa o valor que tem
        # contaAntiga = aurelio.get(palavra, 0)
        # print(f'{palavra} velha {contaAntiga}')
        # novaConta = contaAntiga + 1
        # aurelio[palavra] = novaConta
        #
        #  O trecho abaixo substitui todo o trecho a cima
        # idiom: retrieve/create/update counter
        aurelio[palavra] = aurelio.get(palavra, 0) + 1
        # print(f'{palavra} nova {aurelio[palavra]}')


        
        # print(palavra)
        # if palavra in aurelio:
        #     aurelio[palavra] = aurelio[palavra] + 1
        #     # print('**Existing**')
        # else:
        #     aurelio[palavra] = 1
        #     # print('**NEW**')
        # print(palavra, aurelio[palavra])



print(aurelio)
# aurelio[palavra] = aurelio.get(palavra, 0) + 1

maior = None
campeao = None

for k, v in aurelio.items():
    if campeao is None or maior < v:
        campeao = k
        maior = v

if maior > 1:
    es = 'es'
else:
    es = ''

print(f'O valor com mais aparições foi: {campeao}, ocorrendo {maior} vez{es}')
