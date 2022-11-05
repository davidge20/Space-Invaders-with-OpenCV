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
        self.y = 10

    def getXY(self):
        return [self.x, self.y]

def appStarted(app):
    app.width = 400
    app.height = 400
    app.enemyList = []
    app.enemyDict = dict()
    app.enemyXSet = set()
    app.enemyTime = 0
    app.bulletTime = 0

def keyStarted(app,event):
    pass

def timerFired(app):
    app.enemyTime += 100
    if app.enemyTime == 1000:
         currentEnemy = enemy(app)
         x = currentEnemy.getXY()[0]
         y = currentEnemy.getXY()[1]
         print(x,y)
         if x not in app.enemyXSet:
            app.enemyList = app.enemyList + [[x,y]]
            app.enemyDict[x] = y
            app.enemyXSet.add(x)

         print(app.enemyList)
         print(app.enemyDict)
         app.enemyTime = 0

    for cords in app.enemyList:
        yVal = cords[1]
        yVal += 1
        cords[1] = yVal

    app.bulletTime += 100
    for bullet in app.enemyDict:
        if app.enemyDict[bullet] > app.height:
            for cords in app.enemyList:
                if cords[0] == bullet:
                    app.enemyDict[bullet] = cords[1]
            continue
        app.enemyDict[bullet] += 5
        print(app.enemyDict)

def exampleBullet(app,canvas):
    for bullet in app.enemyDict:
        x = bullet
        y = app.enemyDict[bullet]
        r = 10
        canvas.create_oval(x - r, y - r, x + r, y + r, fill = "green")


def exampleEnemy(app,canvas):
    for enemy in app.enemyList:
        x = enemy[0]
        y = enemy[1]
        r = 15
        canvas.create_oval(x - r, y - r, x + r, y + r, fill = "blue")

def redrawAll(app,canvas):
    exampleEnemy(app,canvas)
    exampleBullet(app, canvas)    

def main():
    runApp(width = 400, height = 400)

if __name__ == "__main__":
    main()
