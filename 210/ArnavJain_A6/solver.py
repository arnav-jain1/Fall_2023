#Sudoku Board class
class Board:
    def __init__(self, board):
        '''
        Inputs: board - 2D list of integers 9x9 expected
        Outputs: None
        Function: Initializes the board and sets the size of the board
        '''
        self.board = board
        self.size = 9
        self.box_size = 3
    
    def solve(self):
        '''
        Inputs: None
        Outputs: Solved board if it is solvable
        Function: Calls the recursive function to solve the board and print it if it is solvable
        '''
        #Calls the recursive function to solve the board and print it if it is solvable
        
        if self._recursive_solve():
            self.print_board()
        else:
            print("This board is not solvable")
    
    def _recursive_solve(self):
        '''
        Inputs: Sudoku board
        Outputs: True if the board is solved, False if it is not
        Function: Recursive function to solve the board no inputs, returns True if the board is solved, False if it is not
        '''


        #Base case: if there are no empty squares, the board is solved, return True
        empty_square = self.search_empty()
        if empty_square == None:
            return True
        
        #Recursive case: try all numbers in the empty square

        #Get the coordinates of the empty square
        row, col = empty_square
        for num in range(1, 10):
            #Check if the number is valid
            if self.check_valid(row, col, num):
                #If it is, set the number and call the recursive function
                self.board[row][col] = num
                #If the recursive function returns true, the board is solved and return True
                if self._recursive_solve():
                    return True
                
                #If the recursive function returns false, the number is not valid and set the square back to 0 so that it can be tried again
                self.board[row][col] = 0
        #If all numbers have been tried and none are valid, return False
        return False
    

    def search_empty(self):
        '''
        Inputs: Sudoku board
        Outputs: Coordinates of the first empty square it finds
        Function: Searches for an empty square and returns the coords
        '''

        for row in range(self.size):
            for col in range(self.size):
                #Goes through each square and checks if it is empty
                if self.board[row][col] == 0:
                    #If the square is empty, return the coordinates other wise continue
                    return row, col
        #If no empty squares are found, return None
        return None
        

    def check_valid(self, row, col, num):
        '''
        Inputs: row - row of the square to check
                col - column of the square to check
                num - number to check
        Outputs: True if the number is valid, False if it is not
        Function: Checks if the number is valid in the given square
        '''

        #Check if there is a number in the square already if so return False
        if self.board[row][col] != 0:
            return False
        
        #Check if the number already exists in the row or column if so return False
        for i in range(self.size):
            #Go through each square in the row and column and check if the number is there
            if self.board[row][i] == num:
                return False
            if self.board[i][col] == num:
                return False
            #Check if the number already exists in the box if so return False
        

        #Find the sub-box the square is in by dividing the row and column by the box size (int div)
        box_row = row // self.box_size

        box_col = col // self.box_size

        #Go through each square in the box by doing box_row*box_size to get the starting row and box_col*box_size to get the starting column
        #Then add the box_size to get the ending row and column
        for i in range(box_row*self.box_size, box_row*self.box_size + self.box_size):
            for j in range(box_col*self.box_size, box_col*self.box_size + self.box_size):
                #Go through each square in the box and check if the number is there
                if self.board[i][j] == num:
                    return False
                    #If the number is there, return False

        #If the number is not in the row, column, or box, return True
        return True
    
    def print_board(self):
        '''
        Inputs: Sudoku board
        Outputs: Printed board
        Function: Prints the board
        '''
        for elem in self.board:
            #Print each row of the board
            print(elem)