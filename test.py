from variables import user_puzzle, goal_state
import copy

nodes = []
nodes.append(user_puzzle)

def find_zero(puzzle):
    row, col = 0, 0
    for row in range(3):
        for col in range(3):
            if user_puzzle[row][col] == 0:
                return row, col

def expand(pz):
    row, col = find_zero(pz)

    # Move up
    if row > 0 and pz.prev_move != "down":
        child_up = copy.deepcopy(pz.puzzle)
        temp = child_up[row-1][col]
        child_up[row][col] = temp
        child_up[row-1][col] = 0
        print_puzzle(child_up)
        print(test_goal_state(child_up))

    # Move down
    if row < 2 and pz.prev_move != "up":
        child_down = copy.deepcopy(pz.puzzle)
        temp = child_down[row+1][col]
        child_down[row][col] = temp
        child_down[row+1][col] = 0
        print_puzzle(child_down)  
        print(test_goal_state(child_down))  

    # Move left
    if col > 0 and pz.prev_move != "right":
        child_left = copy.deepcopy(pz.puzzle)
        temp = child_left[row][col-1]
        child_left[row][col] = temp
        child_left[row][col-1] = 0
        print_puzzle(child_left)
        print(test_goal_state(child_left))

    # Move right
    if col < 2 and pz.prev_move != "left":
        child_right = copy.deepcopy(pz.puzzle)
        temp = child_left[row][col+1]
        child_right[row][col] = temp
        child_right[row][col+1] = 0
        print_puzzle(child_right)
        print(test_goal_state(child_right))

def print_puzzle(puzzle):
        for i in range(3):
            print(puzzle[i])

        print("\n")

def test_goal_state(puzzle):
    solution = True
    for row in range(3):
        for col in range(3):
            if puzzle[row][col] != goal_state[row][col]:
                solution = False

    return solution

class node:
    def __init__(self, puzzle):
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.puzzle = puzzle
        self.prev_move = None


    def print(self):
        for i in range(3):
            print(self.puzzle[i])


if __name__ == "__main__":

    print("Welcome to my Eight-Puzzle solver!\n")
    print("Would you like to create your own puzzle (1) or choose a random puzzle (2)?\n")
    user_input = int(input())
    print("\n")

    if user_input == 1:
        r1, r2, r3 = input("Row 1: ")
        r4, r5, r6 = input("Row 2: ")
        r7, r8, r9 = input("Row 3: ")

        temp_puzzle = [[int(r1), int(r2), int(r3)], [int(r4), int(r5), int(r6)], [int(r7), int(r8), int(r9)]]
        user_puzzle = temp_puzzle


    nd = node(user_puzzle)
    expand(nd)

