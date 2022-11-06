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

def checkInvaderCollison(app, bullet):
    r = 10
    invaderX0 = app.player.x - app.player.r
    invaderX1 = app.player.x + app.player.r
    invaderY0 = app.player.y - app.player.r
    invaderY1 = app.player.y + app.player.r
    #bulet = current x
    #app.enemydict[bulet] = current y
    bulletX0 = bullet - r
    bulletX1 = bullet + r
    bulletY0 = app.enemydict[bullet] - r
    bulletY1 = app.enemydict[bullet] + r
    return ((invaderX0 <= bulletX0 <= invaderX1) or 
            (invaderX0 <= bulletX1 <= invaderX1) or 
            (invaderY0 <= bulletY0 <= invaderY1) or 
            (invaderY0 <= bulletY1 <= invaderY1))

def checkEnemyCollision():
    r = 10
    bulletX0 = bullet[0] - r
    bulletX1 = bullet[0] + r
    bulletY0 = bullet[1] - r
    bulletY1 = bullet[1] + r
    for enemy in app.enemyList:
        enemyX0 = enemy[0] - r
        enemyX1 = enemy[0] + r
        enemyY0 = enemy[1] - r
        enemyY1 = enemy[1] + r
        return (((enemyX0 <= bulletX0 <= enemyX1) or 
                (enemyX0 <= bulletX1 <= enemyX1)) and 
                ((enemyY0 <= bulletY0 <= enemyY1) or
                (enemyY0 <= bulletY1 <= enemyY1)))

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
    # left antenna 
    canvas.create_rectangle(cx - r * (1 / 2), cy - r, cx + r * (1 / 2), cy + r,
                            fill = 'green')
    # right antenna
    canvas.crete_rectangle()

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
