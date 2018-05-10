"""
Program name: textured_cubes_rotation_1.py
Objective: Fully cover two cubes with photo images.
Observe the result of ignoring pixel depth.


comments: There are six 256 x 256 bmp images on the faces of a cube.
Usable image types:    bmp  and jpg work fine, but png does not.
Attempting to use png we get: "SystemError: unknown raw mode"

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3
Author:    De Fine
"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame

# Rotation angles for each cube.
from pygame.tests.base_test import pygame_quit

textures = ()
xrot1 = yrot1 = zrot1 = 0.0
xrot2 = yrot2 = zrot2 = 0.0


# =================================================================

def LoadTextures():
    """  Open images and convert them to "raw" pixel maps and
         bind or associate each image with and integer refernece number.
    """
    global textures
    image = pygame.image.load("chess.png")
    ix = image.get_width()
    iy = image.get_height()

    raw_image = pygame.image.tostring(image, "RGBA", 1)
    textures = glGenTextures(12)
    for i in range(0, 11):
        texture_setup(raw_image, i, ix, iy)


def texture_setup(image_name, texture_num, ix, iy):
    glBindTexture(GL_TEXTURE_2D, textures[texture_num])

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)

    glEnable(GL_TEXTURE_2D)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_name)


def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Clear the background color to black.
    glClearDepth(1.0)  # Clear the Depth buffer.
    glDepthFunc(GL_LESS)  # The type Of depth test to do.
    glEnable(GL_DEPTH_TEST)  # Leave this Depth Testing and observe the visual weirdness.
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Reset The Projection Matrix.
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)  # Aspect ratio. Make window resizable.
    glMatrixMode(GL_MODELVIEW)


# ==============================================================



def make_cube_1(start):
    glBindTexture(GL_TEXTURE_2D, textures[start])
    glBegin(GL_QUADS)
    glTexCoord(0, 0)
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Left of The Texture and Quad
    glTexCoord(1, 0)
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Right of The Texture and Quad
    glTexCoord(1, 1)
    glVertex3f(1.0, 1.0, 1.0)  # Top Right of The Texture and Quad
    glTexCoord(0, 1)
    glVertex3f(-1.0, 1.0, 1.0)  # Top Left of The Texture and Quad
    glEnd();

    # Back Face
    glBindTexture(GL_TEXTURE_2D, textures[start + 1])
    glBegin(GL_QUADS)
    glTexCoord(0, 0)
    glVertex3f(-1.0, -1.0, -1.0)  # Bottom Right
    glTexCoord(1, 0)
    glVertex3f(-1.0, 1.0, -1.0)  # Top Rightn
    glTexCoord(1, 1)
    glVertex3f(1.0, 1.0, -1.0)  # Top Left
    glTexCoord(0, 1)
    glVertex3f(1.0, -1.0, -1.0)  # Bottom Left
    glEnd()

    # Top Face
    glBindTexture(GL_TEXTURE_2D, textures[start + 2])
    glBegin(GL_QUADS)
    glTexCoord(0, 0)
    glVertex3f(-1.0, 1.0, -1.0)  # Top Left
    glTexCoord(1, 0)
    glVertex3f(-1.0, 1.0, 1.0)  # Bottom Left
    glTexCoord(1, 1)
    glVertex3f(1.0, 1.0, 1.0)  # Bottom Right
    glTexCoord(0, 1)
    glVertex3f(1.0, 1.0, -1.0)  # Top Right
    glEnd();

    # Bottom Face
    glBindTexture(GL_TEXTURE_2D, textures[start + 3])
    glBegin(GL_QUADS)
    glTexCoord(0, 0)
    glVertex3f(-1.0, -1.0, -1.0)  # Top Right
    glTexCoord(1, 0)
    glVertex3f(1.0, -1.0, -1.0)  # Top Left
    glTexCoord(1, 1)
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Left
    glTexCoord(0, 1)
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Right
    glEnd();

    # Right face
    glBindTexture(GL_TEXTURE_2D, textures[start + 4])
    glBegin(GL_QUADS)
    glTexCoord(0, 0)
    glVertex3f(1.0, -1.0, -1.0)  # Bottom Right
    glTexCoord(1, 0)
    glVertex3f(1.0, 1.0, -1.0)  # Top Right
    glTexCoord(1, 1)
    glVertex3f(1.0, 1.0, 1.0)  # Top Left
    glTexCoord(0, 1)
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Left
    glEnd();

    # Left Face
    glBindTexture(GL_TEXTURE_2D, textures[start + 5])
    glBegin(GL_QUADS)
    glTexCoord(0, 0)
    glVertex3f(-1.0, -1.0, -1.0)  # Bottom Left
    glTexCoord(1, 0)
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Right
    glTexCoord(1, 1)
    glVertex3f(-1.0, 1.0, 1.0)  # Top Right
    glTexCoord(0, 1)
    glVertex3f(-1.0, 1.0, -1.0)  # Top Left
    glEnd();


def DrawFrontFace():
    """   A texture binding created with glBindTexture remains active until a different texture
    	  is bound to the same target, or until the bound texture is deleted with glDeleteTextures.
    """
    global xrot1, yrot1, zrot1, xrot2, yrot2, zrot2
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen and Depth buffer

    # First textured cube.
    glLoadIdentity()  # Reset The View
    glTranslatef(-2.0, 0.0, -5.0)  # Shift cube left and back.
    glRotatef(xrot1, 1.0, 0.0, 0.0)  # Rotate the cube on It's X axis.
    glRotatef(yrot1, 0.0, 1.0, 0.0)  # Rotate the cube on It's Y axis.
    glRotatef(zrot1, 0.0, 0.0, 0.0)  # Rotate the cube on It's Z axis.
    make_cube_1(0)  # "0" is the first index no. of a six member sequence - images.

    xrot1 = xrot1 + 0.1  # X rotation of first cube.
    yrot1 = yrot1 - 0.05  # Y rotation
    zrot1 = zrot1 + 0.05  # Z rotation

    # Second textured cube.
    glLoadIdentity()  # Reset The view
    glTranslatef(1.5, 0.0, -5.0)  # Shift cube right and back.
    glRotatef(xrot2, 1.0, 0.0, 0.0)  # Rotate the cube on It's X axis.
    glRotatef(yrot2, 0.0, 1.0, 0.0)  # Rotate the cube on It's Y axis.
    glRotatef(zrot2, 0.0, 0.0, 0.0)  # Rotate the cube on It's Z axis
    make_cube_1(5)  # "6" is the first index no. of a different six member sequence - images.

    xrot2 = xrot2 - 0.05  # X rotation of second cube.
    yrot2 = yrot2 + 0.07  # Y rotation
    zrot2 = zrot2 + 0.09  # Z rotation

    glutSwapBuffers()

    # =================================================================


def main():
    glutInit("")
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(1000, 480)
    window = glutCreateWindow(b"Textured rotating cubes")
    LoadTextures()
    glutDisplayFunc(DrawFrontFace)
    glutIdleFunc(DrawFrontFace)  # When we are doing nothing, redraw the scene.
    InitGL(1000, 480)  # Initialize our window.
    glutMainLoop()  # Start the event processing engine


main()


