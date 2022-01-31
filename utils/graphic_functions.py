import pygame, sys, json
#initialisation, setup
def setup():
    try:
        pygame.init()
        clock = pygame.time.Clock()
    except Exception as e:
        print(e)
    return clock

#create the display surface
def display(game):
    try:
        #titre de la fenetre avec recup d'info dans le json
        pygame.display.set_caption(game["player"]["name"])
        clock = setup()
        #surface principal
        screen = pygame.display.set_mode((1310,710))
        #creation de la zone map et affichage d'image en fonction du lieu où l'on se trouve avec recup d'info dans le json  
        if game["player"]["location"]["detail"] == "":
            map_surface = pygame.Surface((990,490))
            map_surface.fill((20,148,20))
        elif game["player"]["location"]["detail"] == "Lindenvale.inn.lobby":
             map_surface = pygame.Surface((990,490)) and pygame.image.load("img/hall_inn.jpg")
        else:
            map_surface = pygame.Surface((990,490)) and pygame.image.load("img/cities.jpg")        
        #creation zone des choix
        choice_surface = pygame.Surface((990,190)) and pygame.image.load("img/choice_background.jpg")
        #creation de la zone inventaire
        inventory_surface = pygame.Surface((290,690))
        inventory_surface.fill((137,137,137))
        #quand le jeu tourne, affichage et moyen de quitter
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #affichage des surfaces
            screen.fill((0,0,0))
            screen.blit(map_surface,(10,10))
            screen.blit(inventory_surface,(1010,10))
            screen.blit(choice_surface,(10,510))
            
            pygame.display.flip()
            clock.tick(60)

    except Exception as e:
        print(e)

    return game
