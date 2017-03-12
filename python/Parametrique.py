# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 17:07:17 2014

@author: Quentin
"""

###################################### TIPE : L-Systèmes - 2e année ############################
######################################## L-systèmes paramétriques ##############################

def nbr_virgule(s):
    """ Compte le nombre de virgule dans un mot"""
    n = 0    
    for k in s:
        if k == ',':
            n+=1
    return n

def mot_parenthese(mot):
    """ Extrait le premier mot entre parenthèse rencontré d'une chaine de caractère"""
    s = ''
    k=0
    while mot[k] != '(':
        k+=1
    k+=1
    while mot[k] != ')':
        s+= mot[k]
        k+=1
    return s

def dico_var(old,s) :
    """ Construit un dictionnaire qui associe les paramètres à leur valeurs """
    L = []
    k=0
    while old[k] == s[k] and old[k] != '(' :
        k+=1
    b = True
    while b:
        k+=1
        i = k
        var = '' #récupère le paramètre de la règle
        while old[i] != ',' and old[i] != ')':
            var += old[i]
            i+=1
        val = '' # récupère la valeur actuelle du paramètre
        while s[k] != ',' and s[k] != ')':
            val += s[k]
            k+=1
        L.append((var,int(val))) # L est une liste de couple (paramètre, valeur)
        if old[i] == ')' or s[k] == ')': # on continue tant qu'il reste des paramètres
            b = False
    return dict(L)
    

# regles de la forme : ("pred","condition","succ")
def chaine_parametrique(axiome,regles,niveau):
    """ Fonction qui construit la chaine d'un L-système paramétrique au niveau demandé """
    l = axiome
    n2 = len(regles)
    for n in range(niveau): #pour chaque niveau
        L=''
        k = 0
        while k < len(l): #on parcourt la chaine actuelle
            b1 = False # booléen qui vérifie si il y a eu un changement
            for p in range(n2): 
                old,cond,new = regles[p][0],regles[p][1],regles[p][2] # old = pred, new = succ
                if l[k] == old:
# si le prédecesseur n'a pas de paramètre (prédécesseur est une lettre) et que la lettre actuelle est égale au prédecesseur
                    L += new # on ajoute le successeur
                    b1 = True # il y a eu un changement
                    incr = 1 # incr compte le nombre de lettre dont il faut avancer
                elif l[k] == old[0]: 
# si la lettre actuelle correspond à la lettre du prédecesseur mais que celui ci a un paramètre
                    s = l[k] + l[k+1]
                    j = 2 
                    while l[k+j] != ')':
                        s += l[k+j]
                        j+=1                    
                    s += l[k+j]
# on extrait la chaine contenant la lettre ainsi que les valeurs des paramètres
                    if nbr_virgule(s) == nbr_virgule(old): # on vérifie qu'il y a le même nombre de paramètres
                        dico = dico_var(old,s) # on construit un dico associant paramètre et valeur
                        if eval(cond,dico) : # on évalue les conditions en fonction des paramètres
                            incr = j+1
                            i = 0
                            b1 = True
                            while i < len(new): # on rajoute le successeur avec les paramètres modifiés
                                if new[i] != '(':
                                    L += new[i]
                                    i+=1
                                else :
                                    L += new[i]
                                    i+= 1
                                    b2 = True
                                    while b2:
                                        s2 = ''
                                        while new[i] != ',' and new[i] != ')' :
                                            s2 += new[i]
                                            i+=1
                                        L += str(eval(s2,dico))
                                        if new[i] == ')':
                                            b2 = False
                                        L += new[i]
                                        i+=1
            if not b1 :
                L += l[k]
                incr = 1
            k += incr
        l=L
    return l


#Test de la chaine parametrique    
#print chaine_parametrique( axiome = "B(2)A(4,4)", regles = [("A(x,y)","y <= 3","A(x*2,x+y)"),("A(x,y)","y>3","B(x)A(x/y,0)"),("B(x)","x<1","C"),("B(x)","x>=1","B(x-1)")], niveau = 6)

#print chaine_parametrique(axiome = "I(9)a(13)", regles = [("a(t)","t>0","[&(70)L]/(137.5)I(10)a(t-1)"),("a(t)","t==0","[&(70)L]/(137.5)I(10)A"),("A","*","[&(18)u(4)FFI(10)I(5)KKKK]/(137.5)I(8)A"),("I(t)","t>0","FI(t-1)"),("I(t)","t==0","F"),("u(t)","t>0","&(9)u(t-1)"),("u(t)","t==0","&(9)"),("L","*","[{-(18)FI(7)+(18)FI(7)+(18)FI(7)}][{+(18)FI(7)-(18)FI(7)-(18)FI(7)}]"),("K","*","[&(18){+(18)FI(2)-(36)FI(2)}][&(18){-(18)FI(2)+(36)FI(2)}]/(90)")], niveau = 15)

def traduction_parametrique(chaine, distance, angle):
    """ Fonction qui traduit une chaine de L-système paramétrique en procédure Géotortue"""
    fichier = open("Chaine.txt","w")
    fichier.write("pour plante\n")    
    l = len(chaine)
    k = 0
    i=0
    j=50
    b = False
    fin = False
    couleur = 'vert'
    while k < l:
        if k == l-1 : 
            fin = True
            
        if chaine[k] == '(':
            b = True
        elif chaine[k] == ')' :
            b = False
        elif chaine[k] == 'F' :
            if not fin:
                if chaine[k+1] == '(':
                    distance = float(mot_parenthese(chaine[k:]))
            fichier.write("av {0}\n".format(distance))
        elif chaine[k] == 'f' :
            if not fin:
                if chaine[k+1] == '(':
                    distance = float(mot_parenthese(chaine[k:]))
            fichier.write("lc\n av {0} \n bc\n".format(distance))
        elif chaine[k] == '+' :
            if not fin:                
                if chaine[k+1] == '(':
                    angle = float(mot_parenthese(chaine[k:]))
            fichier.write("tg {0}\n".format(angle))
        elif chaine[k] == '&' :
            if not fin:                    
                    if chaine[k+1] == '(':            
                        angle = float(mot_parenthese(chaine[k:]))
            fichier.write("pvh {0}\n".format(angle))
        elif chaine[k] == '/' :
            if not fin:            
                if chaine[k+1] == '(':
                    angle = float(mot_parenthese(chaine[k:]))
            fichier.write("pvd {0}\n".format(angle))
        elif chaine[k] == "[" :
            i+=1
            fichier.write("à {0}\n tlp X(Achille) Y(Achille) Z(Achille)\nimite Achille\nà Achille\n".format(i))
        elif chaine[k] == "]" :
            fichier.write("tlp X({0}) Y({0}) Z({0})\nimite {0}\n".format(i))
            i-=1
        elif chaine[k] == "{" :
            fichier.write("remplis [\n")
#            j=50
        elif chaine[k] == "}" :
            fichier.write("]\n crayon noir\n")
#            fichier.write(" à {2}\n crayon {3}\n remplis [boucle k de 50 à {0} [ tlp X(k) Y(k) Z(k)\nvise k+1\nav dist(k,k+1)\n]\ntlp X({1}) Y({1}) Z({1})\nvise 50\nav dist(50,{1})\n ]\nà Achille\n".format(j-1,j,j+1,couleur))
        elif chaine[k] == "'" :
            fichier.write("crayon vert\n")
        elif chaine[k] == "`" :
            fichier.write("crayon rouge\n")
        elif chaine[k] == "." and not b :
            fichier.write("à {0}\n tlp X(Achille) Y(Achille) Z(Achille)\nimite Achille\nà Achille\n".format(j))
            j+=1
        k+=1
    fichier.write("fin")
            
def LSysteme_param(axiome,regles,niveau,distance, angle):
    """ Construit la procédure pour géotortue associée au L-système paramétrique rentré"""
    chaine = chaine_parametrique(axiome,regles,niveau)
    traduction_parametrique(chaine, distance, angle)

#test capsella (old)
#LSysteme_param( axiome = "I(9)a(13)", regles = [("a(t)","t>0","[&(70)L]/(137.5)I(10)a(t-1)"),("a(t)","t==0","[&(70)L]/(137.5)I(10)A"),("A","*","[&(18)u(4)FFI(10)I(5)KKKK]/(137.5)I(2)A"),("I(t)","t>0","FI(t-1)"),("I(t)","t==0","F"),("u(t)","t>0","&(9)u(t-1)"),("u(t)","t==0","&(9)"),("L","*","['{+(-18)FI(7)+(18)FI(7)+(18)FI(7)}]['{+(18)FI(7)+(-18)FI(7)+(-18)FI(7)}]"),("K","*","[&(18)`{+(18)FI(2)+(-36)FI(2)}][&(18)`{+(-18)FI(2)+(36)FI(2)}]/(90)")], niveau = 25, distance = 10, angle = 18)    

#capsella (new, feuille triangle)
#LSysteme_param( axiome = "I(9)a(13)", regles = [("a(t)","t>0","[&(70)L]/(137.5)I(10)a(t-1)"),("a(t)","t==0","[&(70)L]/(137.5)I(10)A"),("A","*","[&(18)u(4)FFI(10)I(5)KKKK]/(137.5)I(2)A"),("I(t)","t>0","FI(t-1)"),("I(t)","t==0","F"),("u(t)","t>0","&(9)u(t-1)"),("u(t)","t==0","&(9)"),("L","*","[F(70)I(5)'{+(30)F(30)I(5)+(-120)F(30)I(5)+(-120)F(30)I(5)}]"),("K","*","[&(18)`{+(18)FI(2)+(-36)FI(2)}][&(18)`{+(-18)FI(2)+(36)FI(2)}]/(90)")], niveau = 15, distance = 10, angle = 18)    

#test Lychnis coronaria
#LSysteme_param( axiome = "A(7)", regles = [("A(t)","t==7","FI(20)[&(60)L]/(90)[&(45)A(0)]/(90)[&(60)L]/(90)[&(45)A(4)]FI(10)K"),("A(t)","t<7","A(t+1)"),("I(t)","t>0","FFI(t-1)"),("L","*","['{+(-18)FI(7)+(18)FI(7)+(18)FI(7)}]['{+(18)FI(7)+(-18)FI(7)+(-18)FI(7)}]"),("K","*","[&(18)`{+(18)FI(2)+(-36)FI(2)}][&(18)`{+(-18)FI(2)+(36)FI(2)}]/(90)")], niveau =20, distance = 10, angle = 18)


#test feuille 1
#traduction_parametrique("'{[++++f.][++ff.][+fff.][fffff.][+(-45)fff.][+(-90)ff.][+(-180)f.]}",20,45)

#test feuille 2
#LSysteme_param(axiome = "[A][B]", regles = [("A","*","[+A{.].C.}"),("B","*","[-B{.].C.}"),("C","*","fC")],niveau = 5, distance = 20, angle =60)

#test
#LSysteme_param( axiome = "A(7)", regles = [("A(t)","t==7","FI(20)[&(60)L]/(90)[&(45)A(0)]/(90)[&(60)L]/(90)[&(45)A(4)]FI(10)B"),("A(t)","t<7","A(t+1)"),("I(t)","t>0","FFI(t-1)"),("L","*","['{+(-18)FI(7)+(18)FI(7)+(18)FI(7)}]['{+(18)FI(7)+(-18)FI(7)+(-18)FI(7)}]"),("K","*","[&(18)`{+(18)FI(2)+(-36)FI(2)}][&(18)`{+(-18)FI(2)+(36)FI(2)}]/(90)"),("B","*","[&&&P/W////W////W////W////W]"),("W","*","[`^F][{&&&&-f+f|-f+f}]")], niveau =20, distance = 10, angle = 18)

