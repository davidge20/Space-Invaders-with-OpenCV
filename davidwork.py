import math, copy, random
from cmu_112_graphics import * 

class invader:
    def __init__(self):
        # self.r = 20
        # self.x = app.width//2
        pass

class bullets:
    def __init__(self, app):
        for enemy in app.enemyList:
            self.x = enemy.getXY[0]
            self.y = enemy.getXY[1]
            app.enemyDict[self.x].get()


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
    app.enemyDict = dict()
    app.enemyXSet = set()
    app.time = 0

def keyStarted(app,event):
    if event.key == "Up":
        app.invader.dx += 1
    pass

def timerFired(app):
    app.time += 100
    if app.time == 1000:
         x = enemy(app).getXY()[0]
         y = enemy(app).getXY()[1]
         app.enemyList = app.enemyList + [(enemy(app).getXY())]
         app.enemyDict[x] = y
         print(app.enemyList)
         print(app.enemyDict)
         app.time = 0

    for cords in app.enemyList:
        print(cords)
        cords[1] += 1
        app.enemyDict.get(cords[0],0) + 1
        print(app.enemyDict)

def exampleBullet(app,canvas):
    pass

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
