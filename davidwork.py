import math, copy, random
from cmu_112_graphics import * 

class invader:
    def __init__(self):
        # self.r = 20
        # self.x = app.width//2
        pass

class enemy():
    def __init__(self, app):
        self.x = random.randrange(app.width//6, app.width * 5//6, 40)

        if self.x in app.enemyXSet:
            self.x = random.randrange(app.width//6, app.width * 5//6, 40)

        app.enemyXSet.add(self.x)

        self.y = 10

    def getXY(self):
        return [self.x, self.y]

def appStarted(app):
    app.width = 400
    app.height = 400
    app.enemyList = []
    app.enemyXSet = set()
    app.time = 0

def keyStarted(app,event):
    if event.key == "Up":
        app.invader.dx += 1
    pass

def timerFired(app):
    app.time += 100
    if app.time == 1000:
         app.enemyList = app.enemyList + [(enemy(app).getXY())]
         print(app.enemyList)
         app.time = 0

    for coords in app.enemyList:
        yCord = coords[1]
        yCord += 1
        coords[1] = yCord

def exampleEnemy(app,canvas):
    for enemy in app.enemyList:
        x = enemy[0]
        y = enemy[1]
        r = 10
        canvas.create_oval(x - r, y - r, x + r, y + r, fill = "blue")

def redrawAll(app,canvas):
    exampleEnemy(app,canvas)    

def main():
    runApp(width = 400, height = 400)

if __name__ == "__main__":
    main()
