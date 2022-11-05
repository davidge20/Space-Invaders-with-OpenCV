import math, copy, random
from cmu_112_graphics import * 

class invader:
    def __init__(self):
        self.r = 20
        self.x = app.width//2
        self.y 

class enemy:
    pass

def appStarted(app):
    app.width = 400
    app.height = 400
    app.invaderdx = 0
    pass

def keyStarted(app,event):
    if event.key == "Up":
        invader.dx += 1
    pass

def redrawAll(app,canvas):
    pass

def main():
    runApp(width = 400, height = 400)

if __name__ == "__main__":
    main()