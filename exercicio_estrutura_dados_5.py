print("**********************************************************************")
print("*************************Exercicio 5**********************************")
print("**********************************************************************")
print("utilizando um dict que leia dados de entrada do usuário. O usuário deve entrar com os dados de uma pessoa como nome, idade e cidade onde mora")

nome_pessoa = input("digite seu nome:")
idade_pessoa = int(input("digite sua idade:"))
cidade_pessoa = input("digite sua cidade:")

pessoa = dict(nome=nome_pessoa, idade=idade_pessoa, cidade=cidade_pessoa)


print(" nome: {} \n idade: {} \n cidade: {}".format(pessoa['nome'], pessoa['idade'], pessoa['cidade']))
