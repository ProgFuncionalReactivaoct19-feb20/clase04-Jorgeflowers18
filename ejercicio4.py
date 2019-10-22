"""
    Ejercicio 4
    author: @Jorgeflowers18
"""
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]

f = lambda x: (x[0] + x[1] + x[2])/3

print(list(zip(map(f, paraleloA),nombres)))