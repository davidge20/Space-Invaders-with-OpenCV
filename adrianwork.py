import math, copy, random
from cmu_112_graphics import *

class Invader:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

def onAppStart(app):
    x = app.width//2
    y = app.height//2 + app.height//3
    r = 10
    app.player = Invader(x, y, r)
    app.dx = 10

def onKeyHold(app, keys):
    if ('right' in keys):
        app.player.x += app.dx
    if ('left' in keys):
        app.player.x -= app.dx

def redrawAll(app, canvas):
    canvas.create_oval(app.player.x, app.player.y, app.player.r)

def main():
    runApp()
main()