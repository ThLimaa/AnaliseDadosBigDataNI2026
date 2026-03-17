# O range(5) gera os números 0, 1, 2, 3, 4 (5 repetições)
# for i in range(5):
#     try:
#         # i representa o número atual da repetição (0, 1, 2...)
#         print(f"Número {i + 1} de 5:")
#         num = float(input("Digite um número: "))
 
#         dobro = num * 2
#         triplo = num * 3
#         quádruplo = num * 4
 
#         print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
 
#     except ValueError:
#         print("Entrada inválida. Tente novamente.")



# >>> WHILE

# loolap=float(input('Qual o valor do evento (inteira)?')) #Dependendo do input, cai num loop infinito

# while loolap > 300:
#     print('Mas não vou mesmo!!!')

# print('Estarei lá!')
# ##

# loolap=0

# while loolap > 300:
#     loolap=float(input('Qual o valor do evento (inteira)?')) #Dependendo do input, cai num loop infinito
#     print('Mas não vou mesmo!!!')

# print('Estarei lá!')
# ##

# loolap=300

# while loolap >= 300:
#     loolap=float(input('Qual o valor do evento (inteira)?')) #Dependendo do input, cai num loop infinito
#     print('Mas não vou mesmo!!!')

# print('Estarei lá!')


#######

# LISTAS:

nomes = ['Matheus','Alice','Caio','Larissa','Miguel','Rafael']

# nome1 = nomes[0]

# print(nomes[-1])
# print(nomes[-2])
# print(nomes[-3])
# print(nomes[-4])
# print(nome1)

# primeira_parte=nomes[0:3]
# print(primeira_parte)
# segunda_parte=nomes[3:6]
# print(segunda_parte)

# print(len(nomes))

#TUPLAS:
nomes_tupla = tuple(nomes)

#SETS:
nome_set = set(nomes)
print(nome_set)

#DICIONÁRIO
nome_dict = {"nome 1" : "Matheus",
              "nome 2" : "Alice", 
              "nome 3" : "Caio", 
              }









