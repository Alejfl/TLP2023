# Inicializamos las variables para la suma y el promedio
suma = 0
promedio = 0

# Pedimos al usuario que ingrese 10 valores flotantes y los sumamos
for i in range(10):
    valor = float(input("Ingrese un valor flotante: "))
    suma = suma + valor

# Calculamos el promedio dividiendo la suma por la cantidad de valores
promedio = suma / 10

# Mostramos los resultados al usuario
print("La suma total de los valores es:", suma)
print("El promedio de los valores es:", promedio)
