""" Escreve um Programa que leia uma lista com no minino 5 itens, contendo itens repetidos e mostre
os itens repetidos.  """ 
aux=0
a = ["andre","pedro","yuri","andre","gabriel"]
for i in (a):
    b = a.count(i)
    if (b > 1):
        aux=1
if aux==0:
    print("Nao ta repetida")
else:
    print("Ta repetida")
