# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:37:00 2014

@author: Quentin
"""

#############################################################################
"""
 pixel.py
 Un environnement minimaliste pour dessiner un bitmap en 2D
"""
#############################################################################
import Tkinter as tkinter
import tkFileDialog as filedialog
import time

#
# Variables globales
#
largeur = 0
hauteur = 0
_fen = None
_sur_clic = None
_liste_modifs = []

_r = 1.0
_g = 1.0
_b = 1.0

#############################################################################
# DÃ©finition des fonctions
#############################################################################

def _menu_enregistrer():
    #########################################################################
    "Demande un nom de fichier pour enregistrer l'image au format GIF"
    #########################################################################
    file_name = filedialog.asksaveasfilename(
        defaultextension = '.gif',
        filetypes = [("Fichier GIF", '*.gif')],
        parent = _fen,
        title = "Enregistrer l'image")

    if file_name != None and file_name != '':
        enregistrer(file_name)

def initialiser(largeur_, hauteur_, taille):
    #########################################################################
    "Initialise la fenÃªtre avec un rectangle de pixels"
    #########################################################################
    global _can
    global _img
    global _fen
    global largeur
    global hauteur
    global _taille
    global _pixels
    global _buffer

    largeur = largeur_
    hauteur = hauteur_
    _taille = taille

    if _fen != None:
        _fen.destroy()

    _fen = tkinter.Toplevel()
    _fen.title("pixel")
    menubar = tkinter.Menu(_fen)
    menubar.add_command(label="Enregistrer l'image...",
                        underline = 0,
                        command = _menu_enregistrer)
    _fen.config(menu = menubar)

    _can = tkinter.Canvas(_fen,
                          width = largeur * taille,
                          height = hauteur * taille)
    _img = tkinter.PhotoImage(width = largeur * taille + 2,
                              height = hauteur * taille + 2)
    _img.put("#808080", (0, 0, largeur * taille + 2, hauteur * taille + 2))
    _img.put("#ffffff", (1, 1, largeur * taille + 1, hauteur * taille + 1))
    _can.create_image(0, 0, image = _img, anchor=tkinter.NW)
    _can.pack()
    _fen.resizable(width=False, height=False)

    _pixels = []
    _buffer = []
    for x in range(largeur):
        _pixels.append([])
        _buffer.append([])
        for y in range(hauteur):
            _pixels[x].append(1.0)
            _buffer[x].append(1.0)

    afficher(0)

def marquer(x, y, valeur = 0):
    #########################################################################
    "Change la valeur d'un pixel"
    #########################################################################
    global _liste_modifs
    xx = x % largeur
    yy = y % hauteur
    _buffer[xx][yy] = valeur
    _liste_modifs.append((xx, yy))

def lire(x, y):
    #########################################################################
    "Lit la valeur d'un pixel"
    #########################################################################
    xx = x % largeur
    yy = y % hauteur
    return _pixels[xx][yy]

def _normaliser(x):
    #########################################################################
    "Normalise un nombre entre 0.0 et 1.0"
    #########################################################################
    if x != None:
        x = float(x)
        if x < 0.0:
            x = 0.0
        elif x > 1.0:
            x = 1.0
    return x

def _couleur(x):
    #########################################################################
    "Calcule la couleur d'une valeur"
    #########################################################################
    if x == None:
        return '#000000'
    elif _r == None or _g == None or _b == None:
        r, g, b = 0.0, 0.0, 0.0
        x = float(x) % 1.0
        if 3.0 * x < 1.0:
            g = 3.0 * x
            r = 1.0 - g
        elif 3 * x < 2.0:
            b = 3.0 * x - 1.0
            g = 1.0 - b
        else:
            r = 3.0 * x - 2.0
            b = 1.0 - r
        r = int(r * 255.99)
        g = int(g * 255.99)
        b = int(b * 255.99)
        return '#%02x%02x%02x' % (r, g, b)
    else:
        x = _normaliser(x)
        r = int(x * _r * 255.99)
        g = int(x * _g * 255.99)
        b = int(x * _b * 255.99)
        return '#%02x%02x%02x' % (r, g, b)

def _copier_buffer_et_afficher():
    #########################################################################
    "Affiche les modifications"
    #########################################################################
    global _liste_modifs
    for xy in _liste_modifs:
        x = xy[0]
        y = xy[1]
        _pixels[x][y] = _buffer[x][y]
        c = _couleur(_pixels[x][y])
        _img.put(c, (x * _taille + 1,
                     y * _taille + 1,
                     (x + 1) * _taille + 1,
                     (y + 1) * _taille + 1))
    _liste_modifs = []

def _copier_buffer():
    #########################################################################
    "Copie le buffer sans l'afficher"
    #########################################################################
    global _liste_modifs
    for xy in _liste_modifs:
        x = xy[0]
        y = xy[1]
        _pixels[x][y] = _buffer[x][y]
    _liste_modifs = []

def couleur(r = None, g = None, b = None):
    #########################################################################
    "Choix de la couleur du dessin (par dÃ©fault = cyclique)"
    #########################################################################
    global _r
    global _g
    global _b

    _r = _normaliser(r)
    _g = _normaliser(g)
    _b = _normaliser(b)

def _tk_sur_clic(event):
    #########################################################################
    "Clic de la souris"
    #########################################################################
    _sur_clic((event.x - 1) // _taille, (event.y - 1) // _taille)

def sur_clic(f):
    #########################################################################
    "Appelle la fonction f(x, y) quand on clique sur le pixel x, y"
    #########################################################################
    global _sur_clic
    _sur_clic = f
    _can.bind("<Button-1>", _tk_sur_clic)

def afficher(pause = None):
    #########################################################################
    "Affiche les modifications, et fait Ã©ventuellement une pause"
    #########################################################################
    if pause == None:
        _copier_buffer_et_afficher()
        _fen.mainloop()
    else:
        if pause < 0:
            _copier_buffer()
        else:
            _copier_buffer_et_afficher()
            _fen.update()
            if pause > 0:
                time.sleep(pause)

def enregistrer(nom, format_enregistrement = 'gif'):
    #########################################################################
    "Enregistre l'image dans un fichier"
    #########################################################################
    _copier_buffer_et_afficher()
    _img.write(nom, format = format_enregistrement)