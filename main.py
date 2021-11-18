import pygame
pygame.init()
W, H = 1280, 720
surface = pygame.display.set_mode((W, H)) #Taille de la fenêtre
pygame.display.set_caption("Projet nsi") #Nom de la fenêtre
running = True #Etat du jeu
clock = pygame.time.Clock() 
couleur = (0, 0, 0) #Variable couleur, par défault ici noire, pour rappel les couleurs se définissent par (red, green, blue)
while running:
    surface.fill(couleur) #Remplit l'écran d'après la variable couleur
    for event in pygame.event.get(): #Prend en compte les actions de l'ordi
        if event.type == pygame.QUIT: #Si l'utilisateur quitte
            running = False
        if event.type == pygame.KEYDOWN: #Si l'utilisateur appuie sur une touche (KEYUP pour détecter si l'utilisateur relache la touche)
            if event.key == pygame.K_a: #Si la touche pressée est a
                if couleur == (0, 0, 0): #Si la couleur est noire
                    couleur = (100, 100, 150) #Change la couleur en une autre couleur
                else:   
                    couleur = (0, 0, 0)
    pygame.display.flip()
    clock.tick(60) #Met le jeu à 60 fps
            
pygame.quit()
