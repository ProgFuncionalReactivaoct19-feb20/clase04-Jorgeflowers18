"""
    Ejercicio 5
    author: @Jorgeflowers18
"""
paraleloA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]
nombres = ["Luis", "Ángel", "José", "Ana"]
# print con zip para unir las listas, luego map para enviar el zip a la funcion 
# que saca el promedio y filter para obtener solo las tuplas con promedio bajo
print(list(filter(lambda x: x[0] < 5, map(lambda x: (sum(x[0])/3, sum(x[0]), x[1]), 
    list(zip(paraleloA, nombres))))))