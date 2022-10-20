

class node:
    def __init__(self, puzzle):
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.puzzle = puzzle
        self.prev_move = "left"

    def __copy__(self):
        return type(self)(self.puzzle)

    def print(self):
        for i in range(3):
            print(self.puzzle[i])
