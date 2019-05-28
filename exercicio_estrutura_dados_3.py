print("**********************************************************************")
print("*************************Exercicio 3**********************************")
print("**********************************************************************")
print("Faça um programa que leia 4 notas, mostre as notas e a média na tela.")

nota1 = int(input("digite a nota 1:"))
nota2 = int(input("digite a nota 2:"))
nota3 = int(input("digite a nota 3:"))
nota4 = int(input("digite a nota 4:"))

media = nota1 + nota2 + nota3 + nota4 / 4
print("As notas do aluno são: nota 1: {}, nota 2: {}, nota 3: {}, nota 4: {} e a media é: {}".format(nota1, nota2, nota3, nota4, media))
