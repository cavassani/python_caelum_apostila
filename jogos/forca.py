import random


def jogar():

    imprime_mensagem_abertura()
    # abro o arquivo
    arquivo = open('palavras.txt', 'r')

    # crio uma lista
    palavras = []

    # adiciono as palavras do arquivo na lista, normalizando as palavras
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    # fecho o arquivo
    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ['_' for letra in palavra_secreta]

    acertou = False
    enforcou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Qual a letra?: ")
        chute.strip().upper()

        if(chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            erros += 1

        enforcou = erros == 5
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print('Você ganhou!!')
    else:
        print('Você perdeu!!')

    print('Fim do jogo')


def imprime_mensagem_abertura():

    print('******************************************')
    print('*****Bem Vindo ao jogo da Forca***********')
    print('******************************************')
