import matplotlib.pyplot as plt 

Rt=0.5 

Ro=0.05 

g=9.8 

ho=1.8 

H=2 

dt=1 

 

t=0 

h=ho 

 

plt.plot([0,0,1,1,1.1,1.1,0],[0,2,2,0.1,0.1,0,0],"k") 

linea=plt.plot([0,1],[ho,ho],"b") 

plt.grid() 

 

while h>0: 

    h=(-(Ro/Rt)**2*(2*g*h)**(1/2))*dt+h 

    t=t+dt 

    linea[0].set_ydata([h,h]) 

    plt.pause(1/24) 

    plt.title("Tiempo = "+str(t)) 