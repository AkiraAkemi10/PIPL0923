# Reseba N valores como input e adicione esses valores a uma lista
# mostre o conteudo da lista
# deve perguntar ao utilizador quantos valores pretende adicionar
lista = []
quantidade = int(input("Quantos valores pretende adicionar à lista?: "))
contagem = 0
if quantidade > 0:
    lista.append(input("Insira um valor: "))
    contagem += 1
    while contagem != quantidade:
        lista.append(input("Insira outro valor: "))
        contagem += 1
else:
    print("A lista está vazia.")
print(lista)