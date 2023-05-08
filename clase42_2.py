# Inicializamos las variables para la suma, el contador y el valor ingresado por el usuario
suma = 0
contador = 0
valor = 0

# Pedimos al usuario que ingrese 10 valores flotantes y los sumamos
while contador < 10:
    valor = float(input("Ingrese un valor flotante: "))
    suma = suma + valor
    contador = contador + 1

# Calculamos el promedio dividiendo la suma por la cantidad de valores
promedio = suma / 10

# Mostramos los resultados al usuario
print("La suma total de los valores es:", suma)
print("El promedio de los valores es:", promedio)
