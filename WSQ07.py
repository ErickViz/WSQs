#Erick Iván Vizcarra Hernández
#Sum of numbers
print("Este programa calcula la suma del rango entre dos números")
print()
x=int(input("Dame un número pequeño: "))
y=int(input("Dame un numero grande: "))

if(y<x):
	print("¡Los numeros no estan correctamente definidos definidos!")
sum=0
z=y-x+1
i=0
while i!=z:
	sum=sum+x
	x=x+1
	i=i+1
print("El resultado de sumar los numeros es: ", sum)
