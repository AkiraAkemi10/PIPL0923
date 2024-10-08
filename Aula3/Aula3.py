# tuples

tp1 = ("Gonçalo", "ATEC", 10793)

print(tp1)
print(tp1[0])
print(tp1[1])
print(tp1[2])

# tp1[0] = "novo nome" <--- Erro
# print(tp1[0]) <--- Erro
temp_list = list(tp1)
print(list_temp)

list_temp[0] = "Novo nome"
tp1 = tuple(list_temp)
print("--- unpack ---")
tp1 = ("Gonçalo", "ATEC", 10793)


(nome, escola, UFCD) = tp1

print("nome")
print("escola")
print("UFCD")

nome = "Novo nome 2"

print("--- unpack list ---")
tp1 = ("Gonçalo", "ATEC", 10793)


print("--- Metodos Tuple ---")
print(tp1.count("Gonçalo"))


# listas (arrays) #############################################
print("------------ listas (arrays) ------------")
# Lista vs Array
my_list = ["Gonçalo", "ana", "Rita", "Luiz"]

print(my_list)
print(my_list[0])
print(my_list[1])

my_list[0] = "Novo nome"
print(my_list[0])
print(my_list)

nomes = [    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia",    "Karla", "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro", "Quintino", "Rafael", "Sara", "Tatiana",    "Ursula", "Vinicius", "Wagner", "Xavier", "Yasmin"]

print(nomes[0])

print(nomes[0:5]) # nome[n:m] --> n a m-1

print(nomes[6:10])

print(nomes[-10: -5])

print(nomes[0:20:3])

nomes.append("Rita")
print(nomes)

nomes.append("Aaron")
print(nomes[-1])

print("Insert")
print(nomes[0:4])
nomes.insert(1, "Novo nome")
print(nomes[0:4])

print("Remove")

print(nomes.remove("Novo nome"))
print(nomes[0:4])

print(nomes[7])
print(nomes.pop[7])
print(nomes[7])

for nome in nomes:
    print(nome)
# Set #########################################################

# dict ########################################################