#Importation de l'arrière-plan du score
import os
os.chdir("C:/Users/Bak/Desktop/Python/Ball/data") 
goodend = pygame.image.load("goodend.jpg").convert()
fenetre.blit(goodend, (0,0))
pygame.display.flip()
#AFFICHAGE DU SCORE
	#Conversion du score jusque là un int en str pour pouvoir l'intégrer dans un texte
y = str(x)
	#Boucle nécessaire à l'affichage du score
if pygame.font:
	font = pygame.font.Font(None, 36)
		#Texte
	text = font.render("GAGNE!!!Vous avez désactivé "+y+" bombes",1,(10,10,10))
		#Texte centré en haut de l'image
	textpos = text.get_rect(centerx=fond.get_width()/2)
	fenetre.blit(text, textpos)
		#Raffraichissement final
	pygame.display.flip()