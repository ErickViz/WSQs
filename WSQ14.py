#Erick Vizcarra
#WSQ14
def calculate_e(x):
	e=0
	y=0
	c=1
	for y in range(100000):
		y= e
		e= e+1/c
		print("Ahora e es", e,"por iteracion", y)
		e2 = 1+e
		c=c*(c+1)
		if exactitud(y,e,x):
			break
	return e
def exactitud (x,y,z):
	import math
	x1= x* pow(10,z)
	x1= math.trunc(x1)
	x1= x1/pow(10,z)
	y1= y* pow(10,z)
	y1= math.trunc(y1)
	y1= y1/pow(10,z)
	return(x1==y1)
x=float(input("Dame la exactitud: "))
a= calculate_e(x)
print(a)
