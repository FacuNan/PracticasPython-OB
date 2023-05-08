#Ejercicio1

a=5
b=6
c=4

if (a <= b):
	c= a 
	b= c + a 
print(b, a)

#Ejercicio2

a = 5 
b = 6
c = 4

if(a <= b):
	c = a 
else:
	a = 6
print(a,b,c)

#Ejercico3

for i in range(10):
	print(i)

#Ejercicio4

for i in range(5, 21, 3):
	print(i)


#Ejercico6

cantidad = input("Ingrese una cantidad: ")
cantidad = int(cantidad)
suma=0

for i in range(cantidad):
	numero = int(input("Ingrese un numero"))
	suma += numero
print(suma)


 


