import random, os
no_of_ghosts = 5
GhostArray = [["0" for x in xrange(40)] for x in xrange(18)]
Ghosts=[]

class Board(object):
	"""Board class takes care of generating board and positions of Pacman, walls, ghosts and coins"""
	def __init__(self,pacinit):
		self.pacmanPos=pacinit
		self.__coins=[]
		self.Walls=[]
		self.score=0
		self.a = [["." for x in xrange(40)] for x in xrange(18)]
	def create(self):
		self.createWalls()
		self.createCoins()
		
	def getAllCoins(self):
		return self.__coins

	def addCoin(self, x, y):
		self.__coins.append((x,y))
	
	def isWall(self, tup):
		if(self.Walls.__contains__(tup)):
			return True
		return False
	
	def isCoin(self, x, y):
		if(self.__coins.__contains__((x,y))):
			return True
		return False
	
	def createWalls(self):
		for i in xrange(18):
			self.a[i][0]='X'
			self.a[i][39]='X'
			self.Walls.extend([(i,0),(i,39)])	
		for i in xrange(7,12):
			self.a[i][8]='X'
			self.a[i][30]='X'
			self.Walls.extend([(i,8),(i,30)])	
		for i in xrange(4,14):
			self.a[i][4]='X'
			self.a[i][35]='X'
			self.Walls.extend([(i,4),(i,35)])	
		self.a[6][30]='X'
		self.a[8][11]='X'
		self.a[9][11]='X'
		self.a[10][11]='X'
		self.a[9][14]='X'
		self.a[10][14]='X'
		self.a[11][14]='X'
		self.a[8][17]='X'
		self.a[9][17]='X'
		self.a[10][17]='X'
		self.a[8][20]='X'
		self.a[9][20]='X'
		self.a[10][20]='X'
		self.a[9][23]='X'
		self.a[10][23]='X'
		self.a[11][23]='X'
		self.a[8][26]='X'
		self.a[9][26]='X'
		self.a[10][26]='X'
		self.Walls.extend([(6,30),(8,11),(9,11),(10,11),(9,14),(10,14),(11,14),(8,17),(9,17),(10,17),(8,20),(9,20),(10,20),(9,23),(10,23),(11,23),(8,26),(9,26),(10,26)])
		for i in xrange(8,15):
			self.a[6][i]='X'
			self.Walls.append((6,i))
		for i in xrange(24,30):
			self.a[11][i]='X'
			self.Walls.append((11,i))
		for i in xrange(8,31):
			self.a[4][i]='X'
			self.a[13][i]='X'
			self.Walls.extend([(4,i),(13,i)])
		for i in xrange(40):
			self.a[0][i]='X'
			self.a[17][i]='X'
			self.Walls.extend([(0,i),(17,i)])

	def createCoins(self):	
		for i in xrange(15):
			x1=random.randrange(0,40)
       	 		y1=random.randrange(0,18)
        		choice=random.randrange(0,2)
        		if(choice):
               	 		x2=random.randrange(0,40-x1)+x1
               	 		y2=y1
                		for j in xrange(x1,x2+1):
                        		if(self.a[y1][j]!='X' and (y1,j)!=self.pacmanPos):
                                		self.a[y1][j]='C'
						if(self.isCoin(y1,j)==False):
							self.__coins.append((y1,j))
        		else:
                		y2=random.randrange(0,18-y1)+y1
                		x2=x1
                		for j in xrange(y1,y2+1):
                        		if(self.a[j][x1]!='X' and (j,x1)!=self.pacmanPos):
                               			self.a[j][x1]='C'
						if(self.isCoin(j,x1)==False):
							self.__coins.append((j,x1))
		
		self.a[7][24]='P'
		self.pacmanPos=(7,24)
			
	def printBoard(self):
		for i in xrange(18):
			for j in xrange(40):
				if(self.pacmanPos==(i,j)):
					print "P ",
				elif(GhostArray[i][j]=="1"):
				 	print "G ",
				elif(self.isCoin(i,j)):
					print "C ",
				else:
					print self.a[i][j]+" ",
			print "\n"
	def incrementScore(self):
		self.score += 1

	def removeCoin(self, x, y):
		self.__coins.remove((x, y))
		self.a[x][y]='.'


