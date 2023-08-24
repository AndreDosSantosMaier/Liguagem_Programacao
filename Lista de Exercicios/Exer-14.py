""" Escreva um Programa que verifique se um elemento está na lista e verifique a posição exata dele da lista """

a = [1,2,3,"andre",5,6]
if "andre" in a:
    print("Esta presente na lista")
    print(a.index("andre"))
else:
    print("Não esta presente na lista")

