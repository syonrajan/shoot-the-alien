import pgzrun
import random

WIDTH=500 #screen width
HEIGHT=500 #screen height

TITLE="SHOOT THE ALIEN"

score=0 #points variable

a=Actor("alien") #image of alien


def a_pos(): #random cordinates for alien
    a.x=(random.randint(50,450)) # random x pos
    a.y=(random.randint(50,450)) #random y pos

def draw(): #draw stuff onto the screen
    screen.fill(color=(67,167,167)) #colour of the background
    a.draw()
    screen.draw.text(message,center=(250,450),fontsize=100) #putting the text(miss/hit) onto the sreen
    screen.draw.text("score:{}".format(score),center=(250,50),fontsize=67) #putting the points to the screen

message=" " 


def on_mouse_down(pos): # to know when you click on the alien with the mouse
    global message
    global score
    if a.collidepoint(pos): #checking if you clicked on the alien
        message="hit" #to put the message on the screen
        a_pos() #calling a random position for the alien
        score=score+5 #adding points to for hitting the alien
    else:
        message="miss" #putting a message on the screen
        score=score-10 #deducting points for missing the alien


a_pos() #to put the alien in a random position at the start
pgzrun.go() #calling the draw funtion
















