""" Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
conversão. """
conversao = input("Digite F (De C° para F°) ou C (De F° para C°)")
temp = int(input("Digite a temperatura : "))
if conversao == "f":
    print(f"A temperatura em F° é {(temp*9)/5}")
else:
    print(f"A temperatura em F° é {temp - 32 * 5/9}")

