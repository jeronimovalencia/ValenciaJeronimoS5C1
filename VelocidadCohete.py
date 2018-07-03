import numpy as np
import matplotlib.pyplot as plt

tiempos = np.array([2.,5.,9.,10.,1.])
velocidades = np.array([45.948, -119.985, 231.497,-123.2,10.09])
vel = np.copy(velocidades)
solution = np.array([])
matriz = np.empty([np.size(tiempos),np.size(velocidades)])

for i in range(np.size(tiempos)):
	for j in range(np.size(velocidades)):
		matriz[i,j] = tiempos[i]**(np.size(tiempos)-1-j)


#------------------------------------------------------------------------------
#Eliminacion Gaussiana
def indice(M,i):
	N = np.shape(M)[0]
	indice = -1
	for j in range(i,N):
		if(M[j,i] != 0): 
			indice = j
			break
	return indice

def reduccion(M,B):
	N = np.shape(M)[0]

	for j in range(N): 		
		if(M[j,j]==0):
			temp = np.copy(M[j])
			if(indice(M,j) == -1): 
				return "No se puede hacer el metodo de eliminacion gaussiana"
				break
			else:
				#Falta cambiar las filas en caso de que encuentre un elemento no 0
				M[j] = np.copy(M[indice(M,j)])
				M[indice(M,j)] = np.copy(temp)
	
		temp1 = np.array(M[j]*(1.0)/M[j,j])
		temp2 = np.array(B[j]*(1.0)/M[j,j])
		M[j] = temp1
		B[j] = temp2

		for i in range(j+1,N):
			temporal1 = np.array(M[i] - M[i,j]*M[j])
			temporal2 = np.array(B[i] - M[i,j]*B[j])
			M[i] = temporal1
			B[i] = temporal2
	return M,B

def eliminacionGaussiana(A,b):	
	M,B = reduccion(A,b)
	sol = np.zeros(np.shape(M)[0])	
	for i in range(np.shape(M)[0]):
		num = B[-1-i]
		for j in range(np.shape(M)[0]):
			num = num - M[-1-i,j]*sol[j]
		sol[-1-i] = num
	
	return sol
#------------------------------------------------------------------------------
def polinomio(x):
	sol = eliminacionGaussiana(matriz,velocidades)
	solution = np.copy(sol)
	
	poli = 0
	for i in range(np.size(sol)):
		poli = poli + (1.)*np.array([sol[i]])*x**(np.size(sol)-1-i)
	return poli, ("a_1","=",sol[0],"a_2","=",sol[1],"a_3","=",sol[2])

x = np.linspace(0,50,1000)

plt.figure()
plt.plot(x,polinomio(x)[0])
plt.scatter(tiempos,vel)
plt.show()






