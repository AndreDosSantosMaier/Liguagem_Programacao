""" Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
Euros. """

reais = float(input("Digite o valor em reais : "))
print(f"O valor em euros é : {reais/5.27}")
print(f"O valor em dolar é : {reais/5.41}")