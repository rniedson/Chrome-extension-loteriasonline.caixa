# Versão 0.3
from random import randint

print('+' * 40)
print('Bem-vindo')
print('+' * 40)
print('Selecione o jogo: ')
print('1 - Mega-sena  |  2 - Quina  |  3 - Lotofácil  |  4 - Lotomania')

# Escolher um tipo de jogo
while True:
    try:
        tp_jogo = int(input("Escolha uma opção de jogo: "))
        if tp_jogo < 1 or tp_jogo  > 4:
            raise ValueError()
        break
    except ValueError:
        print("Você deve escolher um número de 1 a 4")

#Variáveis padrão dos jogos
nome_jogo = ['Mega-sena', 'Quina', 'Lotofácil', 'Lotomania']
amplitude = [60, 80, 25, 100]
quantidade_numeros = [6, 5, 15, 50]


# Validação input numeros
while True:
    if tp_jogo == 1: #validação do input quantidade de números para opção 1 - MegaSena
        try:
            n_numeros = int(input("Informe quantos numeros deseja jogar: "))
            if n_numeros < 6 or n_numeros > 15:
                raise ValueError()
            break
        except ValueError:
            print("Você deve inserir um valor inteiro entre 6 e 15")
    elif tp_jogo == 2:  #validação do input quantidade de números para opção 2 - Quina
        try:
            n_numeros = int(input("Informe quantos numeros: "))
            if n_numeros < 5 or n_numeros > 15:
                raise ValueError()
            break
        except ValueError:
            print("Você deve inserir um valor inteiro entre 5 e 15")
    elif tp_jogo == 3:  #validação do input quantidade de números para opção 3 - lotofácil
        try:
            n_numeros = int(input("Informe quantos numeros deseja jogar: "))
            if n_numeros < 15 or n_numeros > 18:
                raise ValueError()
            break
        except ValueError:
            print("Você deve inserir um valor inteiro entre 15 e 18")
    else: #validação do input quantidade de números para opção 4 - lotomania'
        try:
            n_numeros = int(input("Informe quantos numeros deseja jogar: "))
            if n_numeros != 50 :
                raise ValueError()
            break
        except ValueError:
            print("Para este jogo a única opção é 50 números")


# Validação input quantidade de jogos
while True:
    try:
        n_jogos = int(input("Informe a quantidade de jogos :"))
        if n_jogos < 1 or n_jogos > 10:
            raise ValueError()
        break
    except ValueError:
        print("Você deve inserir um valor inteiro entre 1 e 10.")

# Função cria jogo
def cria_jogo(n_numeros, n_jogos):
    for x in range(n_jogos):
        print("-" * 40)
        print(nome_jogo[tp_jogo - 1], " - jogo", x + 1)
        print("-" * 40)
        jogo = []
        while len(jogo) != n_numeros:  # enquanto o tamanho da lista não for igual a quantidade de números informados repetir a operação
            r = randint(1, amplitude[tp_jogo - 1])  # r recebe um número aleatório entre 1 e 60
            if r not in jogo:  # Se r não existir na lista acrescentá-lo
                jogo.append(r)

        print(sorted(jogo))  # imprimir número ordenado

    print("-" * 40)
    print('Quantida de jogo(s):', n_jogos)  # imprimir número ordenado


# Define valor do jogo utilizando um dicionário
def valor_jogo(nomejogoescolhido, n_jogos):
    dicValorJogo = {
        'Mega-sena6': 4.50,
        'Mega-sena7': 31.50,
        'Mega-sena8': 126,
        'Mega-sena9': 378,
        'Mega-sena10': 945,
        'Mega-sena11': 2079,
        'Mega-sena12': 4158,
        'Mega-sena13': 7722,
        'Mega-sena14': 13513.50,
        'Mega-sena15': 13513.50,
        'Quina5': 2.00,
        'Quina6': 12.00,
        'Quina7': 42.00,
        'Quina8': 112.00,
        'Quina9': 252.00,
        'Quina10': 504.00,
        'Quina11': 924.00,
        'Quina12': 1584.00,
        'Quina13': 2574.00,
        'Quina14': 4004.00,
        'Quina15': 6006.00,
        'Lotofácil15': 2.50,
        'Lotofácil16': 40.00,
        'Lotofácil17': 340.00,
        'Lotofácil18': 2040.00,
        'Lotomania50': 2.50,

    }
    ValorTotalJogo = dicValorJogo[nomejogoescolhido] * n_jogos
    return ValorTotalJogo

# Define valor do jogo utilizando um dicionário
def prob_jogo(nome_jogo, n_numeros):
    dicProbJobo = {
        'Mega-sena6': '\nSena: 50.063.860 \nQuina: 154.518 \nQuadra: 2.332',
        'Mega-sena7': '\nSena: 7.151.980 \nQuina: 44.981 \nQuadra: 1.038',
        'Mega-sena8': '\nSena: 1.787.995 \nQuina: 17.192 \nQuadra: 539',
        'Mega-sena9': '\nSena: 595.998 \nQuina: 7.791 \nQuadra: 312',
        'Mega-sena10': '\nSena: 238.399 \nQuina: 3.973 \nQuadra: 195',
        'Mega-sena11': '\nSena: 108.363 \nQuina: 2.211 \nQuadra: 129',
        'Mega-sena12': '\nSena: 54.182 \nQuina: 1.317 \nQuadra: 90',
        'Mega-sena13': '\nSena: 29.175 \nQuina: 828 \nQuadra: 65',
        'Mega-sena14': '\nSena: 16.671 \nQuina: 544 \nQuadra: 48',
        'Mega-sena15': '\nSena: 10.003 \nQui3na: 370 \nQuadra: 37',
        'Quina5': '\nQuina: 124.040.016 \nQuadra: 64.106 \nTerno: 866 \nDuque: 36',
        'Quina6': '\nQuina: 4.006.669 \nQuadra: 21.658 \nTerno: 445 \nDuque: 36',
        'Quina7': '\nQuina: 1.144.763 \nQuadra: 9.409 \nTerno: 261 \nDuque: 36',
        'Quina8': '\nQuina: 429.286 \nQuadra: 4.770 \nTerno: 168 \nDuque: 36',
        'Quina9': '\nQuina: 190.794 \nQuadra: 2.687 \nTerno: 115 \nDuque: 36',
        'Quina10': '\nQuina: 95.396 \nQuadra: 1.635 \nTerno: 82 \nDuque: 36',
        'Quina11': '\nQuina: 52.035 \nQuadra: 1.056 \nTerno: 62 \nDuque: 36',
        'Quina12': '\nQuina: 30.354 \nQuadra: 714 \nTerno: 48 \nDuque: 36',
        'Quina13': '\nQuina: 18.679 \nQuadra: 502 \nTerno: 38 \nDuque: 36',
        'Quina14': '\nQuina: 12.008 \nQuadra: 364 \nTerno: 31\nDuque: 36',
        'Quina15': '\nQuina: 8.005 \nQuadra: 271 \nTerno: 25 \nDuque: 36',
        'Lotofácil15': '\n15 números: 3.268.760 \n14 números: 21.791 \n13 números: 691 \n12 números: 59 \n11 números: 11',
        'Lotofácil16': '\n15 números: 204.297 \n14 números:3.026 \n13 números: 162 \n12 números: 21 \n11 números: 5,9',
        'Lotofácil17': '\n15 números: 24.035 \n14 números: 600 \n13 números: 49 \n12 números: 9,4 \n11 números: 3,7',
        'Lotofácil18': '\n15 números: 4.005 \n14 números: 152 \n13 números: 18 \n12 números: 5 \n11 números: 2,9',
        'Lotomania50': '\n20 números: 1/11.372.635 \n19 números: 1/352.551 \n18 números: 1/24.235 \n17 números: 1/2.776 \n16 números: 1/472 \n15 números: 1/112 \n00 números: 1/11.372.635'
    }
    ProbabilidadeJogo = dicProbJobo[nome_jogo+str(n_numeros)]
    return ProbabilidadeJogo

# chama a função megasena passando a quantidade de números e quantidade de jogos
cria_jogo(n_numeros, n_jogos)

# print chama a funcção valor jogo passando o nome do jogo concatenado com string quantidade de números solitados, número de jogos
print("\nO valor total dos jogos é R$ ", valor_jogo(nome_jogo[tp_jogo-1]+str(n_numeros), n_jogos))

print("\nProbabilidade de acerto na ", nome_jogo[tp_jogo-1], " apostando ", n_numeros, " números é ", prob_jogo(nome_jogo[tp_jogo-1], n_numeros))
