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

def solo():
    #
    pass

def multiplayer():
    #
    pass

def mods():
    #
    pass

mytheme=pygame_menu.themes.THEME_DARK.copy()
mytheme.widget_font = pygame_menu.font.FONT_MUNRO
mytheme.title_font = pygame_menu.font.FONT_MUNRO

login = pygame_menu.Menu('eletrixworld', 800, 600, theme=mytheme)

pseudo = login.add.text_input('Pseudo : ', default='Elon Musk')
password = login.add.text_input('Password : ', default='123')
login.add.selector("", [('Se connecter', 1), ('Creer un compte', 2)], onchange=set_difficulty)
login.add.button('SOLO', solo)
login.add.button('MULTIJOUEUR', multiplayer)
login.add.button('Mods', mods)
login.add.button('Effectuer action', start_the_game)
login.add.button('Quitter', pygame_menu.events.EXIT)

login.mainloop(window)
