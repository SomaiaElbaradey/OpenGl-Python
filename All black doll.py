from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *


def draw1():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor(0,0,0)
    glBegin(GL_POLYGON)
    r=0.25
    for theta in np.arange(0,2*pi,0.01):
        x=r*cos(theta)
        y=r*sin(theta)+0.65
        glVertex2d(x,y)
    glEnd()
    glFlush()

    glBegin(GL_POLYGON)
    glVertex2d(0.5,-0.5)
    glVertex2d(0,0.65)
    glVertex2d(-0.5,-0.5)
    glEnd()
    glFlush()

    glBegin(GL_POLYGON)
    glVertex2d(0.3,-0.5)
    glVertex2d(0.2,-0.5)
    glVertex2d(0.2,-0.75)
    glVertex2d(0.3,-0.75)
    glEnd()
    glFlush()

    glBegin(GL_POLYGON)
    glVertex2d(-0.3,-0.5)
    glVertex2d(-0.2,-0.5)
    glVertex2d(-0.2,-0.75)
    glVertex2d(-0.3,-0.75)
    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glVertex2d(0.2,0.2)
    glVertex2d(0.75,-0.1)
    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glVertex2d(-0.2,0.2)
    glVertex2d(-0.75,-0.1)
    glEnd()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"girl")
glutDisplayFunc(draw1)
glutMainLoop()