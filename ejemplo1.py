"""
    Ejemplo 1
    author: @Jorgeflowers18
"""

listaA = [10, 2, 3, 4]
listaB = ["a", "b", "c", "d"]

# [(2, "d"), (3, "c"), (4, "d"), (10, "a")]

lista2 = sorted(listaA)
lista3 = sorted(listaB, reverse = True)
print(max(list(zip(lista2, lista3))))


