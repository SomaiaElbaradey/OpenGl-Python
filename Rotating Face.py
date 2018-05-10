import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
z=0

def initGl():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    #glEnable(GL_DEPTH_TEST)

def circle1(r=1, x0=0, y0=0):
    glColor(0,0,0)
    glBegin(GL_POLYGON)
    for ph in np.arange(0,2*pi,.001):
        x=x0+r*cos(ph)
        y=y0+r*sin(ph)
        glVertex2d(x,y)
    glEnd()

def circle(r=1, x0=0, y0=0):
    glColor(0,0,0)
    glBegin(GL_LINE_LOOP)
    for ph in np.arange(0,2*pi,.001):
        x=x0+r*cos(ph)
        y=y0+r*sin(ph)
        glVertex2d(x,y)

    glEnd()

def line():
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex(.32,-.4,1)
    glVertex(-.32,-.4,1)
    glEnd()

def display():
    global z
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    glRotate(z,0,0,1)
    glLineWidth(3.0)
    circle(.8,0,0)
    #glRotate(0,0,z,1)

    circle(.9,0,0)
    glRotate(0,0,z,1)
    circle(.15,.2,.2)
    circle(.15,-0.2,0.2)
    circle(.08,0,-.2)
    line()
    circle1(.06, .2, .2)
    circle1(.06, -.2, .2)
    #glRotate(0,0,z,1)
    z+=0.5
    glutSwapBuffers()


def main():
    glutInit()
    glutInitWindowSize(600,600)
    glutCreateWindow(b"Face1")
    initGl()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()

main()