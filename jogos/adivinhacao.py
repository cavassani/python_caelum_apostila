import random

def jogar():
    abertura_do_game()


    nivel = escolha_nivel()


    numero_secreto = random.randrange(1, 50)

    
    total_tentativas = dificuldade(nivel)


    rodada = 1
    for rodada in range(1, total_tentativas + 1):
        print('---------------------')
        print('Tentativa {} de {}'.format(rodada, total_tentativas))
        print('---------------------')
        chute = int(input('Digite seu numero: '))
        print('você digitou o numero: {}'.format(chute))

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if (acertou):
            print('Você acertou!!')
            break
        elif (maior):
            print('Você errou, tente um numero mais baixo')
        elif (menor):
            print('Você errou, tente um numero mais alto')

        rodada = rodada + 1
        mensagem_final()
        

def abertura_do_game():
    print('**************************')
    print('*                        *')
    print('*  Jogo da Advinhaçao    *')
    print('*                        *')
    print('**************************')

def escolha_nivel():
    nivel = int(input('Escolha um nivel de jogo[1, 2 ou 3]: '))

    while(nivel > 3):
        nivel = int(input('Escolha um nivel de jogo[1, 2 ou 3]: '))

    return nivel

def dificuldade(nivel):
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = int(10)
    elif (nivel == 3):
        total_tentativas = 5

    return total_tentativas

def mensagem_final():
    print('*************')
    print('*FIM DO JOGO*')
    print('*************')