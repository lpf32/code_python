import random
import math
class Rotbot(object):
        def __init__(self, identifier, speed = 1):
                self.identifier = identifier
                self.direction = random.choice(range(360))
                self.speed = speed


        def setNewDirection(self):
                self.direction = random.choice(range(360))
        
        def clean(self):
                deltaX = self.speed * math.cos(math.radians(270 - self.direction))
                deltaY = self.speed * math.sin(math.radians(270 - self.direction))
                return (deltaX, deltaY)

        def __str__(self):
                return 'No.' + str(self.identifier) + ' robot'

class Position(object):
        def __init__(self, x, y):
                self.x = x
                self.y = y

        def getX(self):
                return self.x

        def getY(self):
                return self.y

        def __str__(self):
                return '(' + str(self.x) + ', ' + str(self.y) + ')'


class Room(object):
        def __init__(self, w, h):
                self.w = w
                self.h = h
                self.tiles = [(x,y) for x in range(w) for y in range(h)]
                self.cleans = []
                self.robots = {}

        def addRobot(self, r, p = Position(random.random(), random.random())):
                                
                if r in self.robots.keys():
                        raise ValueError('have been added')
                p = Position(random.random() * self.w, random.random() * self.h)
                self.robots[r] = p

        def cleanRoom(self):
                if len(self.robots) == 0:
                        raise  ValueError('no robot')
                while True:
                        for r in self.robots:
                                deltaX, deltaY = r.clean()
                                directionRirght = False

                                while not directionRirght:
                                        if self.robots[r].getX() + deltaX > self.w or self.robots[r].getX() + deltaX < 0 \
                                                or self.robots[r].getY() + deltaY > self.h or self.robots[r].getY() + deltaY < 0:
                                                        r.setNewDirection()
                                        else:
                                                directionRirght = True

                                self.robots[r] = Position(self.robots[r].getX() + deltaX, self.robots[r].getY() + deltaY)
                                rx = int(self.robots[r].getX())
                                ry = int(self.robots[r].getY())
                                #print(rx,ry)
                                if not (rx,ry) in self.cleans:
                                        self.cleans.append((int(self.robots[r].getX()), int(self.robots[r].getY())))

                                print(r),
                                print('locate '),
                                print(self.robots[r])
                                print('cleaned:' + str(self.cleans))

                        #if len(self.tiles) == len(self.cleans):
                                #break


        def isAllClean(self):
                if len(self.tiles) == len(self.cleans):
                        return True
                else:
                        return False


def cleanRoomtest():
        room = Room(7, 8)
        r1 = Rotbot(1)
        room.addRobot(r1)
        room.cleanRoom()


cleanRoomtest()
