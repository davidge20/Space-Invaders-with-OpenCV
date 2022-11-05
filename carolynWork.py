import math, copy, random
from cmu_112_graphics import * 

class invader:
    def __init__(self):
        self.r = 20

class enemy:
    pass

def appStarted(app):
    app.lives = 3
    app.score = 0
    app.gameOver = False
    #app.enemyList
    #app.bulets
    #app.spaceShip = 

def dotIntersectsPaddle(app):
    # This is a helper function for Controllers
    # Check if the dot intersects the paddle.  To keep this
    # simple here, we will only test that the center of the dot
    # is inside the paddle.  We could be more precise here
    # (that's an interesting exercise!).
    return ((app.paddleX0 <= app.dotCx <= app.paddleX1) and
            (app.paddleY0 <= app.dotCy <= app.paddleY1))

def checkInvaderCollision(app):
    app.I
    pass

#need informantion on how invader bulets are stored first
# def checkEnemyCollision(app):
#     for enemy in app.enemyList:
#         cx = enemy[0]
#         cy = enemy[1]
#         r = 10
#         x0 = cx - r
#         y0 = cy - r
#         x1 = cx + r
#         y1 = cy + r
#         for bulet in app.enemyDict
#     return ()

#app.enemyDict[bullet] += 5
def checkInvaderCollison(app):
    #once the actual invader is made these values would be initialized in app.
    invaderCX = 10
    invaderCY = 10
    invaderWidth = 5
    invaderHeight = 5
    #assuming the invader is a rectagle
    invaderX0 = invaderCX - (invaderWidth / 2)
    invaderX1 = invaderCX + (invaderWidth / 2)
    invaderY0 = invaderCY - (invaderHeight / 2)
    invaderY1 = invaderCY + (invaderHeight / 2)
    #bulet = current x
    #app.enemydict[bulet] = current y
    buletX0 = bulet - r
    buletX1 = bulet + r
    buletY0 = app.enemydict[bulet] - r
    buletY1 = app.enemydict[bulet] + r
    return ((invaderX0 <= buletX0 <= invaderX1) or 
            (invaderX0 <= buletX1 <= invaderX1) or 
            (invaderY0 <= buletY0 <= invaderY1) or 
            (invaderY0 <= buletY1 <= invaderY1))

def drawBorder(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height/10, fill = 'green')
    canvas.create_text(app.width / 4, app.height / 20, 
                        text = f'Score:{app.score}', font = 'courier')
    canvas.create_text(app. width / 1.35, app.height / 20, 
                        text = f'Lives:{app.lives}', font = 'courier')

def drawGameOver(app, canvas):
    canvas.create_text(app.width / 2, app.height / 2, text = 'Game Over!',
                       font = 'courier 20 bold', fill = 'green')
    canvas.create_text(app.width / 2, app.height * (3 / 5),
                       text = 'Press r to restart',
                       font = 'courier 18 bold', fill = 'green')

def drawIntroduction(app, canvas):
    canvas.create_text (app.width / 2, app.height / 2, 
                        text = 'Welcome to Hack 112 Space Invaders!!!', 
                        font = 'courier 12 bold', fill = 'green', )
    canvas.create_text (app.width / 2, app.height * (3 / 5),
                        text = '''Shoot all invading aliens befor they reach 
    you, and aviod their lazer beams.''', 
                        font = 'courier 10', fill = 'green')
    canvas.create_text (app.width / 2, app.height * (4 / 5), 
                        text = 'Press r to start', font = 'courier 10',
                        fill = 'green')

def drawEnemy(app, canvas, cx, cy, r):
    #body
    canvas.create_oval(cx - r * (4 / 3), cy - r, cx + r * (4 / 3), cy + r,
                     fill = 'green')
    #left eye
    canvas.create_oval(cx - r * (5 / 6), cy - r * (4 / 5),
                             cx - r * (1 / 6), cy - r * (1 / 5), fill = 'black')
    # rigth eye
    canvas.create_oval(cx + r * (1 / 6), cy - r * (4 / 5),
                            cx + r * (5 / 6), cy - r * (1 / 5), fill = 'black')

def drawInvader(app, canvas, cx, cy, r):
    pass

def keyStarted(app,event):
    pass

def redrawAll(app,canvas):
    #drawBorder(app, canvas)
    #drawGameOver(app, canvas)
    #drawIntroduction(app, canvas)
    drawEnemy(app, canvas, 200, 200, 100)
    

def main():
    runApp(width = 400, height = 400)

if __name__ == "__main__":
    main()
