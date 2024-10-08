# Faça um programa que leia 20 numeros inteiros e armazene-os numa lista
# Armazene os numeros pares na lista PAR e os numeros impares na lista IMPAR
# Imprima os três vetores

lista = []
quantidade = 20
contagem = 0
par = []
impar = []


while contagem != quantidade:
    leitura = int(input("Insira um valor: "))
    lista.append(leitura)
    contagem += 1
    
    if leitura % 2 == 0:
        par.append(leitura)
    else:
        impar.append(leitura)

print("Lista de numeros inteiros: "lista)
print("Lista de numeros pares: "par)
print("Lista de numeros impares: "impar)