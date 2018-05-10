
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
Hit=0
rotate_angle = 0
Translate_Mov=0
def init():
    glClearColor(0.0,0.0,0.0,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
    glEnable(GL_DEPTH_TEST)
def display():
    global Hit
    global rotate_angle
    global Translate_Mov
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor(1.0,0.0,0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(Translate_Mov,0,0)
    glScale(1,.25,.5)                  #car
    glutWireCube(5)
    glLoadIdentity()
    glTranslate(Translate_Mov,.25*5,0)
    glScale(.5,.25,.5)
    glutWireCube(5)
    glColor(0,1,.3)                   #boxes
    glLoadIdentity()
    glTranslate(Translate_Mov+4, 0, 0)
    glScale(.4, .4, .4)
    glutWireCube(3)
    glLoadIdentity()
    glTranslate(Translate_Mov-4, 0, 0)
    glScale(.4, .4, .4)
    glutWireCube(3)
    glLoadIdentity()
    glTranslate(Translate_Mov, 0, 2.5)
    glScale(.4, .4, .4)
    glutWireCube(3)
    glLoadIdentity()
    glTranslate(Translate_Mov, 0, -2.5)
    glScale(.4, .4, .4)
    glutWireCube(3)
    glColor(0, .3, 1)                 #wheels
    glLoadIdentity()
    glRotate(rotate_angle, 0, 0, 1)
    glTranslate(Translate_Mov+2.5,-.5,.5*2.5)
    glutWireTorus(.25,.5,12,8)
    glLoadIdentity()
    glRotate(rotate_angle, 0, 0, 1)
    glTranslate(Translate_Mov-2.5,-.5,.5*2.5)
    glutWireTorus(.25,.5,12,8)
    glLoadIdentity()
    glRotate(rotate_angle, 0, 0, 1)
    glTranslate(Translate_Mov-2.5,-.5,-.5*2.5)
    glutWireTorus(.25,.5,12,8)
    glLoadIdentity()
    glRotate(rotate_angle, 0, 0, 1)
    glTranslate(Translate_Mov+2.5,-.5,-.5*2.5)
    glutWireTorus(.25,.5,12,8)
    rotate_angle += .01
    if Hit== 0:
        Translate_Mov += 0.1
    else:
        Translate_Mov-=0.1
    if Translate_Mov >= 5 :
        Hit=1
    elif Translate_Mov <= -5:
        Hit=0
    glutSwapBuffers()

def main():
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutCreateWindow(b" car")
        glutInitWindowSize(500, 500)
        init()
        glutIdleFunc(display)
        glutDisplayFunc(display)
        glutMainLoop()
main()