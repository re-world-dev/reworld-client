#===================
#     RE:WORLD
#===================

# Libs import
import modding #RML (reworld mod loader)
from libs import console 
# Import of engine
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pywavefront
console.info("Main/Render : Game init")
modding.init()

pygame.init()


window_size = (800, 600)
screen = pygame.display.set_mode(window_size, DOUBLEBUF | OPENGL)


gluPerspective(45, (window_size[0] / window_size[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)
pygame.display.set_caption("RE:WORLD | BETA V0.1")

player_x = 0
player_y = 0
player_z = -5  # Le joueur commence en arrière
player_camera_rotation_x = 0 # Je sais pas quoi mettre...
player_camera_rotation_y = 0 # Ici aussi  

def load_object(pathobj,pathtexture):
    scene = pywavefront.Wavefront(path, collect_faces=True)

    glPushMatrix()
    glTranslatef(0, 0, -2.5)
    glBegin(GL_TRIANGLES)
    for face in scene.mesh_list[0].faces:
        for vertex_id in face:
            vertex = scene.vertices[vertex_id]
            glVertex3fv(vertex)
    glEnd()
    glPopMatrix()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        player_z += 0.1  
    if keys[pygame.K_s]:
        player_z -= 0.1  
    if keys[pygame.K_d]:
        player_x -= 0.1
    if keys[pygame.K_q]:
        player_x += 0.1

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glPushMatrix()
    glTranslatef(player_x, player_y, player_z)
    draw_cube(pathobj="assets/cube/cube.obj")
    glPopMatrix()
    
    pygame.display.flip()
    pygame.time.wait(10)
modding.stop_mods() # Buggé
pygame.quit()
