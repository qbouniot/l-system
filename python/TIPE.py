# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 19:06:16 2013

@author: Quentin
"""

from turtle import*

up()
goto(0,-320)
setheading(90)
down()
ht()

def lecture(L,d):
    P=[]
    for k in L:
        if k=="F":
            forward(5)
        elif k=="+":
            left(d)
        elif k=="-":
            right(d)
        elif k=="[":
            x=position()
            y=heading()
            P.append((x,y))
        elif k=="]":
            x,y=P.pop()
            goto(x)
            setheading(y)

def axiome1(L):
    i=0
    while i<len(L):
        if L[i]=="F":
            L.insert(i+1,"+")
            L.insert(i+2,"F")
            L.insert(i+3,"-")
            L.insert(i+4,"F")
            L.insert(i+5,"-")
            L.insert(i+6,"F")
            L.insert(i+7,"F")
            L.insert(i+8,"+")
            L.insert(i+9,"F")
            L.insert(i+10,"+")
            L.insert(i+11,"F")
            L.insert(i+12,"-")
            L.insert(i+13,"F")
            i+=13
        i+=1
    return L

def affichage1(n):
    L=["F","+","F","+","F","+","F"]
    for j in range(n):
        L=axiome1(L)
    lecture(L,90)

def ax2(L):
    i=0
    while i<len(L):
        if L[i]=="F":
            L.insert(i+1,"[")
            L.insert(i+2,"+")
            L.insert(i+3,"F")
            L.insert(i+4,"]")
            L.insert(i+5,"F")
            L.insert(i+6,"[")
            L.insert(i+7,"-")
            L.insert(i+8,"F")
            L.insert(i+9,"]")
            L.insert(i+10,"F")
            i+=10
        i+=1
    return L
    
def affichage2(n):
    L=["F"]
    for j in range(n):
        L=ax2(L)
    lecture(L,25.7)
    
def trans():
    L=["F","[","+","F","]","F","[","-","F","]","F"]
    lecture(L,25.7)
    
def dessinercouleur(chaine,motif,distance,angle,position,direction):
    import turtle as tt
    #import LSysteme as ls
    L= []
    xpos= []
    ypos= []
    l1 = len(chaine)
    l2 = len(motif)
    tt.tracer(0)
    tt.penup() #on "lève le crayon" pour ne pas dessiner lorsque l'on initialise la tortue
    tt.setheading(direction) 
    tt.goto(position) #on commence à la position voulue et avec la direction voulue
    tt.pendown()
    tt.speed(0) #on prend la vitesse maximale de la tortue
    tt.hideturtle() #on cache le curseur
    k=0
    while k < l1 :
        if chaine[k] == motif[0]:
            b = True
            if k+l2-1 < l1:
                for m in range(l2):
                    if chaine[k+m] != motif[m]:
                        b = False
                if b:
                    tt.color((1,0,0))
                    pos = tt.pos()
                    dir = tt.heading()
                    ls.dessiner(motif,distance,angle,pos,dir,False)
                    tt.color((0,0,0))
                    k+=l2
        if chaine[k] == 'F' :
            tt.fd(distance) #on fait un trait simple
        elif chaine[k] == 'f' : #on "lève le crayon" pour avancer sans tracer
            tt.penup()
            tt.fd(distance)
            tt.pendown() 
        elif chaine[k] == '+' : #on tourne la tortue à gauche
            tt.left(angle)
        elif chaine[k] == '-' :
            tt.right(angle) #on tourne à droite
        elif chaine[k] == '|' : #on tourne de 180°
            tt.right(180)
        elif chaine[k] == '[' : #on enregistre la position et la direction dans une liste
            x,y = tt.pos()
            d=tt.heading()
            L.append((x,y,d)) #tuple composé de la position (x,y) et de la direction (d)
        elif chaine[k] == ']' : #on déplace à la dernière position enregistrée dans la liste
            tt.penup()
            x,y,d = L.pop() #on sort la dernière position enregistrée et on l'affecte à x,y,d
            tt.goto((x,y)) #on déplace la tortue à la position x,y
            tt.setheading(d) #et on lui donne la direction d
            tt.pendown()
        (x,y)=tt.pos() #on enregistre chacune des positions de la tortue
        xpos.append(x) #puis on les place dans une liste
        ypos.append(y)
        k+=1
    xmax = int(2*max(xpos) + 1) #on choisit les positions de la tortue les plus éloignées
    ymax = int(2*max(ypos) + 1)
    tt.screensize(xmax,ymax)
    tt.setup(xmax,ymax,starty=(-5))
    tt.update()