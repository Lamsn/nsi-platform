import pygame
pygame.init()
W, H = 1280, 720
surface = pygame.display.set_mode((W, H)) #Taille de la fenêtre
pygame.display.set_caption("Projet nsi") #Nom de la fenêtre
running = True #Etat du jeu
clock = pygame.time.Clock() 
couleur = (255, 255, 255) #Variable couleur, par défault ici noire, pour rappel les couleurs se définissent par (red, green, blue)
keysPressed = []
class player:
    def __init__(self, left, top, width, height, moveKeys = [pygame.K_z, pygame.K_q, pygame.K_s, pygame.K_d]):
        self.rect = pygame.Rect(left, top, width, height)
        self.velocity = [0, 0]
        self.color = (100, 100, 150)
        self.moveKeys = moveKeys
        self.onGround = False
    def update(self):
        self.collision()
        if self.moveKeys[0] in keysPressed and self.onGround:
            self.velocity[1] = -20
        
        if self.moveKeys[1] in keysPressed:
            self.velocity[0] = -10
        elif self.moveKeys[3] in keysPressed:
            self.velocity[0] = 10
        else:
            self.velocity[0] = 0
        if not self.onGround:
            self.velocity[1]+=0.5
        self.rect.left+=self.velocity[0]
        self.rect.top+=self.velocity[1]
        print(self.rect)
        pygame.draw.rect(surface, self.color, self.rect)
    def collision(self):
        if self.rect.top + self.rect.height >= H:
            self.rect.top = H - self.rect.height
            self.onGround = True
            self.velocity[1] = 0
        else: 
            self.onGround = False
            
player = player(0, 0, 30, 30)
while running:
    surface.fill(couleur) #Remplit l'écran d'après la variable couleur
    for event in pygame.event.get(): #Prend en compte les actions de l'ordi
        if event.type == pygame.QUIT: #Si l'utilisateur quitte
            running = False
        if event.type == pygame.KEYDOWN: #Si l'utilisateur appuie sur une touche (KEYUP pour détecter si l'utilisateur relache la touche)
            keysPressed.append(event.key)   
            if event.key == pygame.K_a: #Si la touche pressée est a
                    if couleur == (0, 0, 0): #Si la couleur est noire
                        couleur = (100, 100, 150) #Change la couleur en une autre couleur
                    else:   
                        couleur = (0, 0, 0)
        if event.type == pygame.KEYUP:  
            try:
                keysPressed.remove(event.key)   
            except:pass
                
    player.update()
    #print(player.rect.left, player.rect.top)
    pygame.display.flip()
    clock.tick(60) #Met le jeu à 60 fps
            
pygame.quit()
