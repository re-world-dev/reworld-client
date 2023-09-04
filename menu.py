import pygame
import pygame_menu

pygame.init()
window = pygame.display.set_mode((800, 600))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

menu = pygame_menu.Menu('Welcome', 800, 600,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Pseudo : ', default='John Doe')
menu.add.selector('Mode :', [('Connexion serveur', 1), ('Lancer serveur solo', 2)], onchange=set_difficulty)
menu.add.button('Jouer', start_the_game)
menu.add.button('Quitter', pygame_menu.events.EXIT)

menu.mainloop(window)