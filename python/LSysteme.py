# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:10:01 2014

@author: Quentin
"""
##################################TIPE : L-Systèmes - 1ère année ###########################
####################################### Fonctions 2D #######################################

def construire_chaine(axiome,regles,niveau) :
    """Fonction qui construit la chaine de caractère au niveau voulu en fonction de l'axiome de départ
    et de la liste de règle"""
    l = axiome
    P = proba(regles) 
    n2 = len(P)
    for n in range(niveau):
        L='' #Chaine de transition sur laquelle on effectue les changements au rang i+1
        for k in l : # On parcourt la liste au rang i
            b = False #Booléen qui indique si un changement a été effectué sur la chaine L)
            for p in range(n2) :
                i=tirage(P[p]) #à chaque niveau on tire une règle au hasard en fonction de leur probabilité
                old,new = regles[i+p][0],regles[i+p][1] #on applique la règle tirée
                if k == old :
                    L += new #On regarde si les éléments de l correspondent aux règles
                    b = True
#Et on change le booléen pour indiquer qu'il y a eu un changement
            if b == False : 
                L += k 
#Si l'élément ne correspond à aucune règle, on le met inchangé dans la chaine de transition
        l = L #On remplace la chaine initiale par la nouvelle chaine
    return l

def proba(regles):
    """Fonction qui crée une liste contenant les probabilités des règles ayant le même prédécesseur"""
    P=[]
    n = len(regles)
    for p in range(n) : # on parcourt tous les éléments de la liste
        b = False #Booléen qui vérifie une liste de probabilité a déjà été créée pour ce prédécesseur       
        for k in range(p):
            if regles[k][0] == regles[p][0]: # on parcourt les éléments précédent
                b = True
        if not b: #Si il n'y a pas eu de liste pour ce prédécesseur
            q=p+1
            Q = [regles[p][2]] #on crée une liste avec la probabilité de la p-ième règle
            while q < n :
                if regles[q][0] == regles[p][0] : 
                    Q.append(regles[q][2])
                    # si la règle a le même prédécesseur on ajoute la probabilité à la liste
                q+=1
            P.append(Q)
    return P
    
def tirage(L):
    """Fonction qui tire aléatoirement un élément d'une liste pondérée"""
    import random as rd    
    n= rd.random() #on tire un nombre au hasard entre 0 et 1
    k=0
    s = 0
    l=len(L)
    while k < l -1 :
        if s <= n and n <= s+L[k] : # on regarde dans quel intervalle des probabilités se situe n
            break
        s+= L[k]
        k+= 1
    return k # on retourne la position de l'élément tiré

def dessiner(chaine,distance,angle,position,direction,xpos,ypos) :
    """Fonction qui dessine la chaine qu'on lui donne en entrée"""    
    import turtle as tt
    import random as rd
    L = []
    wasdown=tt.isdown() # on vérifie si il faut dessiner ou pas
    tt.penup()
    #on "lève le crayon" pour ne pas dessiner lorsque l'on initialise la tortue
    tt.setheading(direction) 
    tt.goto(position) #on commence à la position voulue et avec la direction voulue
    if wasdown:
        tt.pendown()
    tt.speed(0) #on prend la vitesse maximale de la tortue
    tt.hideturtle() #on cache le curseur
    for k in chaine :
        # On peut définir l'angle avec une borne inférieure et une borne supérieure
        if not tt.fill():        
            if type(angle) == tuple: 
                theta = rd.uniform(angle[0],angle[1])
            else:
                theta = angle
        if k == 'F' :            
            tt.fd(distance) #on fait un trait simple
        elif k == 'f' : #on "lève le crayon" pour avancer sans tracer
            tt.penup()
            tt.fd(distance)
            if wasdown:
                tt.pendown() 
        elif k == '+' : #on tourne la tortue à gauche
            tt.left(theta)
        elif k == '-' :
            tt.right(theta) #on tourne à droite
        elif k == '|' : #on tourne de 180°
            tt.right(180)
        elif k == '[' : #on enregistre la position et la direction dans une liste
            x,y = tt.pos()
            d=tt.heading()
            L.append((x,y,d))
#tuple composé de la position (x,y) et de la direction (d)     
        elif k == ']' : #on déplace à la dernière position enregistrée dans la liste
            tt.penup()
            x,y,d = L.pop()
            #on sort la dernière position enregistrée et on l'affecte à x,y,d
            tt.goto((x,y)) #on déplace la tortue à la position x,y
            tt.setheading(d) #et on lui donne la direction d
            if wasdown:
                tt.pendown()
        elif k == '{':
            tt.fillcolor('green')
            tt.begin_fill()
        elif k == '}':
                tt.end_fill()
        (x,y)=tt.pos()
        xpos.append(x) #liste des positions en x
        ypos.append(y) #et des positions en y
    return xpos,ypos #on renvoie les positions

def screen(xpos,ypos,distance,tps):
    """ Fonction qui adapte la fenêtre affichée à la taille du dessin"""
    import turtle as tt
    Mx = int(max(xpos))
    mx = int(min(xpos))
    My = int(max(ypos))
    my = int(min(ypos)) 
    xmax = max(Mx,mx)
    ymax = max(My,my)
    Max = int(max(xmax,ymax))+1 #on définit la valeur de la position la plus éloignée
    tt.setworldcoordinates(-Max,-Max,Max,Max) #on réorganise la fenêtre en fonction de cette position
    tt.update() #on réactualise l'écran
    tt.mainloop(tps) #on laisse tourner la tortue pour ne pas faire planter le programme

def Lsystem(axiome,regles,niveau=1,distance=10,angle=90,position=(0,0),direction=90,tps=0) :
    """Fonction qui dessine le L-système qu'on lui donne en entrée"""
    import turtle as tt
    import random as rd
    tt.mode('world')
    tt.tracer(0) #on enlève les animations
    xpos=[]
    ypos=[]
    chaine=construire_chaine(axiome,regles,niveau) #on construit la chaine au niveau voulu
    xpos,ypos = dessiner(chaine,distance,angle,position,direction,xpos,ypos) #puis on la dessine
    screen(xpos,ypos,distance,tps) #on affiche la fenêtre avec les bonnes coordonnées


    
#Plante 1
#Lsystem(axiome ="X", regles = [("X","F[+X]F[-X]+X",1),("F","FF",1)], niveau=7, angle= 20)

#Plante 2
#Lsystem(axiome ="X", regles = [("X","F-[[X]+X]+F[+FX]-X",1),("F","FF",1)], niveau=5, angle= 22.5)

# Plante feuille sans aléatoire
#Lsystem(axiome ="B", regles = [("X","FX",1),("B","[-F{[-f+f+f][+f-f-f]}]FX[[-B][+B]]FX[+FXB]-B",1)], niveau=4, angle= 20)

#Plante aléatoire 1
#Lsystem(axiome ="F", regles = [("F","F[+F]F[-F]F",0.33),("F","F[+F]F",0.33),("F","F[-F]F",0.34)], niveau=5, angle= 25.7)

#Plante aléatoire 2
#Lsystem(axiome ="F", regles = [("F","F[+F][-F]F",0.5),("F","F[-F]F",0.3),("F","F[+F]F",0.2)], niveau=5, angle= 22.5)

#Plante à feuille aléatoire
#Lsystem(axiome ="B", regles = [("X","FX",1),("B","[-F{[-f+f+f][+f-f-f]}]FX[[-B][+B]]FX[+FXB]-B",0.5),("B","[+F{[-f+f+f][+f-f-f]}]FX[-B]FX[-FXB]+B",0.5)], niveau=7, angle= 20)

# Plante à feuille aléatoire avec angle aléatoire
#Lsystem(axiome ="B", regles = [("X","FX",1),("B","[-F{[-f+f+f][+f-f-f]}]FX[[-B][+B]]FX[+FXB]-B",0.5),("B","[+F{[-f+f+f][+f-f-f]}]FX[-B]FX[-FXB]+B",0.5)], niveau=6, angle= (15,26))

