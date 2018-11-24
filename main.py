#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Pygame
from pygame import *
from pygame.locals import *
import math
import db
		

#Char
class Char:
	
	def __init__(self, fenetre, x, y, couleur, nom, vitesse=4, relief=1):
		"""Où 'canvas' le nom du Canvas,
'x' et 'y' les coordonnées du char,
nom, un tuple sous la forme:nom = ('nom', x, y, couleur)"""
		#Le "monde" dans lequel évolue le char (fenêtre, canvas)
		self.fenetre = fenetre
		#Données qui seront initialisées plus tard (dans la fonction afficher)
		self.terrain = None
		self.Joueurs = None
		#Coordonnée du char
		self.char_x, self.char_x0 = x, x
		self.char_y, self.char_y0 = y, y
		#Coordonnée du canon
		self.alpha = math.pi/2
		self.canon_x = self.char_x + db.TILE//2 + 0.8*db.TILE*math.sin(0)
		self.canon_y = self.char_y + db.TILE//2 - 0.8*db.TILE*math.cos(0)
		#Pour la mine
		self.mine = None
		self.mine_x = 0
		self.mine_y = 0
		self.stock_mine = 1
		self.timer = 5000
		#Pour les munitions
		self.munition = []
		#Pour le mouvement
		self.dir = [False, False, False, False]
		self.vitesse = vitesse
		#Autre caractéristique ( couleur du char, nom, état (mort ou pas?), relief (taille des bordures) )
		self.couleur = couleur
		self.nom = nom
		self.mort = False
		self.relief = relief
	
	def afficher(self, fenetre):
		#
		self.canon_x = self.char_x + db.TILE//2 + 0.8*db.TILE*math.sin(0)
		self.canon_y = self.char_y + db.TILE//2 - 0.8*db.TILE*math.cos(0)
		
		#Le char
		draw.rect(fenetre, self.couleur, (self.char_x, self.char_y, db.TILE, db.TILE) )
			#Roues
		draw.rect(fenetre, db.GREY, (self.char_x, self.char_y, 6, 32) )
		draw.rect(fenetre, db.GREY, (self.char_x+26, self.char_y, 6, 32) )
			#Contour
		draw.rect(fenetre, db.BLACK, (self.char_x, self.char_y, 32, 32), 1 )
		#Le canon
		draw.line(fenetre, db.BLACK, (self.char_x+16, self.char_y+16), (self.canon_x, self.canon_y), 5 )
		#Le pivot
		draw.ellipse(fenetre, db.BLACK, (self.char_x+6, self.char_y+6, 20, 20) )
		draw.ellipse(fenetre, db.YELLOW, (self.char_x+12, self.char_y+12, 8, 8) )
	
	def change_dir(self, event):
		#Active la direction (pour le rang, voir clavier numérique)
		if (event == 'Down'):
			self.dir[0] = True
		elif (event == 'Left'):
			self.dir[1] = True
		elif (event == 'Up'):
			self.dir[2] = True
		elif (event == 'Right'):
			self.dir[3] = True
			
	def stop_dir(self, event):
		#Désactive la direction (pour le rang, voir clavier numérique)
		if (event == 'Down'):
			self.dir[0] = False
		if (event == 'Left'):
			self.dir[1] = False
		if (event == 'Up'):
			self.dir[2] = False
		if (event == 'Right'):
			self.dir[3] = False
			
	def mouvement_char(self):
		#Change la direction
		if self.dir[0]:
			self.char_y += self.vitesse
		if self.dir[1]:
			self.char_x -= self.vitesse
		if self.dir[2]:
			self.char_y -= self.vitesse
		if self.dir[3]:
			self.char_x += self.vitesse
		

#On affiche la fenêtre
##fenetre = display.set_mode( (0, 0), FULLSCREEN )
longueur, largeur = 32*db.TILE, 20*db.TILE
fenetre = display.set_mode( (longueur, largeur) )
display.set_caption("Char")

init()

#Boucle principale
continuer = 1
Joueur1 = Char( fenetre, 32, 32, db.YELLOW, ('Joueur', 60, 20, 'White') )
while continuer:
    time.Clock().tick(30)

    draw.rect(fenetre, db.NAVAJOWHITE, (0, 0, longueur, largeur) )
    Joueur1.afficher(fenetre)
    #fond = pygame.image.load('background.png').convert()
    #fenetre.blit(fond, (0, 0))
    display.flip()
    
    #Détection des touches / clicks
    for touche in event.get():
        if touche.type == QUIT:
            continuer = 0
        
        elif touche.type == KEYDOWN:
            """Touches clavier"""
            #=========Tileset=========#
            if (touche.key == K_z) or (touche.key == K_a):
                Joueur1.change_dir('Up')
            elif (touche.key == K_q) or (touche.key == K_w):
                Joueur1.change_dir('Left')
            elif (touche.key == K_s):
                Joueur1.change_dir('Down')
            elif (touche.key == K_d):
                Joueur1.change_dir('Right')
            if (touche.key == K_ESCAPE):
                continuer = 0
        if touche.type == KEYUP:
            """Touches clavier"""
            #=========Tileset=========#
            if (touche.key == K_z) or (touche.key == K_a):
                Joueur1.stop_dir('Up')
            elif (touche.key == K_q) or (touche.key == K_w):
                Joueur1.stop_dir('Left')
            elif (touche.key == K_s):
                Joueur1.stop_dir('Down')
            elif (touche.key == K_d):
                Joueur1.stop_dir('Right')
    Joueur1.mouvement_char()








