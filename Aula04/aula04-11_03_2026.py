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

# LISTA DE EXERCICIOS - AULA 4

# 1. Cálculo de Lâmpadas: # Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
# Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. 
# Considere que a potência necessária é de 3 watts por metro quadrado e a cada 3m² existe um bocal para uma lâmpada.
# 
# 
# 

# 
# 
# 
# 2. Quantidade de Caixas de Azulejos:
# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
# largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
# todas as suas paredes (considere que não será descontada a área ocupada por portas e
# janelas). Cada caixa de azulejos possui 1,5 m²
# 
# 
# 
# 
# 
# 
# 
# 3. Rendimento do Taxista:
# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
# preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
# odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
# combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
# média do consumo em km/L e o lucro (líquido) do dia.







# 4. Código de Origem do Produto:
# Escreva um programa que leia o código de origem de um produto e imprima na tela a região
# de sua procedência, conforme a tabela abaixo:
# Observação: caso o código não seja nenhum dos especificados, o produto deve ser
# encarado como “Importado”.








# 5. Média do Aluno com Optativa:
# Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação
# optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve
# ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
# substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e
# mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em
# recuperação, de acordo com as informações abaixo:
# Aprovado: média >= 6.0
# Reprovado: média < 3.0
# Recuperação: média >= 3.0 e < 6.0
# Observação: nota optativa - o estudante decide fazer uma prova extra para melhorar o
# resultado final.

#identificar variável:
#nota1=
#nota2= 
#nota_optativa == -1
#media = 
#resultado = 

#nota_optativa == -1 

 
nota1 = int(input("Digite a primeira nota: ")) 
nota2 = int(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
optativa = input("Teve nota optativa? ")












# 6. Positivo ou Negativo:
# Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o
# valor zero como positivo