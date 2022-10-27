

# Class object which holds puzzle
class node:
    def __init__(self, puzzle):
        # up, down, left, right hold the child nodes, if a move isn't valid it holds a null value
        self.cost = 0
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.puzzle = puzzle

        # Holds previous move so it cannot be reversed in the next iteration
        self.prev_move = None


    def print(self):
        for i in range(3):
            print(self.puzzle[i])
