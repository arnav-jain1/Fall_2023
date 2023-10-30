from solver import Board
import os
def main():
    for file in sorted(os.listdir(".")):
        if file.endswith(".txt"):
            sudoku = []
            print("Solving " + file)
            with open(file) as f:
                lines = f.readlines()

            for line in lines:
                board_line = []
                for elem in line:
                    if elem in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        board_line.append(int(elem))
                    elif elem == "_":
                        board_line.append(0)
                sudoku.append(board_line)

            solve = Board(sudoku)
            solve.solve()
            print()
main()