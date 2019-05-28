print("**********************************************************************")
print("*************************Exercicio 1**********************************")
print("**********************************************************************")
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
print(lista)
print("======================================================================")
# a) imprima o maior elemento
print('a) O maior elemento da lista é: {}'.format(max(lista)))
print("======================================================================")

# b) imprima o menor elemento
print('b) O menor elemento da lsita é: {}'.format(min(lista)))
print(len(lista))
print("======================================================================")

# c) imprima os números pares
print('c) imprima os números pares')
lista_par = []
for item in lista:
    if item % 2 == 0:
        lista_par.append(item)
        print(" o numero {} é par.".format(item))
print('lista apenas com numeros pares: {}'.format(lista_par))
print("======================================================================")

# d) imprima o número de ocorrências do primeiro elemento da lista
print('d)imprima o número de ocorrências do primeiro elemento da lista')
count = 0
for item in lista:
    if item == 12:
        count = count + 1
print("o Numero 12 aparece {} vezes na lista ".format(count))
print("======================================================================")

# e) imprima a média dos elementos
print('e)')
total_itens_lista = len(lista)
soma_itens_lista = sum(lista)
media_lista = soma_itens_lista / total_itens_lista
print('A media da lista é: {}'.format(media_lista))
print("======================================================================")

# f) imprima a soma dos elementos de valor negativo
lista_negativa = []
print('f)')
for item in lista:
    if item < 0:
        lista_negativa.append(item)

print('Soma dos numeros  negativos da lista é: {}'.format(sum(lista_negativa)))
print("======================================================================")
