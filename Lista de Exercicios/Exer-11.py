""" Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
ao final mostrar seu nome e salário final calculado. """
nome = input("Digite o seu nome : ")
numeroh = int(input("Digite o numero de horas trabalhadas : "))
valorh = float(input("Digite o valor das horas : "))
salario = numeroh*valorh
print(f"O salario final é {salario}")
print(f"O desconto do INSS é de : {salario*0.02}")
print(f"O salario final é {salario*0.98}")