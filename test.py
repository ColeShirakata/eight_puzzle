from variables import user_puzzle, solution


nodes = []
nodes.append(user_puzzle)

def find_zero(puzzle):
    row, col = 0, 0
    for row in range(3):
        for col in range(3):
            print(puzzle.puzzle[row][col])
            if user_puzzle[row][col] == 0:
                return row, col

def expand(pz):
    row, col = find_zero(pz)

    # Move up
    if row > 0 and pz.prev_move != "down":
        child_up = pz.__copy__()
        print(row, col)
        temp = child_up[row-1][col]
        child_up[row][col] = temp
        child_up[row-1][col] = 0
        print(child_up)

    # Move down
    if row < 2 and pz.prev_move != "up":
        child_down = pz.__copy__()
        temp = child_down[row+1][col]
        child_down[row][col] = temp
        child_down[row+1][col] = 0
        print(child_down)
        print(pz.puzzle)    

    # Move left
    if col > 0 and pz.prev_move != "right":
        pass

    # Move right
    if col < 2 and pz.prev_move != "left":
        pass

class node:
    def __init__(self, puzzle):
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.puzzle = puzzle
        self.prev_move = "left"

    def __copy__(self):
        return self.puzzle


    def print(self):
        for i in range(3):
            print(self.puzzle[i])


if __name__ == "__main__":
    
    

    nd = node(user_puzzle)
    expand(nd)

