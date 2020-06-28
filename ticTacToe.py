class TicTacToe:
    board = None
    def __init__(self):
        self.player = "X"
        self.board = [[0 for i in range(3)]for j in range(3)]
        for i in range(3):
            for j in range(3):
                self.board[i][j]=(i*3+j)+1
        self.printBoard()
        while True:
            isMarkerPositionCorrect = False
            while not isMarkerPositionCorrect:
                print(self.player,"'s turn to play")
                isMarkerPositionCorrect = self.placeMarker()
            self.printBoard()
            if self.isBoardFull():
                print("DRAW")
                return
            if self.isWinner(self.player):
                print(self.player,"is the winner")
                return
            self.changePlayer()

    def placeMarker(self):
        print("Enter a position (0-8): ")
        position = int(input())-1
        y = position%3
        x = position//3
        if x<0 or x>=3 or y<0 or y>=3:
            print("Error! x and y should be between 0 and 3")
            self.printBoard
            print("Try again")
            return False
        if self.board[x][y]!=(x*3+y)+1:
            print("Error! Position already filled.")
            self.printBoard
            print("Try again")
            return False
        self.board[x][y]=self.player
        return True

    def changePlayer(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def printBoard(self):
        print("_____")
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                print(self.board[i][j],end=" ")
            print()
        print("_____")
    
    def isBoardFull(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j]!='X' and self.board[i][j]!='O':
                    return False
        return True

    def isWinner(self,currentPlayer):
        if self.checkRows(currentPlayer) or self.checkCols(currentPlayer) or self.checkDiagonals(currentPlayer):
            return True
        else:
            return False

    def checkRows(self,currentPlayer):
        for i in range(3):
            if self.board[i][0]==self.board[i][1]==self.board[i][2]==currentPlayer:
                return True
        return False

    def checkCols(self,currentPlayer):
        for i in range(3):
            if self.board[0][i]==self.board[1][i]==self.board[2][i]==currentPlayer:
                return True
        return False
    
    def checkDiagonals(self,currentPlayer):
        if self.board[0][0]==self.board[1][1]==self.board[2][2]==currentPlayer:
            return True
        elif self.board[0][2]==self.board[1][1]==self.board[2][0]==currentPlayer:
            return True
        return False
    # def initialize(self):
    #     self.player = "X" 
    #     self.printBoard(self.board)


if __name__ == "__main__":
    tic = TicTacToe()
    