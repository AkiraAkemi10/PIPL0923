#receba N notas (0 a 20) como input e adicione esses valroes a uma lista.
# mostre o conteudo de lista 
# deve preguntar ao utilizadar qunados valores pretende adicionar
# deve garantir que todas as notas sao validas
# deve assumir que o utilizador vai tentar adicionar valores numericos
contagem = int(input("Quantas notas pretende adicionar?: "))
lista = []
nota = 0
for i in range(contagem):
    nota = int(input(f"Insira a {i+1}º nota: "))
    while nota > 20 or nota < 0:
        if nota > 20 or nota < 0:
            print("Nota invalida")
            nota = int(input(f"Insira novamente a {i+1}º nota: "))
        else:
            break
    lista.append(nota)
print(lista)