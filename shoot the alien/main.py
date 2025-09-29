import pgzrun

WIDTH=500
HEIGHT=500

TITLE="SHOOT THE ALIEN"



a=Actor("alien")


def a_pos():
    a.x=(50,450)
    a.y=(50,450)

def draw():
    screen.fill(color=(67,167,167))
    a.draw()


a_pos()
pgzrun.go()