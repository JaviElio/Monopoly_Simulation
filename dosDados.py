#!/usr/bin/env python
from random import randint

def rollTwoDice():
	return randint(1,6) + randint(1,6)

contador = [0.]*12
nVeces   = 1000

for i in range(nVeces):
	valorDados = rollTwoDice()
	
	contador[valorDados-1] +=1
	
for i in range(len(contador)):
	contador[i] /= float(nVeces)

print ("Probabilidad de obtener el valor tirando dos dados:")

for i in range(len(contador)):
	print("P("+str(i+1)+")= "+str(contador[i]))

