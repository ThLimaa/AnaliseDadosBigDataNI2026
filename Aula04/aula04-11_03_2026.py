## Aula 04 - Estruturas de Decisão II

# carro=False
# combustivel=False

# # Qual a condição pro carro funcionar ?

# if not carro and not combustivel:
#     print("Meu fusca está rodando.")
# else:
#     print("Não sobrou nada pro fusca.")

# print("*")

# if not carro and not combustivel:
#     print("Meu fusca está rodando.")
# elif carro==False or combustivel==False:
#     print("Não sobrou nada pro fusquinha.")
# else:
#     print("Erro de execução.")


#MATH CASE:
try:
    mes = int(input("Informe o mês:"))
    match mes:
        case 1:
            print("Janeiro.")
        case 2:
            print("Fevereiro.")
        case 3:
            print("Março.")
        case 4:
            print("Abril")
        case 5:
            print("Maio")
        case 6:
            print("Junho.")
        case 7:
            print("Julho")
        case 8:
            print("Agosto")
        case 9:
            print("Setembro")
        case 10:
            print("Outubro")
        case 11:
            print("Novembro")
        case 12:
            print("Dezembro")    
        case _:  ## O underline ( _ ) funciona como o 'default' ou 'else'
            print("Mês inválido.")               
except ValueError:
    print("Entrada inválida. Digite um número inteiro: ")

# try:
#     numero_mes = int(input("Digite um número de 1 a 12: "))

#     match numero_mes:
#         case 1:
#             print("O número 1 corresponde a Janeiro.")
#  # Inclua todos os outros meses aqui!
#         case 12:
#             print("O número 12 corresponde a Dezembro.")
#         case _:
#             print(f"Número {numero_mes} inválido. Digite entre 1 e 12.")
# except ValueError:
#         print("Entrada inválida. Por favor, digite um número inteiro.")