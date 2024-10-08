
print("## Exercicio 1 ##")
vetor = []
for i in range(5):
    num = int(input("Digite um número inteiro: "))
    vetor.append(num)
print(vetor)

print("## Exercicio 2 ##")
vetor = []
for i in range(10):
    num = float(input("Digite um número real: "))
    vetor.append(num)
print(vetor[::-1])

print("## Exercicio 3 ##")
notas = []
for i in range(4):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
media = sum(notas) / len(notas)
print("Notas:", notas)
print("Média:", media)

print("## Exercicio 4 ##")
vetor = []
consoantes = []
for i in range(10):
    caractere = input("Digite um caractere: ").lower()
    vetor.append(caractere)
    if caractere not in 'aeiou' and caractere.isalpha():
        consoantes.append(caractere)
print(f"Foram lidas {len(consoantes)} consoantes:", consoantes)

print("## Exercicio 5 ##")
numeros = []
pares = []
impares = []
for i in range(20):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print("Vetor de números:", numeros)
print("Vetor de números pares:", pares)
print("Vetor de números ímpares:", impares)

print("## Exercicio 6 ##")
medias = []
for aluno in range(10):
    notas = []
    for nota in range(4):
        nota = float(input(f"Digite a nota {nota+1} do aluno {aluno+1}: "))
        notas.append(nota)
    media = sum(notas) / 4
    medias.append(media)
alunos_aprovados = sum(1 for media in medias if media >= 7.0)
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")

print("## Exercicio 7 ##")
vetor = []
for i in range(5):
    num = int(input("Digite um número inteiro: "))
    vetor.append(num)
soma = sum(vetor)
multiplicacao = 1
for num in vetor:
    multiplicacao *= num
print("Números:", vetor)
print("Soma:", soma)
print("Multiplicação:", multiplicacao)

print("## Exercicio 8 ##")
idades = []
alturas = []
for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    altura = float(input(f"Digite a altura da pessoa {i+1}: "))
    idades.append(idade)
    alturas.append(altura)
print("Idades na ordem inversa:", idades[::-1])
print("Alturas na ordem inversa:", alturas[::-1])

print("## Exercicio 9 ##")
vetor = []
for i in range(10):
    num = int(input(f"Digite o número inteiro {i+1}: "))
    vetor.append(num)
soma_quadrados = sum([num ** 2 for num in vetor])
print("Soma dos quadrados dos elementos do vetor:", soma_quadrados)
##################################### TEMINOU #########################################
x = 1
while x != 0:
	input("\n\n##################################### TEMINOU #########################################")
	x += 1
