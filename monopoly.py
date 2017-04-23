#!/usr/bin/env python
from random import randint

import matplotlib.pyplot as pyplot

def rollTwoDice():
	return randint(1,6) + randint(1,6)

def plot(x,y):
	pyplot.bar(x,y)
	pyplot.show()


nVeces    = 100000
nCasillas = 40
contador  = [0.]*nCasillas
posicionActual = 0


print ("Tirando los dados " + str(nVeces) + " veces")


for i in range(nVeces):

	#Tirar dados
	valorDados = rollTwoDice()
	
	#Mover posicion
	posicionActual += valorDados

	#Corregir posicion si se da la vuelta
	if posicionActual >= nCasillas :
		posicionActual -= nCasillas

	#Aumentar el contador de la casilla
	contador[posicionActual] += 1 


for i in range(len(contador)):
	contador[i] = contador[i] / float(nVeces)


print ("Probabilidades de caer en cada casilla:")

for i in range(nCasillas):
	print("P(" + str(i) + ")= " + str(contador[i]))

plot(range(len(contador)),contador)
	



