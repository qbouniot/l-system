# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 14:33:59 2014

@author: Quentin
"""

################################ TIPE : L-systèmes - 2e année ##############################
################################## Fonctions 3D / Géotortue ################################

def traduction(chaine,distance,angle):
    """ Traduit la chaine de caractère en procédure pour géotortue"""
    import random as rd
    i = 0
    j =50
    fichier = open("Chaine.txt","w")
    fichier.write("pour plante\n")
    for k in chaine :
        if type(angle) == tuple: 
                theta = rd.uniform(angle[0],angle[1])
        else:
                theta = angle
        if k == "F" :
            fichier.write("av {0}\n".format(distance))
        elif k == "f" :
            fichier.write("lc\n av {0} \n bc\n".format(distance))
        elif k == "+" :
            fichier.write("tg {0}\n".format(theta))
        elif k == "-" :
            fichier.write("td {0}\n".format(theta))
        elif k == "|" :
            fichier.write("tg 180\n")
        elif k == "&" :
            fichier.write("pvh {0}\n".format(theta))
        elif k == "^" :
            fichier.write("pvb {0}\n".format(theta))
        elif k == "\\" :
            fichier.write("pvg {0}\n".format(theta))
        elif k == "/" :
            fichier.write("pvd {0}\n".format(theta))
        elif k == "[" :
            i+=1
            fichier.write("à {0}\n tlp X(Achille) Y(Achille) Z(Achille)\nimite Achille\nà Achille\n".format(i))
        elif k == "]" :
            fichier.write("tlp X({0}) Y({0}) Z({0})\nimite {0}\n".format(i))
            i-=1
        elif k == "{" :
            fichier.write("remplis [\n")
        elif k == "}" :
            fichier.write("]\n crayon noir\n")
        elif k == "'" :
            fichier.write("crayon vert\n")
        elif k == "`" :
            fichier.write("crayon rouge\n")
        elif k == "." :
            j+=1
            fichier.write("à {0}\n tlp X(Achille) Y(Achille) Z(Achille)\nimite Achille\nà Achille\n".format(j))
            if j != 51 :
                fichier.write("à {0}\n vise {1}\n av dist({0},{1})\n".format(j-1,j))
    fichier.write("fin")

def geoturtle(axiome,regles,niveau,distance,angle, parametre = False) :
    """ Construit la procédure pour géotortue associée au L-système rentré"""
    import LSysteme as LS
    chaine = LS.construire_chaine(axiome,regles,niveau)
    traduction(chaine,distance,angle)    
    
    
#Plante à fleurs
#geoturtle(axiome = "A", regles = [("A","I+[A+B]--//[--L]I[++L]-[AB]++AB",1),("I","FS[//&&L][//^^L]FS",1),("S","SFS",1),("L","['{+f-ff-f+|+f-ff-f}]",1),("B","[&&&P/W////W////W////W////W]",1),("P","FF",1),("W","[`^F][{&&&&-f+f|-f+f}]",1)], niveau = 5, distance = 10, angle = 18)

#Plante à fleurs stochastique
#geoturtle(axiome = "A", regles = [("A","I+[A+B]--//[--L]I[++L]-[AB]++AB",1),("I","FS[//&&L][//^^L]FS",1),("L","['{+f-ff-f+|+f-ff-f}]",1),("B","[&&&P/W////W////W////W////W]",1),("P","FF",1),("W","[`^F][{&&&&-f+f|-f+f}]",1),("S","S[//&&L][//^^L]FS",0.33),("S","SFS",0.33),("S","S",0.34)], niveau = 5, distance = 10, angle = (15,21))

#Bush-like structure
#geoturtle(axiome = "A", regles = [("A","[&FLA]/////[&FLA]///////[&FLA]",1),("F","S/////F",1,),("S","FL",1),("L","[^^'{-f+f+f-|-f+f+f}]",1)], niveau = 7, distance = 10, angle = 22.5)

#traduction("{[++++F.][++FF.][+FFF.][FFFFF.][-FFF.][--FF.][---F.]}",20,45)