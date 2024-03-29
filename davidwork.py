import math, copy, random
from cmu_112_graphics import * 
from PIL import Image

import cv2

# ###############################################################################
# #https://itsourcecode.com/free-projects/opencv/eye-detection-opencv-python-with-source-code/

# # Load the cascade
# face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# # To capture video from webcam. 
# cap = cv2.VideoCapture(0)
# while True:
#     # Read the frame
#     _, img = cap.read()
#     # Convert to grayscale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # Detect the faces
#     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#     print(faces)
#     # Draw the rectangle around each face
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#     # Display
#     cv2.imshow('img', img)
#     # Stop if escape key is pressed
#     k = cv2.waitKey(30) & 0xff
#     if k==27:
#         break
# # Release the VideoCapture object
# cap.release()

def video(app):
    # Read the frame
    _, img = app.cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = app.face_cascade.detectMultiScale(gray, 1.1, 4)
    print(faces)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    cv2.imshow('img', img)

###################################################################
class Invader:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

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
    app.image1 = Image.open("./space.png")
    app.spaceResize = app.image1.resize((app.width, app.height))
    app.backgroundIMG = ImageTk.PhotoImage(app.spaceResize)

    app.image2 = Image.open("./spaceship.png")
    app.shipResize = app.image2.resize((app.width//7, app.height//7))
    app.spaceShip = ImageTk.PhotoImage(app.shipResize)

    app.width = 400
    app.height = 400
    app.enemyList = []
    app.enemyDict = dict()
    app.enemyXSet = set()
    app.enemyTime = 0
    app.bulletTime = 0

    app.player = Invader(app.width//2, y = app.height//2 + app.height//3, r = 10)
    app.dx = 10
    app.playerBullets = []

    app.lives = 3

    app.face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    app.cap = cv2.VideoCapture(0)

def keyPressed(app,event):
    if event.key == "a":
        app.cap.release()
    if event.key == "r":
        app.spaceShip = app.spaceShip.rotate(20)

    if event.key == "e":
        app.spaceShip = app.spaceShip.transpose(Image.ROTATE_90)

    if event.key == 'Space':
        if app.bulletTime > 400:
            app.bulletX, app.bulletY = app.player.x, app.player.y
            app.playerBullets.append([app.bulletX, app.bulletY])
            app.bulletTime = 0

    if event.key == 'Right':
        if app.player.x + app.player.r < app.width:
            app.player.x += app.dx
    if event.key == 'Left':
        if app.player.x - app.player.r > 0:
            app.player.x -= app.dx

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
    bulletY0 = app.enemyDict[bullet] - r
    bulletY1 = app.enemyDict[bullet] + r
    return (((invaderX0 <= bulletX0 <= invaderX1) or 
            (invaderX0 <= bulletX1 <= invaderX1)) and 
            ((invaderY0 <= bulletY0 <= invaderY1) or
            (invaderY0 <= bulletY1 <= invaderY1))) 

def timerFired(app):
    video(app)
    app.bulletTime += 100
    for bullet in app.playerBullets:
        bullet[1] -= 10
        if bullet[1] < 0:
            app.playerBullets.remove(bullet)

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

    for bullet in app.enemyDict:
        if app.enemyDict[bullet] > app.height:
            for cords in app.enemyList:
                if cords[0] == bullet:
                    app.enemyDict[bullet] = cords[1]
            continue
        app.enemyDict[bullet] += 5
        if checkInvaderCollison(app, bullet) == True:
            app.lives -= 1
            print(app.lives)
            del app.enemyDict[bullet]
            break

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

def redrawAll(app,canvas):
    canvas.create_image(app.width//2, app.height//2, image = app.backgroundIMG)
    # canvas.create_image(200, 300, image = app.spaceShip)

    exampleEnemy(app,canvas)
    exampleBullet(app, canvas) 

    canvas.create_oval(app.player.x - app.player.r, app.player.y - app.player.r, 
            app.player.x + app.player.r, app.player.y + app.player.r, fill = "white")

    for bullet in app.playerBullets:
        bulletX = bullet[0]
        bulletY = bullet[1]
        canvas.create_oval(bulletX - app.player.r, bulletY - app.player.r,
                           bulletX + app.player.r, bulletY + app.player.r, fill = "purple")   

def main():
    runApp(width = 400, height = 400)

if __name__ == "__main__":
    main()

