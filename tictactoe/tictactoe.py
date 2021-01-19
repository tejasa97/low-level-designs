class TicTacToe():
    
    class IllegalArgumentException(Exception):
        """Raised if an illegal `row`/`col`/`player` is provided
        """
        ...
    
    def __init__(self, board_size):
        
        self.n = board_size
        self.board = [[0 for i in range(self.n)] for i in range(self.n)]
        
    def move(self, player:int, row:int, col:int):
        
        if row < 0  or col < 0 or row >= self.n or col >= self.n :
            raise self.IllegalArgumentException("Move out of board boundary!")
        elif self.board[row][col] != 0:
            raise self.IllegalArgumentException("Square is already occupied!")
        elif player not in [0, 1]:
            raise self.IllegalArgumentException("Invalid player!")
        
        player = -1 if player is 0 else 1        
        self.board[row][col] = player
        winRow, winCol, winDiag, winRevDiag = True, True, True, True
        
        for i in range(self.n):
            if self.board[row][i] != player:
                winRow = False
            if self.board[i][col] != player:
                winCol = False
            if self.board[i][i] != player:
                winDiag = False
            if self.board[i][self.n-1-i] != player:
                winRevDiag = False
        
        if winCol or winRow or winDiag or winRevDiag:
            return player
        
        return 0