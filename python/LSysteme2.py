# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:10:01 2014

@author: Quentin
"""
#Fractales L-Systèmes
def dessinerpix(xpos,ypos,taille):
    import pixel as px  
    xmax = int(2*max(xpos) + 1) #on choisit les positions de la tortue les plus éloignées
    ymax = int(2*max(ypos) + 1)
    departx = xmax/2 #la position (0,0) correspond au coin gauche dans pixel, donc il faudra décaler tout les pixels pour qu'ils soient au bon endroit
    departy = ymax/2
    px.initialiser(xmax,ymax,taille) #on définit la fenêtre à partir des positions les plus éloignées pour voir tout le dessin
    for k in range(len(xpos)) : #on parcourt la liste des positions
        px.marquer(int(xpos[k]) + departx , departy - int(ypos[k])) #on prend la partie entière de chaque position car les coordonnées des pixels sont forcéments entières
    px.afficher() #on affiche
    
def dessinerPosition(chaine,distance,angle,position,direction) :
    import turtle as tt
    xpos= []
    ypos= []
    L= []
    tt.tracer(0)
    tt.penup() #on "lève le crayon" pour ne pas dessiner lorsque l'on initialise la tortue
    tt.setheading(direction) 
    tt.goto(position) #on commence à la position voulue et avec la direction voulue
    tt.pendown()
    tt.speed(0) #on prend la vitesse maximale de la tortue
    tt.hideturtle() #on cache le curseur
    for k in chaine :
        if k == 'F' :
            tt.fd(distance) #on fait un trait simple
        elif k == 'f' : #on "lève le crayon" pour avancer sans tracer
            tt.penup()
            tt.fd(distance)
            tt.pendown() 
        elif k == '+' : #on tourne la tortue à gauche
            tt.left(angle)
        elif k == '-' :
            tt.right(angle) #on tourne à droite
        elif k == '|' : #on tourne de 180°
            tt.right(180)
        elif k == '[' : #on enregistre la position et la direction dans une liste
            x,y = tt.pos()
            d=tt.heading()
            L.append((x,y,d)) #tuple composé de la position (x,y) et de la direction (d)
        elif k == ']' : #on déplace à la dernière position enregistrée dans la liste
            tt.penup()
            x,y,d = L.pop() #on sort la dernière position enregistrée et on l'affecte à x,y,d
            tt.goto((x,y)) #on déplace la tortue à la position x,y
            tt.setheading(d) #et on lui donne la direction d
            tt.pendown()
        (x,y)=tt.pos() #on enregistre chacune des positions de la tortue
        xpos.append(x) #puis on les place dans une liste
        ypos.append(y)
    xmax = int(2*max(xpos) + 1) #on choisit les positions de la tortue les plus éloignées
    ymax = int(2*max(ypos) + 1)
    tt.screensize(xmax,ymax)
    tt.setup(xmax,ymax,starty=-1)
    tt.update()
    return xpos,ypos #on renvoie la liste des positions
    
def LsystemPixel(axiome,regles,niveau=1,distance=10,angle=90,position=(0,0),direction=90) :
    
    from LSysteme3 import dessinerpix
    import turtle as tt
    chaine=construire_chaine(axiome,regles,niveau) #on construit la chaine au niveau voulu
    (xpos,ypos) = dessinerPosition(chaine,distance,angle,position,direction) #puis on la dessine
    dessinerpix(xpos,ypos,distance//2) #on dessine à partir des positions de la tortue
    tt.mainloop()


LsystemPixel(axiome ="X", regles = [("X","F[+X]F[-X]+X"),("F","FF")], niveau=5, angle= 20)

#print construire_chaine(axiome ="X", regles = [("X","F[+X]F[-X]+X"),("F","FF")], niveau=2)   
"""axiome = raw_input("Entrez l'axiome de depart :")
regles = input("Entrez la liste de regle voulue :")
niveau = input("Entrez le niveau voulue (par defaut 1) :")
distance = input("Entrez la distance de trait voulue (par defaut 10) :")
angle = input("Entrez l'angle voulue (par defaut 90) :")
position = input("Entrez la position de depart (en tuple, par defaut (0,0)) :")
direction = input("Entrez la direction de depart (par defaut 0) :")

Lsystem(axiome,regles,niveau,distance, angle, position, direction)
input("Appuyez sur une touche pour terminer...")"""