#!/usr/bin/env python
from random import randint

import matplotlib.pyplot as pyplot


def plot(x,y):
	pyplot.bar(x,y)
	pyplot.show()


nDado1	  = 0
nDado2    = 0
bDadosIguales = False
vecesCarcel = 0
nVeces    = 100000
nCasillas = 40
contador  = [0.]*nCasillas
posicionActual = 0
bCarcel = False


print ("Tirando los dados " + str(nVeces) + " veces")


for i in range(nVeces):

	#Tirar dados
	bDadosIguales = False
	nDado1 = randint(1,6) 
	nDado2 = randint(1,6)
	
	valorDados = nDado1 + nDado2

	#Comprobar dados dobles
	if nDado1 == nDado2:
		bDadosIguales = True
	
	
	#Mover posicion si:
	#	Si se esta en la carcel, mover si dados dobles
	#	Si no se esta en la carcel
	#	Si se esta en la carcel y es la tercera tirada
	if (bCarcel and bDadosIguales) or (not bCarcel) or (bCarcel and vecesCarcel>=3) : 
		posicionActual += valorDados
		bCarcel = False
		bVecesCarcel = 0

	#Sumar tiradas estando en la carcel
	if bCarcel and not bDadosIguales:
		bVecesCarcel +=1

	#Corregir posicion si se da la vuelta
	if posicionActual >= nCasillas :
		posicionActual -= nCasillas

	#Sumar uno al contador de la casilla
	#Si casilla "ir a carcel", cambiar posicion a carcel
	if posicionActual == 30:
		contador[posicionActual] += 1 
		posicionActual = 10
		bCarcel = True 
	
	else:
		contador[posicionActual] += 1 


for i in range(len(contador)):
	contador[i] = contador[i] / float(nVeces)


print ("Probabilidades de caer en cada casilla:")

for i in range(nCasillas):
	print("P(" + str(i) + ")= " + str(contador[i]))

plot(range(len(contador)),contador)
	



