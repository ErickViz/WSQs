def texto(x):
	highmpg=0
	citympg=0
	pricemid=0
	c=0
	for line in x:
		c=c+1
		if(c%2==1):
			price= line[42:46]
			pricef= float(price)
			pricemid= pricemid+pricef
			city= line[52:54]
			cityf= float(city)
			citympg= citympg+cityf
			high= line[55:57]
			highf= float(high)
			highmpg= highmpg+highf
	autos= c/2
	promedio_p= pricemid/autos
	promedio_c= citympg/autos
	promedio_h= highmpg/autos
	return(promedio_p, promedio_c, promedio_h)

txt= open("93cars.dat.txt")
(p,c,h)= texto(txt)
p=str(p)
c= str(c)
h= str(h)
print("El promedio del precio (en $1000) es: ", p[0:5])
print("El promedio de MPG en la ciudad es: ", c[0:5])
print("El promedio de MPG en la autopista es: ", h[0:5])
