print("Hello World")

# Comentarios:
""" 
bdwuhecjn
ewcwd
cdwc
"""



# var
nome = "Valor" # str/String é uma cadeia de caracteres
idade = 10 # int é um numero inteiro sem limite de tamanho
nota = 10.9 # Float é um numero com 6 a 7 casas decimais, double tem 14
aprovado = True # Valor True(Verdadeiro) ou False(Falso)


# Somas
soma = idade + 3
print(soma)

soma2 = nota + 2
print(soma2)

soma3 = nome + "Foo"
print(soma3)

#soma4 = nome + 2024
#print(nome)

op5 = nome * 2
print(op5)


# print v2

nome = "Afonso"
ano = 2024

# Olá Mundo, Afonso em 2024

# str(ano) converte para string
print("Olá Mundo, " + nome + " em " + str(ano))

print("Olá Mundo,", nome, "em", str(ano))

print("Olá Mundo,", nome, "em", ano)

print(f"Olá Mundo, {nome.upper()} em {ano}")


# -> % <-
op2 = 10 % 3
print(op2)

op3 = 13 % 3
print(op3)

op4 = 10 / 3
print(op4)

op5 = 10 // 3
print(op5)

# ler dados do teclado
nome = input("Escreve o teu nome: ")
print(f"Olá {nome}")


#IFs

idade = 10
if idade >= 18:
    print("És um adulto")
else:
    print("Não és um adulto")

print("Fora do if")



idade = 18
if idade > 18:
    print("És um adulto")
elif idade > 15:
    print("És jovem")
else:
    print("És uma criança")
