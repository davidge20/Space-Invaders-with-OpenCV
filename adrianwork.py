import math, copy, random
from cmu_112_graphics import *
#from cmu_cs3_graphics import *

class Invader:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

def appStarted(app):
    x = app.width//2
    y = app.height//2 + app.height//3
    r = 10
    app.player = Invader(x, y, r)
    app.dx = 10
    app.playerBullets = []
   

def keyPressed(app, event):
    if event.key == 'Space':
        app.bulletX, app.bulletY = app.player.X, app.player.Y
        app.playerBullets.append((app.bulletX, app.bulletY))
    if event.key == 'Right':
        app.player.x += app.dx
        print(app.player.x)
    if event.key == 'Left':
        app.player.x -= app.dx

def timerFired(app):
    for (app.bulletX, app.bulletY) in app.playerBullets:
        app.bulletY -= 10

def redrawAll(app, canvas):
    canvas.create_oval(app.player.x - app.player.r, app.player.y - app.player.r, 
                     app.player.x + app.player.r, app.player.y +app.player.r)
    for (app.bulletX, app.bulletY) in app.playerBullets:
        canvas.create_oval(app.bulletX - app.player.r, app.bulletY - app.player.r,
                           app.bulletX + app.player.r, app.bulletY + app.player.r)

def main():
    runApp()
main()