#imports
import pgzrun
import random

#define window size
WIDTH=720
HEIGHT=480

#target 1 initialize
target1=Actor("target_red1")
target1.x=WIDTH/2
target1.y=HEIGHT/2

#target 2 initialize
target2=Actor("duck_outline_target_yellow")
target2.right=WIDTH
target2.bottom=HEIGHT

#target 3 initialize
target3=Actor("target_colored")
target3.left=25
target3.top=25



cursor=Actor("crosshair_blue_large")
rifle=Actor("rifle")

score=0


#updates: moving
def update():
    target1.x+=random.randint(1,10)
    target2.x+=random.randint(1,7)
    target3.x+=random.randint(1,13)

    if target1.left>=WIDTH:
        target1.right=0
    if target2.left>=WIDTH:
        target2.right=0
    if target3.left>=WIDTH:
        target3.right=0

def on_mouse_move(pos):
    cursor.pos=pos
    rifle.top=pos[1]
    rifle.left=pos[0]

def on_mouse_down(pos):
    global score
    if cursor.colliderect(target1):
        target1.y=random.randint(0,HEIGHT) 
        target1.x=random.randint(0,WIDTH)
        score +=15
    elif cursor.colliderect(target2):
        target2.y=random.randint(0,HEIGHT) 
        target2.x=random.randint(0,WIDTH)
        score -=50
    elif cursor.colliderect(target3):
        target3.y=random.randint(0,HEIGHT) 
        target3.x=random.randint(0,WIDTH)
        score+=10
        
        



    

#draw the actors
def draw():
    screen.clear()

    target1.draw()
    target2.draw()
    target3.draw()
    cursor.draw()
    rifle.draw()
    screen.draw.text(str(score),(10,10))
pgzrun.go()