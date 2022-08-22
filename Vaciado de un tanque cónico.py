import matplotlib.pyplot as plt
import numpy as np
import time

#datos de entrada
Hi=0.5
hf=0
r=0.003



ang=8*np.pi/180
teta2=np.tan(ang)
teta=np.tan(ang)**2

inv=(1/teta2)

dt=1
g=9.8
t=0
t1=0
h=Hi

h2=0

R=np.tan(ang)*h
R1=np.tan(ang)*h



#definición de listas
Vh=[h]
Vt=[t]
Ah=[h2]
At=[t1]
Rt=[R]



#primera figura
f1 = plt.figure(1)

plot1=plt.plot([R-r,0,2*R,R+r,R-r],[0,Hi,Hi,0,0],"k")


plt.grid()
plt.ylabel("ALtura del agua")


#Calculo Euler
while h>0 and R>0:
    h=(-((r)**2)*((2*g)**(1/2))*(h**(-3/2))*(inv)**2)*dt+h
    R=(np.tan(ang)*h)
    t=t+dt
    plot1=line=plt.plot([R1-R,R1+R],[h,h],"b")
    





    Vh.append(h)
    Vt.append(t)
    Rt.append(R)

    line[0].set_ydata([h])
 
    plt.pause(1/30)
    plt.title("Tiempo = "+str(t))
    
    time.sleep(0.1)
    
    plot2=line=plt.plot([(R1-R)+0.00030,(R1+R)-0.00030],[h,h], "white")
    



#Solución análitica 

while t1<t:
    h2=((25*g*(r**4)*t1**2)**(1/5)/(2*teta**2)**(1/5))
    t1=t1+dt

    Ah.append(h2)
    At.append(t1)
    
list.reverse(Ah)  



#Calculo del porcentaje de error 

Error = (abs((np.array(Vh)-np.array(Ah))))*100


    



#segunda figura
f2 = plt.figure(2)
plt.plot(Vt,Vh)
plt.plot(At,Ah)
plt.grid()
plt.xlabel("Tiempo")
plt.ylabel("ALtura del agua")
plt.title("Análitica vs Numérico")




#Figura del porcentaje


f2 = plt.figure(3)
plt.plot(Vt,Error)
plt.grid()
plt.xlabel("Tiempo")
plt.ylabel("Porcentaje de error (%)")
plt.title("Errores porcentuales")


	  


    
