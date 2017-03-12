# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:41:22 2014

@author: Quentin
"""
    
def dessinerCouleur(chaine,motif,distance,angle,position,direction,xpos,ypos):
    import turtle as tt
    from LSysteme import dessiner, alphabet_dessin
    l1=len(chaine)
    l2=len(motif)
    L=[]
    k=0
    while k<l1: #on parcourt la chaine
        b = True #booléen qui indique si la chaine est un motif
        if chaine[k] == motif[0]:
            if k+l2-1 < l1: #on vérifie que l'on ne va pas dépasser la chaine
                for m in range(l2):
                    if alphabet_dessin.find(chaine[k+m]) != -1 and chaine[k+m] != motif[m]: 
                        b = False 
                        #on vérifie que l'on a un motif ou que les caractères n'influent pas le motif
                if b: #si c'est bien un motif, on le colorie en rouge
                    tt.color((1,0,0))
                    xpos,ypos,L=dessiner(motif,L,distance,angle,position,direction,xpos,ypos)
                    tt.color((0,0,0))
                    k+=l2
            else :
                b = False
        else :
            b = False
        if not b: #si le ce n'est pas un motif, on éffectue les translations et rotations
            xpos,ypos,L=dessiner(chaine[k],L,distance,angle,position,direction,xpos,ypos)
            k+=1
        position = tt.pos()
        direction = tt.heading()
    return xpos,ypos

def LsystemCouleur(axiome,regles,niveau=1,distance=10,angle=90,position=(0,0),direction=90) :
    
    from LSysteme import screen,construire_chaine
    import turtle as tt
    tt.mode('world')
    tt.tracer(0) #on enlève les animations
    xpos=[]
    ypos=[]
    chaine= construire_chaine(axiome,regles,niveau) #on construit la chaine au niveau voulu
    motif = construire_chaine(axiome,regles,2)
    xpos,ypos = dessinerCouleur(chaine,motif,distance,angle,position,direction,xpos,ypos)#et on la dessine
    screen(xpos,ypos)    #on affiche la fenêtre avec les bonnes coordonnées
            
#LsystemCouleur(axiome="SX", regles=[("S","F-F--F+F++FF+F-"),("R","+F-FF--F-F++F+F"),("X","X-YR--YR+SX++SXSX+YR-"),("Y","+SX-YRYR--YR-SX++SX+Y")], angle=60 ,niveau =4) 

#LsystemCouleur(axiome ="X", regles = [("X","F[+X]F[-X]+X"),("F","FF")], niveau=7, angle= 20)

LsystemCouleur(axiome ="X", regles = [("X","F-[[X]+X]+F[+FX]-X"),("F","FF")], niveau=5, angle= 22.5)