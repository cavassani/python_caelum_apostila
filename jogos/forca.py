import random


def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    acertou = False
    enforcou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute,letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print('Fim do jogo')


def imprime_mensagem_abertura():

    print('******************************************')
    print('*****Bem Vindo ao jogo da Forca***********')
    print('******************************************')


def carrega_palavra_secreta():
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

    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    letras_acertadas = ['_' for letra in palavra]
    return letras_acertadas


def pede_chute():
    chute = input("Qual a letra?: ")
    chute = chute.upper().strip()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[posicao] = letra
        posicao += 1


def imprime_mensagem_vencedor():
    print("Você ganhou!!!")
    print('Parabéns, você ganhou!')
    print("		 ___________	")
    print("		'._==_==_=_.'	")
    print("		 -\\:	  /-.   ")
    print("	  |  (|:.	  |)  |	")
    print("		'-|:.	  |-'	")
    print("		  \\::.   /		")
    print("		  '::.	.'		")
    print("			)   (		")
    print("		  _.'   '._		")
    print("		  '-------'		") 


def imprime_mensagem_perdedor(palavra_secreta):
    print('A palavra era {}'.format(palavra_secreta))
    print("    ----------------        ")
    print("   /                \       ")
    print("  /                  \      ")
    print("//                    \/\   ")
    print("\|   XXXX       XXXX  | /   ")
    print(" |   XXXX       XXXX  |/    ")
    print(" |   XXX         XXX  |     ")
    print(" |                    |     ")
    print(" \__       XXX      __/     ")
    print("   |\      XXX     /|       ")
    print("   | |            | |       ")
    print("   | I I I I I I I  |       ")
    print("   |  I I I I I I   |       ")
    print("   \__            __/       ")
    print("      \__      __/          ")
    print("       \_______/            ")


def desenha_forca(erros):
    if (erros == 1):
        print("      /////       ")
    elif (erros == 2):
       print("      /////       ")
       print("    (.O...O.)     ")
    elif (erros == 3):
        print("      /////       ")
        print("    (.X...X.)     ")
        print("       ||||      ")
    elif (erros == 4):
        print("      /////       ")
        print("    (.O...O.)     ")
        print("       ||||      ")
        print("=======||||========")
    elif (erros == 5):
        print("      /////       ")
        print("    (.o...o.)     ")
        print("       ||||      ")
        print("=======||||========")
        print("      //..\\       ")
    elif (erros == 6):
        print("      /////       ")
        print("    (.X...O.)     ")
        print("       ||||      ")
        print("=======||||========")
        print("      //..\\       ")
    elif (erros == 7):
        print("      /////       ")
        print("    (.X...X.)     ")
        print("       ||||      ")
        print("=======||||========")
        print("      //..\\       ")
        print("você se fudeu meu irmão!!!!!!!!!!")