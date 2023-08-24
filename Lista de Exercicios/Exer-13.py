""" Escreva um Programa que leia uma lista de 5 números inteiros, mostre a soma deles. """

numeros = []
soma = 0
for i in range (5):
    numeros.append(int(input("Digite o numero") ))
for i in numeros:
    soma += i
print(soma)