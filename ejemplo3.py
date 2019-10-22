"""
    Ejemplo 3
    author: @Jorgeflowers18
"""

lista = [(100, 2), (20, 4), (30,1)]
lista2 = ["b", "a", "c"]
f = lambda x: x.upper()



print(list(zip(sorted(lista), sorted(map(f, lista2), reverse = True))))