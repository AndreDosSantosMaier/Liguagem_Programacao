""" Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os
códigos utilizados são:
 1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)

1 - Andre
2 - Pedro
3 - Davi
4 - Gabriel
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
a. O total de votos para cada candidato;
b. O total de votos nulos;
c. O total de votos em branco;
d. A percentagem de votos nulos sobre o total de votos;
e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o
valor zero """
v1 = v2 = v3 = v4 = v5 = v6 = 0
for i in range(5):
    voto = int(input("Digite seu voto : "))
    if voto == 1:
        v1+=1
    elif voto == 2:
        v2+=1
    if voto == 3:
        v3+=1
    if voto == 4:
        v4+=1
    if voto == 5:
        v5+=1
    if voto == 6:
        v6+=1
print(f"o total de votos para o Andre é {v1}, para Pedro é {v2}, para Davi é {v3} e para Gabriel {v4}")
print(f"o total de votos nulos é {v5}")
print(f"o total de votos em branco é {v6}")
print(f"a procentagem de votos brancos é : {(100/5*v6)}%")
print(f"a procentagem de votos nulos é : {(100/5*v5)}%")

