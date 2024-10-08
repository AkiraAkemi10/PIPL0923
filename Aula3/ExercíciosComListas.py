
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

print("## Exercicio 10 ##")
vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
    num1 = int(input(f"Digite o {i+1}º número do primeiro vetor: "))
    num2 = int(input(f"Digite o {i+1}º número do segundo vetor: "))
    vetor1.append(num1)
    vetor2.append(num2)

for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print("Vetor intercalado:", vetor3)

print("## Exercicio 11 ##")
vetor1 = []
vetor2 = []
vetor3 = []
vetor_final = []

for i in range(10):
    vetor1.append(int(input(f"Digite o {i+1}º número do primeiro vetor: ")))
    vetor2.append(int(input(f"Digite o {i+1}º número do segundo vetor: ")))
    vetor3.append(int(input(f"Digite o {i+1}º número do terceiro vetor: ")))

for i in range(10):
    vetor_final.append(vetor1[i])
    vetor_final.append(vetor2[i])
    vetor_final.append(vetor3[i])

print("Vetor intercalado:", vetor_final)

print("## Exercicio 12 ##")
idades = []
alturas = []

for i in range(30):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    altura = float(input(f"Digite a altura do aluno {i+1} em metros: "))
    idades.append(idade)
    alturas.append(altura)

media_altura = sum(alturas) / len(alturas)
alunos_com_mais_13_anos = sum(1 for i in range(30) if idades[i] > 13 and alturas[i] < media_altura)

print(f"Alunos com mais de 13 anos e altura abaixo da média: {alunos_com_mais_13_anos}")

print("## Exercicio 13 ##")
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]
temperaturas = []

for i in range(12):
    temperatura = float(input(f"Digite a temperatura média de {meses[i]}: "))
    temperaturas.append(temperatura)

media_anual = sum(temperaturas) / len(temperaturas)

print(f"Média anual das temperaturas: {media_anual:.2f}°C")
print("Meses com temperatura acima da média anual:")

for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{i+1} - {meses[i]}: {temperaturas[i]:.2f}°C")
##################################### TEMINOU #########################################
