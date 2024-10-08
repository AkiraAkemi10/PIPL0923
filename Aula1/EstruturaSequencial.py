#1
print("** Exercicio 1 **\n")

print("Alo mundo")

#2
print("\n** Exercicio 2 **\n")

numero = int(input("Escreva um numero: "))
print(f"O número informado foi {numero}")

#3
print("\n** Exercicio 3 **\n")

numero1 = int(input("Escreva um numero: "))
numero2 = int(input("Escreva outro numero: "))
print(f"A soma de {numero1} com o {numero2} dá {numero1 + numero2}")

#4
print("\n** Exercicio 4 **\n")

n1 = int(input("Escreve uma nota: "))
n2 = int(input("Escreve outra nota: "))
n3 = int(input("Escreve outra nota: "))
n4 = int(input("Escreve outra nota: "))

matriz_da_media = (n1, n2, n3, n4)
soma_das_notas = sum(matriz_da_media)
numero_de_notas = len(matriz_da_media)
media = soma_das_notas / numero_de_notas

print(f"A media das notas é {media}")

#5
print("\n** Exercicio 5 **\n")

leia_metro = float(input("Escreva a medida de algo em metros: "))
convercao_centimetro = leia_metro * 100
print(f"Essa coisa mede {convercao_centimetro}cm")

#6
print("\n** Exercicio 6 **\n")

import math
raio = float(input("Qual o raio do circulo em centimetros: "))
area = math.pi * raio**2
print(f"A área desse criculo é {area}cm2")

#7
print("\n** Exercicio 7 **\n")

ladoquadrado = float(input("Escreve o tamanho em centimetro de um dos lados dum quadrado: "))
areaquadrado = ladoquadrado**2
print("A área desse quadrado é ", areaquadrado, "\nE o dobro dela é ", areaquadrado*2, "cm")

#8
print("\n** Exercicio 8 **\n")

hora = float(input("Quanto ganhas por hora: "))
mes = float(input("Quantas horas trabalhas por mês: "))
salario = hora * mes
print(f"Ao fim do mês tu ganhas {salario}€")

#9
print("\n** Exercicio 9 **\n")

f = int(input("Escreve a temperatura em Fahrenheit: "))
celsius  = 5 * ((f - 32) / 9)
print(f"{f} Fahrenheit são {round(celsius)} graus celsius")

#10
print("\n** Exercicio 10 **\n")

celsius = int(input("Escreve a temperatura em Graus: "))
f = ((celsius * 9 / 5) + 32)
print(f"{celsius} graus celsius são {round(f)} Fahrenheit")

#11
print("\n** Exercicio 11 **\n")

n1 = int(input("Escreva um numero inteiro: "))
n2 = int(input("Escreva outro numero inteiro: "))
n3 = float(input("Escreva um numero real: "))
a = (n1 * 2) * (n2 / 2)
b = (n1 * 3) + n3
c = n3 ** 3
print(f"O produto do dobro de {n1} com a metade de {n2} dá {a}")
print(f"A soma do triplo de {n1} com {n3} dá {b}.")
print(f"{n3} elevado ao cubo dá {c}.")

#12
print("\n** Exercicio 12 **\n")

altura = float(input("Qual a tua altura em metros: "))
peso = (72.7 * altura) - 58

print(f"O teu peso ideal seria {round(peso)}Kg")

#13
print("\n** Exercicio 13 **\n")

h = float(input("Qual a tua altura em metros: "))
sexo = input("És Homem(H) ou Mulher(M): ")

if sexo == 'H' or 'h' or 'Homem' or 'homem':
    peso = (72.7 * h) - 58
else:
    peso = (62.1 * h) - 44.7
print(f"O teu peso ideal seria {round(peso)}Kg")

#14
print("\n** Exercicio 14 **\n")

kgpescado = float(input("Quantos quilos o João pescou: "))
excesso = kgpescado - 50
multa = excesso * 4
if excesso > 0:
    print(f"O João tem {excesso}Kg a mais do que o permitido, ele tem de pagar {multa}€ de multa.")
else:
    print("O João pescou dentro do limite aceitavel, ele não tem de pagar nenhuma multa.")
#15
print("\n** Exercicio 15 **\n")

hora = float(input("Quanto ganhas por hora: "))
mes = float(input("Quantas horas trabalhas por mês: "))
salario = hora * mes
IR = salario -
print(f"Ao fim do mês tu ganhas {salario}€")
#16
print("\n** Exercicio 16 **\n")

#17
print("\n** Exercicio 17 **\n")

#18
print("\n** Exercicio 18 **\n")
