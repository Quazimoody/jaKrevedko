from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global x_rot
global y_rot
global ambient
global green_color
global tree_color
global light_pos


def init():
    global x_rot, y_rot, ambient, green_color, \
        tree_color, light_pos

    x_rot = 0.0
    y_rot = 0.0
    ambient = (1.0, 1.0, 1.0, 1)
    green_color = (0.2, 0.8, 0.0, 0.8)
    tree_color = (0.9, 0.6, 0.3, 0.8)
    light_pos = (1.0, 1.0, 1.0)

    glClearColor(0.1, 0.1, 0.1, 1.0)

    gluOrtho2D(-2.0, 2.0, -1.0, 1.0)
    glRotatef(-90, 1.0, 0.0, 0.0)

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)


def special_keys(key, x, y):
    global x_rot, y_rot

    if key == GLUT_KEY_UP:
        x_rot -= 2.0
    if key == GLUT_KEY_DOWN:
        x_rot += 2.0
    if key == GLUT_KEY_LEFT:
        y_rot -= 2.0
    if key == GLUT_KEY_RIGHT:
        y_rot += 2.0

    glutPostRedisplay()


def draw():
    global x_rot, y_rot, light_pos, \
        green_color, tree_color

    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()
    glRotatef(x_rot, 1.0, 0.0, 0.0)
    glRotatef(y_rot, 0.0, 0.0, 1.0)

    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)

    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, tree_color)
    glTranslatef(0.0, 0.0, -0.7)

    glutSolidCylinder(0.1, 0.2, 120, 120)

    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, green_color)
    glTranslatef(0.0, 0.0, 0.2)

    glutSolidCone(0.5, 0.5, 120, 120)
    glTranslatef(0.0, 0.0, 0.3)
    glutSolidCone(0.4, 0.4, 120, 120)
    glTranslatef(0.0, 0.0, 0.3)
    glutSolidCone(0.3, 0.3, 120, 120)

    glPopMatrix()
    glutSwapBuffers()


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

glutInitWindowSize(1800, 900)
glutInitWindowPosition(50, 50)

glutInit(sys.argv)

glutCreateWindow(b"HP_NW_YR!")

glutDisplayFunc(draw)
glutSpecialFunc(special_keys)
init()

glutMainLoop()
