'''
Author: Arnav Jain
Program Name: EECS 210 Assignment 6
Function: Sudoku Solver
Inputs: A text file with a sudoku puzzle (5 total)
Outputs: Solved sudoku puzzle (if possible)
Collaborators: None
Other sources: Stack Overflow
Creation Date: 11/09/2023
'''
from solver import Board
import os
def main():
    '''
    Inputs: Sudoku puzzle text files
    Outputs: Solved sudoku puzzle
    Function: Solve a sudoku puzzle
    '''
    #Go through each file in the directory 
    for file in sorted(os.listdir(".")):
        if file.endswith(".txt") and 'puzzle' in file:
            #if the file ends with .txt, solve the sudoku

            #Get an empty list to store the sudoku
            sudoku = []
            
            #Print the puzzle being solved
            print("Solving " + file)
            
            #Open the file and read the lines
            with open(file) as f:
                lines = f.readlines()

            #Go through each line
            for line in lines:
                #Initialize an empty list to store the line
                board_line = []
                for elem in line:
                    #Go through each element in the line and check if it is a number or an empty square
                    if elem in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        board_line.append(int(elem))
                        #If it is a number, add it to the list
                    elif elem == "_":
                        #If it is an empty square, add a 0 to the list
                        board_line.append(0)
                #Add the list to the sudoku list to make a 2d array
                sudoku.append(board_line)

            #Create a board object and solve the sudoku
            solve = Board(sudoku)
            solve.solve()
            #Print a new line to separate the puzzles
            print()
main()
# Call main function