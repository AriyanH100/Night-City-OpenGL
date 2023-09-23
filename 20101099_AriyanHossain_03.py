from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

def draw_points(x,y):
    glPointSize(5) 
    glBegin(GL_POINTS)
    glColor3f(102.0/255.0, 102.0/255.0, 102.0/255.0)
    glVertex2f(x,y)  
    glEnd()

def draw_points0(x,y):
    glPointSize(5) 
    glBegin(GL_POINTS)
    glColor3f(102.0/255.0, 102.0/255.0, 102.0/255.0)
    glVertex2f(x,y)  
    glEnd()

def draw_points1(x,y):
    glPointSize(5) 
    glBegin(GL_POINTS)
    glColor3f(255.0/255.0, 255.0/255.0, 122.0/255.0)
    glVertex2f(x,y)  
    glEnd()

def draw_points2(x,y):
    glPointSize(3) 
    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(x,y)  
    glEnd()

def draw_points3(x,y):
    glPointSize(3) 
    glBegin(GL_POINTS)
    glColor3f(102.0/255.0, 102.0/255.0, 102.0/255.0)
    glVertex2f(x,y)  
    glEnd()

def draw_points4(x,y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(x,y)  
    glEnd()

def draw_points5(x,y):
    glPointSize(4) 
    glBegin(GL_POINTS)
    glColor3f(242.0/255.0, 253.0/255.0, 58.0/255.0)
    glVertex2f(x,y)  
    glEnd()

def draw_points6(x,y):
    glPointSize(3) 
    glBegin(GL_POINTS)
    glColor3f(242.0/255.0, 253.0/255.0, 58.0/255.0)
    glVertex2f(x,y)  
    glEnd()

def draw_points7(x,y):
    glPointSize(6) 
    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(x,y)  
    glEnd()

def draw_points8(x,y):
    glPointSize(3) 
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(x,y)  
    glEnd()

def draw_points9(x,y):
    glPointSize(1) 
    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(x,y)  
    glEnd()

def draw_points10(x,y):
    glPointSize(3) 
    glBegin(GL_POINTS)
    glColor3f(86.0/255.0, 86.0/255.0, 87.0/255.0)
    glVertex2f(x,y)  
    glEnd()
    
def draw_quads(x1,y1,x2,y2,x3,y3,x4,y4):
    glBegin(GL_QUADS)
    glColor3f(31.0 / 255, 29.0 / 255, 28.0 / 255)
    glVertex2f(x1, y1)   
    glVertex2f(x2, y2)  
    glVertex2f(x3, y3)   
    glVertex2f(x4, y4)   
    glEnd()

def draw_quads0(x1,y1,x2,y2,x3,y3,x4,y4):
    glBegin(GL_QUADS)
    glColor3f(79.0 / 255, 2.0 / 255, 2.0 / 255)
    glVertex2f(x1, y1)   
    glVertex2f(x2, y2)  
    glVertex2f(x3, y3)   
    glVertex2f(x4, y4)   
    glEnd()

def draw_quads1(x1,y1,x2,y2,x3,y3,x4,y4):
    glBegin(GL_QUADS)
    glColor3f(2.0 / 255, 38.0 / 255, 79.0 / 255)
    glVertex2f(x1, y1)   
    glVertex2f(x2, y2)  
    glVertex2f(x3, y3)   
    glVertex2f(x4, y4)   
    glEnd()

def draw_quads2(x1,y1,x2,y2,x3,y3,x4,y4):
    glBegin(GL_QUADS)
    glColor3f(61.0 / 255, 62.0 / 255, 64.0 / 255)
    glVertex2f(x1, y1)   
    glVertex2f(x2, y2)  
    glVertex2f(x3, y3)   
    glVertex2f(x4, y4)   
    glEnd()

def findZone(x1,y1,x2,y2):
    zone=0
    dx=x2-x1
    dy=y2-y1
    if abs(dx)>=abs(dy):
        if dx>=0 and dy>=0:
            zone=0
        if dx<0 and dy>=0:
            zone=3
        if dx<0 and dy<0:
            zone=4
        if dx>=0 and dy<0:
            zone=7
    else:
        if dx>=0 and dy>=0:
            zone=1
        if dx<0 and dy>=0:
            zone=2
        if dx<0 and dy<0:
            zone=5
        if dx>=0 and dy<0:
            zone=6
    return zone

def convertToZone0(x,y,zone):
    if zone==0:
        a=x
        b=y
        return a,b
    elif zone==1:
        a=y
        b=x
        return a,b
    elif zone==2:
        a=y
        b=-x
        return a,b
    elif zone==3:
        a=-x
        b=y
        return a,b
    elif zone==4:
        a=-x
        b=-y
        return a,b
    elif zone==5:
        a=-y
        b=-x
        return a,b
    elif zone==6:
        a=-y
        b=x
        return a,b
    elif zone==7:
        a=x
        b=-y
        return a,b

def convertBack(x,y,zone):
    if zone==0:
        a=x
        b=y
        return a,b
    elif zone==1:
        a=y
        b=x
        return a,b
    elif zone==2:
        a=-y
        b=x
        return a,b
    elif zone==3:
        a=-x
        b=y
        return a,b
    elif zone==4:
        a=-x
        b=-y
        return a,b
    elif zone==5:
        a=-y
        b=-x
        return a,b
    elif zone==6:
        a=y
        b=-x
        return a,b
    elif zone==7:
        a=x
        b=-y
        return a,b

def drawline(x1,y1,x2,y2,*c):
    zone=findZone(x1,y1,x2,y2)
    x1,y1=convertToZone0(x1,y1,zone)
    x2,y2=convertToZone0(x2,y2,zone)
    dx=x2-x1
    dy=y2-y1
    d=2*dy-dx
    incE=2*dy
    incNE=2*(dy-dx)
    x=x1
    y=y1
    while True:
        X,Y=convertBack(x,y,zone)
        if c==():
            draw_points(X,Y)
        elif c[0]==0:
            draw_points0(X,Y)
        elif c[0]==1:
            draw_points1(X,Y)
        elif c[0]==2:
            draw_points2(X,Y)
        elif c[0]==7:
            draw_points7(X,Y)
        elif c[0]==10:
            draw_points10(X,Y)
        if d>0:
            d+=incNE
            y+=1
        else:
            d+=incE
        x+=1
        if x==x2 and y==y2:
            break

def MidpointCircle(r,cx,cy,*c):
    d=1-r
    x=0
    y=r
    if c==():
        Circlepoints(x,y,cx,cy)
    elif c[0]==1:
        Circlepoints1(x,y,cx,cy)
    elif c[0]==2:
        Circlepoints2(x,y,cx,cy)
    while x<=y:
        if d<0:
            d+=2*x+3
        else:
            d+=2*x-2*y+5
            y-=1
        x+=1
        if c==():
            Circlepoints(x,y,cx,cy)
        elif c[0]==1:
            Circlepoints1(x,y,cx,cy)
        elif c[0]==2:
            Circlepoints2(x,y,cx,cy)

def Circlepoints(x,y,cx,cy): 

    draw_points5(-x+cx,-y+cy)
    draw_points5(-y+cx,-x+cy)
    draw_points5(-y+cx,x+cy)
    draw_points5(-x+cx,y+cy)

def Circlepoints1(x,y,cx,cy): 
    draw_points8(x+cx,y+cy)
    draw_points8(y+cx,x+cy)
    draw_points8(y+cx,-x+cy)
    draw_points8(x+cx,-y+cy)
    draw_points8(-x+cx,-y+cy)
    draw_points8(-y+cx,-x+cy)
    draw_points8(-y+cx,x+cy)
    draw_points8(-x+cx,y+cy)

def Circlepoints2(x,y,cx,cy): 
    draw_points9(x+cx,y+cy)
    draw_points9(y+cx,x+cy)
    draw_points9(y+cx,-x+cy)
    draw_points9(x+cx,-y+cy)
    draw_points9(-x+cx,-y+cy)
    draw_points9(-y+cx,-x+cy)
    draw_points9(-y+cx,x+cy)
    draw_points9(-x+cx,y+cy)

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

c=110
d=300
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0) 

    #buildings  sheight=100  mheight=170  bheight=220  width=80
    #1
    drawline(0,220,35,220,2)
    drawline(35,220,35,120,2)
    #2
    drawline(50,120,50,340,2)
    drawline(50,340,130,340,2)
    drawline(130,340,130,220,2)
    #3
    drawline(90,120,90,220,2)
    drawline(90,220,170,220,2)
    drawline(170,220,170,120,2)
    #4
    drawline(200,120,200,290,2)
    drawline(200,290,270,290,2)
    #5
    drawline(270,120,270,340,2)
    drawline(270,340,350,340,2)
    drawline(350,340,350,120,2)
    #6
    drawline(380,120,380,220,2)
    drawline(380,220,460,220,2)
    drawline(460,220,460,120,2)
    #7
    drawline(480,120,480,290,2)
    drawline(480,290,560,290,2)
    #behind buildings
    drawline(0,270,48,270,10)
    drawline(133,250,198,250,10)
    drawline(353,280,420,280,10)
    drawline(420,280,420,222,10)
    drawline(420,251,477,251,10)
    
    #street
    drawline(0,120,500,120)
    draw_quads(0,0,0,120,500,120,500,0)

    #windows  square=10  top=20 side=15  gap=50
    #1
    w=1 if c>100 and c<300 else 0
    drawline(10,200,20,200,w)
    drawline(20,200,20,190,w)
    drawline(20,190,10,190,w)
    drawline(10,190,10,200,w)
    
    drawline(10,150,20,150)
    drawline(20,150,20,140)
    drawline(20,140,10,140)
    drawline(10,140,10,150)
    #2
    w=1 if c>150 and c<250 else 0
    drawline(65,320,75,320,w)
    drawline(75,320,75,310,w)
    drawline(75,310,65,310,w)
    drawline(65,310,65,320,w)

    w=1 if c>50 and c<170 else 0
    drawline(65,270,75,270,w)
    drawline(75,270,75,260,w)
    drawline(75,260,65,260,w)
    drawline(65,260,65,270,w)

    drawline(65,220,75,220)
    drawline(75,220,75,210)
    drawline(75,210,65,210)
    drawline(65,210,65,220)

    drawline(65,170,75,170,1)
    drawline(75,170,75,160,1)
    drawline(75,160,65,160,1)
    drawline(65,160,65,170,1)

    drawline(105,320,115,320,1)
    drawline(115,320,115,310,1)
    drawline(115,310,105,310,1)
    drawline(105,310,105,320,1)

    drawline(105,270,115,270)
    drawline(115,270,115,260)
    drawline(115,260,105,260)
    drawline(105,260,105,270)
    #3
    drawline(105,200,115,200,1)
    drawline(115,200,115,190,1)
    drawline(115,190,105,190,1)
    drawline(105,190,105,200,1)
    
    drawline(105,150,115,150)
    drawline(115,150,115,140)
    drawline(115,140,105,140)
    drawline(105,140,105,150)

    drawline(145,200,155,200)
    drawline(155,200,155,190)
    drawline(155,190,145,190)
    drawline(145,190,145,200)
    
    drawline(145,150,155,150,1)
    drawline(155,150,155,140,1)
    drawline(155,140,145,140,1)
    drawline(145,140,145,150,1)
    #4 
    w=1 if c>110 and c<400 else 0
    drawline(215,270,225,270,w)
    drawline(225,270,225,260,w)
    drawline(225,260,215,260,w)
    drawline(215,260,215,270,w)

    drawline(215,220,225,220,1)
    drawline(225,220,225,210,1)
    drawline(225,210,215,210,1)
    drawline(215,210,215,220,1)
    
    drawline(215,170,225,170)
    drawline(225,170,225,160)
    drawline(225,160,215,160)
    drawline(215,160,215,170)

    drawline(255,270,265,270)
    drawline(265,270,265,260)
    drawline(265,260,255,260)
    drawline(255,260,255,270)

    drawline(255,220,265,220)
    drawline(265,220,265,210)
    drawline(265,210,255,210)
    drawline(255,210,255,220)

    w=1 if c>160 and c<430 else 0
    drawline(255,170,265,170,w)
    drawline(265,170,265,160,w)
    drawline(265,160,255,160,w)
    drawline(255,160,255,170,w)
    #5
    w=1 if c>210 and c<390 else 0
    drawline(285,320,295,320,w)
    drawline(295,320,295,310,w)
    drawline(295,310,285,310,w)
    drawline(285,310,285,320,w)

    drawline(285,270,295,270)
    drawline(295,270,295,260)
    drawline(295,260,285,260)
    drawline(285,260,285,270)

    drawline(285,220,295,220,1)
    drawline(295,220,295,210,1)
    drawline(295,210,285,210,1)
    drawline(285,210,285,220,1)

    drawline(285,170,295,170)
    drawline(295,170,295,160)
    drawline(295,160,285,160)
    drawline(285,160,285,170)

    drawline(325,320,335,320)
    drawline(335,320,335,310)
    drawline(335,310,325,310)
    drawline(325,310,325,320)

    drawline(325,270,335,270)
    drawline(335,270,335,260)
    drawline(335,260,325,260)
    drawline(325,260,325,270)

    w=1 if c>260 and c<420 else 0    
    drawline(325,220,335,220,w)
    drawline(335,220,335,210,w)
    drawline(335,210,325,210,w)
    drawline(325,210,325,220,w)

    drawline(325,170,335,170,1)
    drawline(335,170,335,160,1)
    drawline(335,160,325,160,1)
    drawline(325,160,325,170,1)
    #6
    w=1 if c>230 and c<410 else 0
    drawline(395,200,405,200,w)
    drawline(405,200,405,190,w)
    drawline(405,190,395,190,w)
    drawline(395,190,395,200,w)

    w=1 if c>260 and c<430 else 0
    drawline(395,150,405,150,w)
    drawline(405,150,405,140,w)
    drawline(405,140,395,140,w)
    drawline(395,140,395,150,w)

    w=1 if c>330 and c<450 else 0
    drawline(435,200,445,200,w)
    drawline(445,200,445,190,w)
    drawline(445,190,435,190,w)
    drawline(435,190,435,200,w)

    w=1 if c>390 and c<500 else 0
    drawline(435,150,445,150,w)
    drawline(445,150,445,140,w)
    drawline(445,140,435,140,w)
    drawline(435,140,435,150,w)

    #moon
    MidpointCircle(20,150,420)

    #divider
    drawline(0,60,30,60,7)
    drawline(80,60,130,60,7)
    drawline(180,60,230,60,7)
    drawline(280,60,330,60,7)
    drawline(380,60,430,60,7)
    drawline(480,60,500,60,7)
    
    #cars
    #1
    #c=110
    drawline(c-60,20,c,20,2)
    drawline(c-60,20,c-60,35,2)
    drawline(c-60,35,c-50,35,2)
    drawline(c-50,35,c-40,45,2)
    drawline(c-40,45,c-25,45,2)
    drawline(c-25,45,c-10,35,2)
    drawline(c-10,35,c,35,2)
    drawline(c,35,c,20,2)
    
    drawline(c-50,35,c-10,35,2)
    draw_quads0(c-60,21,c-60,34,c,34,c,21)
    draw_quads2(c-50,35,c-40,45,c-25,45,c-10,35)

    MidpointCircle(5,c-50,12,1)
    MidpointCircle(2,c-50,12,1)
    MidpointCircle(5,c-10,12,1)
    MidpointCircle(2,c-10,12,1)
    MidpointCircle(6,c-50,12,2)
    MidpointCircle(6,c-10,12,2)

    draw_points6(c+2,25)
    draw_points6(c+6,25)

    #2
    #d=300
    drawline(d,80,d+60,80,2)
    drawline(d,80,d,95,2)
    drawline(d,95,d+10,95,2)
    drawline(d+10,95,d+25,105,2)
    drawline(d+25,105,d+40,105,2)
    drawline(d+50,95,d+40,105,2)
    drawline(d+50,95,d+60,95,2)
    drawline(d+60,95,d+60,80,2)
    
    drawline(d+10,95,d+50,95,2)
    draw_quads1(d,81,d,94,d+60,94,d+60,81)
    draw_quads2(d+10,95,d+25,105,d+40,105,d+50,95)

    MidpointCircle(5,d+10,72,1)
    MidpointCircle(2,d+10,72,1)
    MidpointCircle(5,d+50,72,1)
    MidpointCircle(2,d+50,72,1)
    MidpointCircle(6,d+10,72,2)
    MidpointCircle(6,d+50,72,2)
    
    draw_points6(d-2,85)
    draw_points6(d-6,85)

    # stars
    for i in range(15):
        x=random.randint(0,500)
        y=random.randint(350,500)
        draw_points4(x,y)
    for i in range(2):
        x=random.randint(0,40)
        y=random.randint(280,330)
        draw_points4(x,y)
    for i in range(1):
        x=random.randint(140,190)
        y=random.randint(260,280)
        draw_points4(x,y)
    for i in range(3):
        x=random.randint(140,260)
        y=random.randint(300,330)
        draw_points4(x,y)
    for i in range(2):
        x=random.randint(360,480)
        y=random.randint(290,330)
        draw_points4(x,y)

    glutSwapBuffers()

def animate():
    time.sleep(0.001)
    global c
    global d
    c+=10
    if c>500:
        c=0
    d-=9
    if d<=0:
        d=500
    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"City at Night")
glutDisplayFunc(showScreen)
glutIdleFunc(animate)

glutMainLoop()

