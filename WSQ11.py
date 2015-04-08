# WSQs
#Erick Iván Vizcarra Hernandez
def palindromo(x):
	a=str(x)
	b=a[::-1]
	c=int(b)
	if(x==c):
		return True
	else:
		return False
nonlycherels= 0
lycherels= 0
npalindromos= 0
x=int(input("Dame un numero pequeño: "))
y=int(input("Dame un numero grande: "))
print("Numeros analizados desde",x," hasta ",y)
for d in range(x,y+1):
	d1=palindromo(d)
	if(d1==False):
		d2 = 0
		p = False
		candidato = c
		while(d2<30 and p==False):
			d2 = d2 + 1
			d3 = str(candidato)
			r = d3[::-1]
			r1 = int(r)
			candidato = candidato + r1
			p = palindromo(candidato)
		if(p==True):
			nonlycherels = nonlycherels + 1
		if(d2==30 and p==False):
			Lycherels = Lycherels + 1
	else:
		npalindromos = npalindromos + 1
print("Palindromos: ", npalindromos)
print("Non-Lycherels: ", nonlycherels)
print("Lycherels: ", lycherels)
