contador=0
contador1=0
for x in range(10):
    num=int(input("ingrese un numero "))
    if num%5==0:
        contador=contador+1
    if num%3==0:
        contador1=contador1+1
print("los numeros ingresados divisibles por 5 son: ",contador)
print("los numeros ingresados divisibles por 3 son: ",contador1)

        
