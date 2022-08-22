"""
Created on Fri Nov 12 13:37:57 2021

@author: Martín
"""

from vpython import *
import time

#Funcion para modificar la direccion del movimiento
def acc():
    dr_right = ball.pos - wall_right.pos 
    force_right = -spring_right.constant*(mag(dr_right) - length - fric)*norm(dr_right)
    
    dr_left = ball.pos - wall_left.pos
    force_left = -spring_left.constant*(mag(dr_left) - length - fric)*norm(dr_left)
    
    return (force_right+force_left) / ball.mass
#Funciones para modificar los parametros 
def change_radius(widget):
    print('radius:', widget.value)
    ball.radius = widget.value 

def change_weight(widget):
    print('weight:', widget.value)
    ball.mass = widget.value 

def change_g(widget):
    print('g:', widget.value)
    ball.mass = widget.value 
    
def change_fric(widget):
    print('fric:', widget.value)
    ball.mass = widget.value        
    
def change_spring1(widget):
    print('spring1:', widget.value)
    spring_right.constant = widget.value     
    
    
def change_spring2(widget):
    print('spring2:', widget.value)
    spring_left.constant = widget.value
  
  

#Información de las diferentes variables


fric = 0.01
massball = 20
g=2
radius = 5
spring1=1.2
spring2=1.2

weight=g*massball


#Información de posición y velocidad 

length = 30.

posix=2
posiy=0

velx=0.1
vely=-2

posy1=0
posy2=0


#Creación de los objetos visuales

scene2 = canvas(title='Masa con dos sistemas', width=400, height=200, center=vector(0,0,0), background=color.white) 

ball = sphere(pos=vector(posix,posiy,0), velocity=vector(velx,vely,0), radius=radius, mass=weight, color=color.red)

wall_right = box(pos=vector(length,posy1,0), size=vector(0.2, 5, 5), color=color.yellow)
wall_left = box(pos=vector(-length,posy2,0), size=vector(0.2, 5, 5), color=color.yellow)

spring_right = helix(pos=wall_right.pos, axis=ball.pos-wall_right.pos, constant=spring1, coils=10, thickness=0.2, radius=1, color=color.blue)
spring_left = helix(pos=wall_left.pos, axis=ball.pos-wall_left.pos, constant=spring2, coils=10, thickness=0.2, radius=1, color=color.blue)


#información de los sliders

scene2.caption = "Peso: Radio: Gravedad: Fricción: Resorte derecho: Resorte izquierdo"

sl1 = slider(min=0.3, max=10, value=weight, length=110, bind=change_weight, right=15, vertical=True)

sl2 = slider(min=0.3, max=10, value=radius,   length=110, bind=change_radius,   right=15, vertical=True)

sl3 = slider(min=0.3, max=10, value=g,   length=110, bind=change_g,   right=15, vertical=True)

sl4 = slider(min=0.01, max=1, value=fric,   length=110, bind=change_fric,   right=15, vertical=True)

sl5 = slider(min=0.01, max=10, value=spring1,   length=110, bind=change_spring1,   right=15, vertical=True)

sl6 = slider(min=0.01, max=10, value=spring2,   length=110, bind=change_spring2,   right=15, vertical=True)


#Traza del movimiento 
ball.trail = curve(color=ball.color)


#Loop principal
t = 0
dt = 0.01

time.sleep(5)
while t < 200:

    rate(500)
    ball.velocity = ball.velocity + acc() * dt
    ball.pos = ball.pos + ball.velocity  * dt
    spring_right.axis = ball.pos - wall_right.pos
    spring_left.axis = ball.pos - wall_left.pos
    ball.trail.append(pos=ball.pos)
    t = t + dt