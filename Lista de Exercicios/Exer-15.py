""" Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
tela dizendo se está “quente”, “frio” ou “agradável”. """

temp = float(input("Digite a temperatura atual : "))
if temp<25 and temp>0:
    print("Friozinho")
elif temp>31:
    print("Quente")
else:
    print("Agradavel")
    