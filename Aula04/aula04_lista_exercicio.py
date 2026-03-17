# 1. Cálculo de Lâmpadas: # Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
# Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. 
# Considere que a potência necessária é de 3 watts por metro quadrado e a cada 3m² existe um bocal para uma lâmpada.

POTENCIA = 3 #VARIAVEL CONSTANTE
lampadas = 0
largura = float(input("Largura: "))
comprimento = float(input("Comprimento: "))

area = largura * comprimento 

lampadas = area/POTENCIA

print(f"São necessárias {lampadas} para iluminar um cômodo de {area} m2")



# 2. Quantidade de Caixas de Azulejos:
# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
# largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
# todas as suas paredes (considere que não será descontada a área ocupada por portas e
# janelas). Cada caixa de azulejos possui 1,5 m²










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

#identificar variaveis:
#nota1=
#nota2= 
#nota_optativa == -1
#media = 
#resultado = 

#nota_optativa == -1 

 
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# optativa = float(input("Teve nota optativa? "))

# if optativa == -1:
#     media = (nota1 + nota2) / 2 
# else:
#     if optativa > nota1:
#         media = (optativa + nota2) / 2
#     else:
#         media = (optativa + nota1) / 2

# if media >= 6.0:
#     resultado = "Aprovado"
# elif media >= 3.0:
#     resultado = "Recuperação"
# else:
#     resultado = "Reprovado"

# print(f"Média final ,{media} resultado: {resultado}")













# 6. Positivo ou Negativo: escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo