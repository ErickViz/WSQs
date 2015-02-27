# WSQ09
#Erick Iván Vizcarra Hernández

def factorial(x):
	a=x
	c=1
	while(a>1):
		c = c*a
		a = a-1
	return c
z='s'
while(z=='s'):
	x=int(input("Dame un numero: "))
	a=factorial(x)
	print("El factorial de",x,"es: ",a)

	z= input("Quieres probar otro numero? ")

print("Bien, que tengas un buen dia :)")	
