from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

        
def init():
    glClearColor(0.,0.,0.,0.)
    glEnable(GL_DEPTH_TEST)
    gluOrtho2D(-20.0, 20.0, -20.0, 20.0)

# Fungsi konversi rgb
def rgb(n):
    return n / 255.0

# Pivot
def pivot():
    glBegin(GL_LINES)
    glColor3f(1,0,0) #merah x
    glVertex3f(10,0,0)
    glVertex3f(-10,0,0)
    glColor3f(0,1,0) #hijau y
    glVertex3f(0,10,0)
    glVertex3f(0,-10,0)
    glColor3f(0,0,1) #biru x
    glVertex3f(0,0,10)
    glVertex3f(0,-0,-10)    
    glEnd()

# Piramida
def piramida():
    # Depan
    glBegin(GL_POLYGON)
    glColor3f(rgb(231),rgb(1),rgb(10))
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(0.0, 1.0, 0.0) # Point
    glVertex3f(-1.0, -1.0, 1.0)
    glEnd()

    # Belakang
    glBegin(GL_POLYGON)
    glColor3f(rgb(231),rgb(1),rgb(10))
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(0.0, 1.0, 0.0) # Point
    glVertex3f(-1.0, -1.0, -1.0)
    glEnd()

    # Kanan
    glBegin(GL_POLYGON)
    glColor3f(rgb(166),rgb(0),rgb(0))
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(0.0, 1.0, 0.0) # Point
    glVertex3f(1.0, -1.0, 1.0)
    glEnd()

    # Kiri
    glBegin(GL_POLYGON)
    glColor3f(rgb(166),rgb(0),rgb(0))
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(0.0, 1.0, 0.0) # Point
    glVertex3f(-1.0, -1.0, 1.0)
    glEnd()

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity() 

    glTranslatef(0, 0, -7.0)
    glRotatef(45.0, 0.0, 1.0, 0.0)

    pivot()

    piramida()

    glutSwapBuffers()
    glFlush()


def reshape(width, height):  
   aspect = width / height
   glViewport(0, 0, width, height)
   glMatrixMode(GL_PROJECTION) 
   glLoadIdentity()            
   gluPerspective(45.0, aspect, 0.1, 100.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Piramida 3D")
    glutDisplayFunc(myDisplay)
    glutReshapeFunc(reshape)
   
    init()
    glutMainLoop()

main()


