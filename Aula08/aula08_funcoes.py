# import time

# 1. DEFINIÇÃO da função
# def dar_boas_vindas():
#     print("-"*40)
#     print("  Bem-vindo ao nosso aplicativo! 😀")
#     print("-"*40)

# # 2. CHAMADA da função
# # O código abaixo só será executado se você "chamar" a função pelo nome:

# print("Início do programa.")
# print('Por favor, aguarde...')
# time.sleep(2)  # Simula uma pausa
# dar_boas_vindas()  # <-- Isso executa o código dentro da função
# print("Meio do programa.")
# dar_boas_vindas()  # <-- Podemos chamar de novo!
# print("Fim do programa.")

# # 'nome_da_pessoa' é um PARÂMETRO.
# # É uma variável que só existe dentro da função.
# def boas_vindas_personalizado(nome_da_pessoa):
#     print("-"*40)
#     print(f"Olá, {nome_da_pessoa}! Seja bem-vindo(a)! 😀")
#     print("-"*40)

import random

def gerar_dados(qtd, min_valor, max_valor):
    """
     Gera uma LISTA de números aleatórios.
    - qtd: quantos números queremos na lista                        #DOCSTRING
    - min_val: o valor mínimo (inclusivo)
    - max_val: o valor máximo (inclusivo)
    """
    lista_de_dados = [random.randint(min_valor, max_valor) for _ in range(qtd)]
    return lista_de_dados 

dados_aleatorios = gerar_dados(5, 1, 100)   #Gera 5 números entre 1 e 100
print(f"Dados gerados: {dados_aleatorios}")