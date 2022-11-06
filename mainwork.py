import math, copy, random
from cmu_112_graphics import * 
from PIL import Image
# hi
# import cv2

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
    # From https://www.tutorialspoint.com/how-to-resize-an-image-using-tkinter
    app.image1 = Image.open("./space.png")
    app.spaceResize = app.image1.resize((app.width, app.height))
    app.backgroundIMG = ImageTk.PhotoImage(app.spaceResize)

    #app.image2 = Image.open("./spaceship.png")
    #app.shipResize = app.image2.resize((app.width//7, app.height//7))
    #app.spaceShip = ImageTk.PhotoImage(app.shipResize)
    

    app.width = 400
    app.height = 400
    app.enemyList = []
    app.enemyDict = dict()
    app.enemyXSet = set()
    app.enemyTime = 0
    app.bulletTime = 0

    #
    app.player = Invader(app.width//2, y = app.height//2 + app.height//3, r = 15)
    app.dx = 10
    app.playerBullets = []

    app.lives = 3
    app.score = 0
    app.gameOver = False
    app.showIntro = True
    app.gameStart = False

def keyPressed(app,event):
    if event.key == "r":
        app.showIntro = False
        runApp(width = 400, height = 400)
        app.gameStart = True

    if app.gameOver:
        return

    # if event.key == "r":
    #     app.spaceShip = app.spaceShip.rotate(20)

    # if event.key == "e":
    #     app.spaceShip = app.spaceShip.transpose(Image.ROTATE_90)

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

def checkEnemyCollision(app, bullet):
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
        if (((enemyX0 <= bulletX0 <= enemyX1) or 
                (enemyX0 <= bulletX1 <= enemyX1)) and 
                ((enemyY0 <= bulletY0 <= enemyY1) or
                (enemyY0 <= bulletY1 <= enemyY1))) == True:
            app.enemyList.remove(enemy)
            app.enemyXSet.remove(enemy[0])
            app.score += 10

def timerFired(app):
    if app.score >= 100:
        app.gameOver = True
    if app.lives <= 0:
        app.gameOver = True
        return
    app.bulletTime += 100
    for bullet in app.playerBullets:
        bullet[1] -= 10
        checkEnemyCollision(app, bullet)
        if bullet[1] < 0:
            app.playerBullets.remove(bullet)

    app.enemyTime += 100
    if app.enemyTime == 1000:
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

def drawInvader(app, canvas):
    cx = app.player.x 
    cy = app.player.y
    r = app.player.r
    # top
    canvas.create_oval(cx - r * (6 / 7), cy - r * 1.5, cx + r * (6 / 7),
                        cy - r * (1 / 2), fill = 'blue')
    # body
    canvas.create_oval(cx - r * (5 / 3), cy - r, cx + r * (5 / 3), cy + r,
                        fill = 'yellow')
    # windows
    canvas.create_oval(cx - r * (1 / 5), cy - r * (1 / 5), cx + r * (1 / 5),
                        cy + r * (1 / 5), fill = 'red')
    canvas.create_oval(cx - r * (4 / 5), cy - r * (1 / 5), cx - r * (2 / 5), 
                        cy + r * (1 / 5), fill = 'red')
    canvas.create_oval(cx - r * (7 / 5), cy - r * (1 / 5), cx - r, 
                        cy + r * (1 / 5), fill = 'red')
    canvas.create_oval(cx + r * (4 / 5), cy - r * (1 / 5), cx + r * (2 / 5), 
                        cy + r * (1 / 5), fill = 'red')
    canvas.create_oval(cx + r * (7 / 5), cy - r * (1 / 5), cx + r, 
                        cy + r * (1 / 5), fill = 'red')

def drawEnemy(app, canvas):
    r = 15
    for enemy in app.enemyList:
        cx = enemy[0]
        cy = enemy[1]
    # left antenna 
        canvas.create_rectangle(cx - r * (1 / 2), cy - (r * 1.5), 
                                cx - r * (1 / 4), cy, fill = 'green')
    # right antenna
        canvas.create_rectangle(cx + r * (1 / 2), cy - (r * 1.5), 
                                cx + r * (1 / 4), cy, fill = 'green')
    #body
        canvas.create_oval(cx - r * (4 / 3), cy - r, cx + r * (4 / 3), 
                            cy + r, fill = 'green')
    #left eye
        canvas.create_oval(cx - r * (5 / 6), cy - r * (4 / 5),
                             cx - r * (1 / 6), cy - r * (1 / 5), fill = 'black')
    # rigth eye
        canvas.create_oval(cx + r * (1 / 6), cy - r * (4 / 5),
                            cx + r * (5 / 6), cy - r * (1 / 5), fill = 'black')  

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
    #canvas.create_image(200, 300, image = app.spaceShip)
    if (app.gameOver is False and app.showIntro == True and 
        app.gameStart == False):
        drawIntroduction(app,canvas)

    drawBorder(app, canvas)
    drawEnemy(app, canvas)
    exampleBullet(app, canvas) 
    drawInvader(app, canvas)

    for bullet in app.playerBullets:
        bulletX = bullet[0]
        bulletY = bullet[1]
        canvas.create_oval(bulletX - app.player.r, bulletY - app.player.r,
                           bulletX + app.player.r, bulletY + app.player.r, fill = "purple" )

    if app.gameOver:
        drawGameOver(app,canvas)  

    if app.score >= 100:
        canvas.create_text(app.width//2, app.height * 2//5, text = "Winner!!", 
                        font = "courier 18 bold", fill = 'green') 

def main():
    runApp(width = 400, height = 400)

if __name__ == "__main__":
    main()
