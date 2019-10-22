"""
    Ejercicio 5
    author: @Jorgeflowers18
"""
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]
# funcion para conseguir el promedio
f = lambda x: (x[0] + x[1] + x[2])/3
# prints enviando la informacion a través de maps para enviar argumentos a las funciones
print(list(zip(map(f, paraleloA),nombres)))
print(max(list(zip(map(f, paraleloA),nombres))))
print(list(sorted(zip(map(f, paraleloA), nombres), key = lambda x: x[1])))

