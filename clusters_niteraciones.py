import numpy as np
import matplotlib.pyplot as plt
import sys

m=sys.argv[1]
n=int(m)

datos=np.loadtxt("data.dat")
sh=np.shape(datos)
x=np.zeros(sh[0])
y=np.zeros(sh[0])
for i in range(sh[0]):
    x[i]=datos[i][0]
    y[i]=datos[i][1]

plt.scatter(x,y)
xcentro_azul=np.zeros(n)
ycentro_azul=np.zeros(n)
xcentro_rojo=np.zeros(n)
ycentro_rojo=np.zeros(n)
xcentro_azul[0]=(15*np.random.random())
ycentro_azul[0]=(15*np.random.random())
xcentro_rojo[0]=(15*np.random.random())
ycentro_rojo[0]=(15*np.random.random())

colores=np.zeros(sh[0])
distancia1=np.zeros(sh[0])
distancia2=np.zeros(sh[0])
for j in range(n-1):                 
   for i in range(sh[0]):
        distancia1[i]=np.sqrt(((x[i]-xcentro_azul[j])**2)+((y[i]-ycentro_azul[j])**2))
        distancia2[i]=np.sqrt(((x[i]-xcentro_rojo[j])**2)+((y[i]-ycentro_rojo[j])**2))
        if(distancia1[i]<distancia2[i]):
            colores[i]=0
        else:
            colores[i]=1
            
   puntos_azules=np.where(colores==0)
   xazules=x[puntos_azules]
   yazules=y[puntos_azules]
   if (np.size(xazules)!= 0):
     xcentro_azul[j+1]=sum(xazules)/np.size(xazules)
   if (np.size(yazules)!= 0):
     ycentro_azul[j+1]=sum(yazules)/np.size(yazules)        
   puntos_rojos=np.where(colores==1)
   xrojos=x[puntos_rojos]
   yrojos=y[puntos_rojos]
   xcentro_rojo[j+1]=sum(xrojos)/np.size(xrojos)
   ycentro_rojo[j+1]=sum(yrojos)/np.size(yrojos)

   plt.scatter(xcentro_azul[j+1],ycentro_azul[j+1], c='b', s=90)
   plt.scatter(xcentro_rojo[j+1],ycentro_rojo[j+1], c='r', s=90)
   plt.scatter(xazules,yazules,c='b')
   plt.scatter(xrojos,yrojos, c='r')

   plt.show()
