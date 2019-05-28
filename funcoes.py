def velocidade_media(distancia, tempo):
    velocidade = distancia/tempo
    return velocidade


resposta = velocidade_media(100, 20)
print(resposta)

resposta2 = velocidade_media(150, 50)
print(resposta2)

resposta3 = velocidade_media(200, 30)
print(resposta3)

resposta4 = velocidade_media(50, 3)
print(resposta4)


def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado


def subtracao(num1, num2):
    resultado = num1 - num2
    return resultado


def divisao(nume1, nume2):
    resultado = nume1 / nume2
    return resultado


def multiplicacao(numero1, numero2):
    resultado = numero1 * numero2
    return resultado


def calculadora(numero1, numero2):
    return (soma(numero1, numero2), subtracao(numero1, numero2), multiplicacao(numero1, numero2), divisao(numero1, numero2))


print(calculadora(13, 5))
