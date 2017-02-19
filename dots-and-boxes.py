import sys

"""

.   .   .   .
             
.   .   .   .
             
.   .   .   . 


"""

## Classes

class Board:

	def __init__(self, n = 0, m = 0):
		self.board = self.__createBoard(n, m)

		

	def __createBoard(self, n, m):
		board = []
		for i in xrange(n -1):
			board += [[]]
			for j in xrange(m - 1):
				board[-1].append(Box())


		upperEdges = []
		for j in range(m - 1):
			# print (j, j + 1)
			upperEdges.append(Edge((0, j), (0, j + 1)))

		for i in range(n -1):
			lowerEdges = []
			for j in range(m - 1):
				lowerEdges.append(Edge((i + 1, j), (i + 1, j + 1)))


			horizontalEdges = []
			## Horizontal Vertexes
			for j in range(m):
				horizontalEdges.append(Edge((i, j), (i + 1, j)))


			## Fill Boxes
			for j in range(m - 1):
				board[i][j].edges = [upperEdges[j], 
				horizontalEdges[j], horizontalEdges[j + 1], 
				lowerEdges[j]]


			## End
			upperEdges = lowerEdges

		return board

	def inputBoard(self, stringBoard):
		m = stringBoard.split("|")[0].count(".")
		n = stringBoard.count(".") / m
		
		stringBoard = stringBoard.upper().replace(".", "").split("|")
		self.board = self.__createBoard(n, m)
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				self.board[i][j].edges[0].marked = stringBoard[i * 2][j] == "X" 			   # UP
				self.board[i][j].edges[1].marked = stringBoard[i * 2 + 1][j * 2] == "X"        # LEFT
				self.board[i][j].edges[2].marked = stringBoard[i * 2 + 1][(j + 1) * 2] == "X"  # RIGHT
				self.board[i][j].edges[3].marked = stringBoard[(i + 1) * 2][j] == "X"  		   # DOWN

				self.board[i][j].player = stringBoard[i * 2 + 1][j * 2 + 1].replace("*","")    # Marked

class Box:
	
	def __init__(self):
		self.edges = [] # UP LEFT RIGHT DOWN
		self.player = ""

	def listVertexes(self):

		vertexes = []
		for i in self.edges:
			vertexes += i.listVertexes()

		return vertexes

	def toString(self):
		return "".join([i.toString() for i in self.edges])

class Edge:
	
	def __init__(self, vertex1 = (), vertex2 = ()):
		self.vertex1 = vertex1
		self.vertex2 = vertex2
		self.marked = False

	def listVertexes(self):
		return [self.vertex1, self.vertex2]

	def toString(self):
		return str([str(self.vertex1), str(self.vertex2)])

## Functions
		
def nextMove():
	x, y = 0, 0
	return (x, y)


## Input

if __name__ == "__main__":
	args = sys.argv[1:]

	if (len(args) != 2):
		raise ValueError("Invalid Arguments")

	b =  Board()

	print "\n\n"

	b.inputBoard(args[1])

	# print len(b.board)
	# print b.board[1][0].player

	# print b.board[0][0].toString()
	# print b.board[0][0].listVertexes()
	# print (1, 0) in b.board[0][0].listVertexes()

	# print b.board[0][0].edges[2].vertex1
	# print b.board[0][1].edges[1].vertex1
	# b.board[0][0].edges[2].vertex1 = "a"
	# print b.board[0][1].edges[1].vertex1
