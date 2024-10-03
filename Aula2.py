# Exercicio 1
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

if n1 > n2:
    print(n1)
else:
    print(n2)
    
# Exercicio 2
genero = input("És Homem(M) ou Mulher(F): ")

if genero == M or genero == m or genero == Homem or genero == homem:
    print("Masculino")
elif genero == F or genero == f or genero == Mulher or genero == mulher:
    print("Feminino")
else:
    print("Género invalido")
    
# loop

# while (Enquanto- faça)

count = 0
while op != "q":
    print(f"loop: {count})
    
    op = input("Selecione a op: ")
    
    count += 1
    
num = 0

while num < 10:
    print(num)
    num += 1

# Range

range(0,10,2)

"""
range(a,b,c)

a - LB
b - UB
c - step

range(1, 5)
1, 2, 3, 4

range(5)
0, 1, 2, 3, 4

range(0, 10, 2)
0, 2, 4, 6, 8

range(0, 10, 3)
0, 3, 6, 9
"""

# for (para)
print("---" * 10)
for elm in range(0,10,2):
    print(elm)

print("---" * 10)
for elm in range(0,100):
    print(elm)
    if elm == 50:
        break
print("Fim do loop")

# Listas
nomes = [
    "Bruno", "Carlo", "João", "Maria", "Pedro", "Ana", "Miguel", "Rita", "José", "Ana", "Carla", "António", "Sofia",
    "Manuel", "Francisca", "Carlos", "Isabel", "Luís", "Patrícia", "Ricardo", "Beatriz" ]

for nome in nomes:
    print(nome)

print("Fim do loop")

print(nomes.count("Daniela"))

print(nome.__len__())
print(len(nome))

print(nomes.__contains__("Sara"))
print(nomes.__contains__("Ana"))
print("Pedro" in nomes)

#nomes.sort(reverse=true)

print("---------------" * 5)
nomes.sort()
print(nomes)

# Faça um programa que peça uma nota, entre zero e dez.Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = int(input("Insira uma nota sde 0 a 10: "))
while nota in range(11):
    print("valor Invalido")
    nota = int(input("Insira uma nota de 0 a 10: "))
print("A tua nota é", nota)