class TicTacToe():
    
    class IllegalArgumentException(Exception):
        """Raised if an illegal `row`/`col`/`player` is provided
        """
        ...
    
    def __init__(self, board_size):
        """Inits a Tic Tac Toe board with `board_size` dimensions (square)

        :param board_size: dimensions
        :type board_size: int
        """
        self.n = board_size
        self.board = [[0 for i in range(self.n)] for i in range(self.n)]
        self.row_sum = [0 for i in range(self.n)]
        self.col_sum = [0 for i in range(self.n)]
        self.diag_sum = 0
        self.rev_diag_sum = 0
        
    def move(self, player:int, row:int, col:int):
        """Makes a move for a player

        :param player: 0 or 1
        :type player: int
        :param row: row idx of move
        :type row: int
        :param col: col idx of move
        :type col: int
        :raises self.IllegalArgumentException: raised for several exceptions
        :return: -1, 0, 1
        :rtype: int
        """
        
        if row < 0  or col < 0 or row >= self.n or col >= self.n :
            raise self.IllegalArgumentException("Move out of board boundary!")
        elif self.board[row][col] != 0:
            raise self.IllegalArgumentException("Square is already occupied!")
        elif player not in [0, 1]:
            raise self.IllegalArgumentException("Invalid player!")
        
        player = -1 if player is 0 else 1        
        self.board[row][col] = player
        
        self.row_sum[row] += player
        self.col_sum[col] += player
        
        if row == col:
            self.diag_sum += player
        if row == self.n - 1 - col:
            self.rev_diag_sum += player
        
        if abs(self.row_sum[row]) == self.n or abs(self.col_sum[col]) == self.n or abs(self.diag_sum) == self.n or abs(self.rev_diag_sum) == self.n:
            return player
        
        return 0