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
    app.spa
    pass

def checkEnemyCollision(app):
    pass

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

def keyStarted(app,event):
    pass

def redrawAll(app,canvas):
    drawBorder(app, canvas)
    #drawGameOver(app, canvas)
    drawIntroduction(app, canvas)
    

def main():
    runApp(width = 400, height = 400)

if __name__ == "__main__":
    main()
