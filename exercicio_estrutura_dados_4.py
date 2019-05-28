print("**********************************************************************")
print("*************************Exercicio 4**********************************")
print("**********************************************************************")
print("Pergunte ao usuário se ele deseja adicionar uma nova pessoa.")
print("Após adicionar dados de algumas pessoas,")
print(",você deve imprimir todos os dados de cada pessoa de forma organizada.")

resp = input("deseja adicionar uma pessoa a lista ? [S/N] : ")

lista = []

while resp == "S":
    nome_pessoa = input("digite seu nome:")
    idade_pessoa = int(input("digite sua idade:"))
    cidade_pessoa = input("digite sua cidade:")

    pessoa = dict(nome=nome_pessoa, idade=idade_pessoa, cidade=cidade_pessoa)

    lista.append(pessoa)

    resp = input("deseja adicionar + uma pessoa a lista ? [S/N] : ")

for humano in lista:
    print(" nome: {} \n idade: {} \n cidade: {}".format(humano['nome'], humano['idade'], humano['cidade']))
