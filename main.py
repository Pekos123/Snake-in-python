from queue import Empty
import readchar, time, msvcrt, random, os
from threading import Thread

class Object:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


# APPLEE: ◉
class Apple:
    def __init__(self, x, y):
        self.skin = '◉'
        self.X = x
        self.Y = y

    def render(self, Map):
        Map[self.Y][self.X] = self.skin


class Game:
    def __init__(self):
        self.rotation = 'right'
        self.skin = '▀'
        self.length = 1

        self.apple = Apple(1, 1)

        self.objects = []

        self.map = [['-','-','-','-','-','-','-','-','-','-'], ['-','-','-','-','-','-','-','-','-','-']]
        self.EmptyMap = [['-','-','-','-','-','-','-','-','-','-'], ['-','-','-','-','-','-','-','-','-','-']]


    def FirstTimeRender(self):
        for i in range(1, 9):
            self.map.insert(i, ['-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-'])
            self.EmptyMap.insert(i, ['-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-'])

        _object = Object(5, 5)
        _object2 = Object(5, 4)
        _object3 = Object(5, 3)

        self.objects.append(_object)
        self.objects.append(_object2)
        self.objects.append(_object3)

        self.PutAppleOnMap()

    def RenderCharacter(self):
        for i in self.objects:
            self.map[i.Y][i.X] = self.skin
            

    def AddNewCharacter(self):
        LastObject = self.objects[len(self.objects)-1]
        _object = Object(LastObject.Y, LastObject.X)
        self.objects.append(_object)

    def CheckIfCharacterPickUpApple(self):
        if self.apple.X == self.objects[0].X and self.apple.Y == self.objects[0].Y:
            #self.AddNewCharacter()
            print("you GOT AN APPLE")
            self.PutAppleOnMap()
            self.length += 1

        return False

    def PutAppleOnMap(self):
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        while self.map[y][x] != ' ':
            x = random.randint(1, 8)
            y = random.randint(1, 8)

        self.apple.X = x
        self.apple.Y = y
        #os._exit(0)

    def RenderMap(self):
        #self.map = self.EmptyMap
        for j in range(1,9):
            self.map[j] = ['-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-']

        self.apple.render(self.map)
        self.MoveCharacter()
        self.RenderCharacter()

        string = ''
        for i in range(0, 10):
            for j in range(0, 10):
                string += self.map[i][j]
            string += '\n'
        print(string)
        #os._exit(0)

    def GetKey(self):
        if msvcrt.kbhit():
            return msvcrt.getch()
        else:
            return None

    def MoveCharacter(self):
        if self.rotation == 'up':
            backY = self.objects[0].Y
            self.objects[0].Y -= 1
            for i in range(1, len(self.objects)):
                backY2 = self.objects[i].Y
                self.objects[i].Y = backY
                backY = backY2

        elif self.rotation == 'down':
            backY = self.objects[0].Y
            self.objects[0].Y += 1
            for i in range(1, len(self.objects)):
                backY2 = self.objects[i].Y
                self.objects[i].Y = backY
                backY = backY2
        elif self.rotation == 'right':
            backX = self.objects[0].X
            self.objects[0].X += 1
            for i in range(1, len(self.objects)):
                backX2 = self.objects[i].X
                self.objects[i].X = backX
                backX = backX2
        elif self.rotation == 'left':
            backX = self.objects[0].X
            self.objects[0].X -= 1
            for i in range(1, len(self.objects)):
                backX2 = self.objects[i].X
                self.objects[i].X = backX
                backX = backX2


    def update(self):
        os.system("cls")
        self.RenderMap()
        self.CheckIfCharacterPickUpApple()

    def GameLoop(self):
        self.time = time.time()
        while True:
            a = time.time()
            if a - self.time >= 0.5: 
                self.update()
                self.time = a

            self.SetRotation(self.GetKey())

    def SetRotation(self, char):
        if str(char) == "b'w'":
            self.rotation = 'up'
        elif str(char) == "b's'":
            self.rotation = 'down'
        elif str(char) == "b'd'":
            self.rotation = 'right'
        elif str(char) == "b'a'":
            self.rotation = 'left'


game = Game()
game.FirstTimeRender()
game.GameLoop()