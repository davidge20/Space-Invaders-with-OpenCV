import math, copy, random
from cmu_112_graphics import * 
from PIL import Image

class invader:
    def __init__(self):
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
    #From https://www.tutorialspoint.com/how-to-resize-an-image-using-tkinter
    image = Image.open("./space.png")
    spaceResize = image.resize((app.width, app.height))
    app.backgroundIMG = ImageTk.PhotoImage(spaceResize)

    image = Image.open("./spaceship.png")
    shipResize = image.resize((app.width//7, app.height//7))
    app.spaceShip = ImageTk.PhotoImage(shipResize)

    app.width = 400
    app.height = 400
    app.enemyList = []
    app.enemyDict = dict()
    app.enemyXSet = set()
    app.enemyTime = 0
    app.bulletTime = 0

def keyStarted(app,event):
    if event.key == "r":
        app.spaceShip = app.spaceShip.rotate(20)

    if event.key == "e":
        app.spaceShip = app.spaceShip.transpose(Image.ROTATE_90)

def timerFired(app):
    app.enemyTime += 100
    if app.enemyTime == 1000 and len(app.enemyList) < 7:
         currentEnemy = enemy(app)
         x = currentEnemy.getXY()[0]
         y = currentEnemy.getXY()[1]
         if x not in app.enemyXSet:
            app.enemyList = app.enemyList + [[x,y]]
            app.enemyDict[x] = y
            app.enemyXSet.add(x)

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
    canvas.create_image(app.width//2, app.height//2, image = app.backgroundIMG)
    canvas.create_image(200, 300, image = app.spaceShip)

    exampleEnemy(app,canvas)
    exampleBullet(app, canvas)    

def main():
    runApp(width = 400, height = 400)

if __name__ == "__main__":
    main()
