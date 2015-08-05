import sys
import os
import random
import time
from getChar import *
from Board import *
B = Board((7, 24))


class Person(Board):

    def __init__(self):
        Board.__init__(self, (7, 24))
        self.pos = (0, 0)

    def checkWall(self, tup):
        if self.isWall(tup):
            return True
        return False

    def setPos(self, x, y):
        self.pos = (x, y)

    def getPos(self):
        return self.pos


class Pacman(Person):

    def __init__(self, tup, score):
        Person.__init__(self)
        self.pacPos = tup
        self.__myScore = score
        (self.x, self.y) = tup

    def moveTo(self, x, y):
        (self.x, self.y) = (x, y)

    def incrementScore(self):
        self.__myScore += 1

    def totalScore(self):
        return self.__myScore

    def incrementBy(self, val):
        self.__myScore += val


class Ghost(Person, Board):

    def __init__(self, tup):
        Person.__init__(self)
        self.ghostPos = tup

    def moveRandom(self):
        tmpdict = {
            0: 'w',
            1: 'a',
            2: 's',
            3: 'd',
            }
        while True:
            x = random.randrange(0, 4)
            direction = tmpdict[x]
            origpos = B.a[self.ghostPos[0]][self.ghostPos[1]]

            if direction == 'w':
                tmpx = self.ghostPos[0]
                tmpy = self.ghostPos[1] - 1
                if tmpy == 1:
                    continue
                tmppos = B.a[self.ghostPos[0]][self.ghostPos[1] - 1]
                if tmppos == 'X':
                    continue
                elif tmppos == 'C' or tmppos == '.':
                    self.ghostPos = (tmpx, tmpy)
                    B.a[tmpx][tmpy] = 'G'
                    GhostArray[tmpx][tmpy + 1] = '0'
                    GhostArray[tmpx][tmpy] = '1'

                    if B.isCoin(tmpx, tmpy + 1):
                        B.a[tmpx][tmpy + 1] = 'C'
                    elif B.isCoin(tmpx, tmpy + 1) == False:
                        B.a[tmpx][tmpy + 1] = '.'
                    break
                elif tmppos == 'P':
                    return False
            elif direction == 'a':

                tmpx = self.ghostPos[0] - 1
                tmpy = self.ghostPos[1]
                if tmpx == 1:
                    continue
                tmppos = B.a[self.ghostPos[0] - 1][self.ghostPos[1]]
                if tmppos == 'X':
                    continue
                elif tmppos == 'C' or tmppos == '.':
                    self.ghostPos = (tmpx, tmpy)
                    B.a[tmpx][tmpy] = 'G'
                    GhostArray[tmpx + 1][tmpy] = '0'
                    GhostArray[tmpx][tmpy] = '1'
                    if B.isCoin(tmpx + 1, tmpy):
                        B.a[tmpx + 1][tmpy] = 'C'
                    elif B.isCoin(tmpx + 1, tmpy) == False:
                        B.a[tmpx + 1][tmpy] = '.'
                    break
                elif tmppos == 'P':
                    return False
            elif direction == 's':

                tmpx = self.ghostPos[0]
                tmpy = self.ghostPos[1] + 1
                if tmpy == 38:
                    continue
                tmppos = B.a[self.ghostPos[0]][self.ghostPos[1] + 1]
                if tmppos == 'X':
                    continue
                elif tmppos == 'C' or tmppos == '.':
                    self.ghostPos = (tmpx, tmpy)
                    B.a[tmpx][tmpy] = 'G'
                    GhostArray[tmpx][tmpy - 1] = '0'
                    GhostArray[tmpx][tmpy] = '1'
                    if B.isCoin(tmpx, tmpy - 1):
                        B.a[tmpx][tmpy - 1] = 'C'
                    elif B.isCoin(tmpx, tmpy - 1) == False:

                        B.a[tmpx][tmpy - 1] = '.'
                    break
                elif tmppos == 'P':
                    return False
            else:
                tmpx = self.ghostPos[0] + 1
                tmpy = self.ghostPos[1]
                if tmpx == 16:
                    continue
                tmppos = B.a[self.ghostPos[0] + 1][self.ghostPos[1]]
                if tmppos == 'X':
                    continue
                elif tmppos == 'C' or tmppos == '.':
                    self.ghostPos = (tmpx, tmpy)
                    B.a[tmpx][tmpy] = 'G'
                    GhostArray[tmpx - 1][tmpy] = '0'
                    GhostArray[tmpx][tmpy] = '1'
                    if B.isCoin(tmpx - 1, tmpy):
                        B.a[tmpx - 1][tmpy] = 'C'
                    elif B.isCoin(tmpx - 1, tmpy) == False:
                        B.a[tmpx - 1][tmpy] = '.'
                    break
                elif tmppos == 'P':
                    return False


def gameOver(totalScore, levelScore):
    os.system('clear')
    print 'Your Total Score is: %d' % (B.score + prev)
    print 'Level Score is: %d' % B.score
    print 'GAME OVER'
    sys.exit()


if __name__ == '__main__':
    B.create()
    no_of_ghosts = input('Enter number of ghosts:')
    level = 1
    for i in xrange(no_of_ghosts):
        while True:
            x = random.randrange(1, 18)
            y = random.randrange(1, 39)
            if (x, y) != B.pacmanPos and B.isWall((x, y)) == False:
                break
        B.a[x][y] = 'G'
        GhostArray[x][y] = '1'
        g = Ghost((x, y))
        Ghosts.append(g)

    prev = 0
    os.system('clear')
    while True:
        print '\n'
        B.printBoard()
        P = Pacman(B.pacmanPos, prev)

        print 'Total score: ' + str(prev + B.score)
        print 'Enter next move:'
        nextMove = getch()
        if nextMove == 'q':
            sys.exit()
        if nextMove == 'w' and B.isWall((P.x - 1, P.y)) == False:
            if GhostArray[P.x - 1][P.y] == '1':
                gameOver(prev + B.score, B.score)
                break
            B.a[P.x][P.y] = '.'
            if P.x != 1:
                P.x -= 1
            else:
                continue
            if B.isCoin(P.x, P.y):
                B.removeCoin(P.x, P.y)
                B.incrementScore()
            B.pacmanPos = (P.x, P.y)
            P.moveTo(P.x, P.y)
            B.a[P.x][P.y] = 'P'
        elif nextMove == 'a' and B.isWall((P.x, P.y - 1)) == False:
            if GhostArray[P.x][P.y - 1] == '1':
                gameOver(prev + B.score, B.score)
                break
            B.a[P.x][P.y] = '.'
            if P.y != 1:
                P.y -= 1
            else:
                continue
            if B.isCoin(P.x, P.y):
                B.removeCoin(P.x, P.y)
                B.incrementScore()
            B.pacmanPos = (P.x, P.y)
            P.moveTo(P.x, P.y)
            B.a[P.x][P.y] = 'P'
        elif nextMove == 's' and B.isWall((P.x + 1, P.y)) == False:
            if GhostArray[P.x + 1][P.y] == '1':
                gameOver(prev + B.score, B.score)
                break
            B.a[P.x][P.y] = '.'
            if P.x != 16:
                P.x += 1
            else:
                continue
            if B.isCoin(P.x, P.y):
                B.removeCoin(P.x, P.y)
                B.incrementScore()
            B.pacmanPos = (P.x, P.y)
            P.moveTo(P.x, P.y)
            B.a[P.x][P.y] = 'P'
        elif nextMove == 'd' and B.isWall((P.x, P.y + 1)) == False:
            if GhostArray[P.x][P.y + 1] == '1':
                gameOver(prev + B.score, B.score)
                break
            B.a[P.x][P.y] = '.'
            if P.y != 38:
                P.y += 1
            else:
                continue
            if B.isCoin(P.x, P.y):
                B.removeCoin(P.x, P.y)
                B.incrementScore()
            B.pacmanPos = (P.x, P.y)
            P.moveTo(P.x, P.y)
            B.a[P.x][P.y] = 'P'
        for i in Ghosts:
            tmpres = i.moveRandom()
            if tmpres == False:
                gameOver(prev + B.score, B.score)
        os.system('clear')
        if len(B.getAllCoins()) == 0:
            print 'CONGRATULATIONS'
            print 'Level %d completed' % level
            print 'Level Score: %d' % B.score
            P.incrementBy(B.score)
            prev = P.totalScore()
            print 'Total Score: %d' % P.totalScore()
            print 'Loading Level %d ...' % (level + 1)
            time.sleep(2)
            level += 1
            B.score = 0
            os.system('clear')
            B.a[B.pacmanPos[0]][B.pacmanPos[1]] = '.'
            B.create()


			
