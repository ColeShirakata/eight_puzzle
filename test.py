from variables import goal_state, node_count, puzzle_01, frequency, duration
import copy
from queue import Queue
from node import *
import winsound

# Finds where 0 is located in the puzzle
def find_zero(pz):
    row, col = 0, 0
    for row in range(3):
        for col in range(3):
            if pz.puzzle[row][col] == 0:
                return row, col

# Creates child nodes based on available moves from parent
def expand(pz):
    row, col = find_zero(pz)
    global node_count

    # Move up
    # Checks location of zero and the previous move; creates child node by deepcopy and moves the zero up
    if row > 0 and pz.prev_move != "down":
        child_up = copy.deepcopy(pz.puzzle)
        temp = child_up[row-1][col]
        child_up[row][col] = temp
        child_up[row-1][col] = 0
        pz.up = node(child_up)
        pz.up.prev_move = "up"
        node_count += 1

    # Move down
    # Checks location of zero and the previous move; creates child node by deepcopy and moves the zero down
    if row < 2 and pz.prev_move != "up":
        child_down = copy.deepcopy(pz)
        temp = child_down.puzzle[row+1][col]
        child_down.puzzle[row][col] = temp
        child_down.puzzle[row+1][col] = 0
        pz.down = child_down
        pz.down.prev_move = "down" 
        node_count += 1

    # Move left
    # Checks location of zero and the previous move; creates child node by deepcopy and moves the zero left
    if col > 0 and pz.prev_move != "right":
        child_left = copy.deepcopy(pz)
        temp = child_left.puzzle[row][col-1]
        child_left.puzzle[row][col] = temp
        child_left.puzzle[row][col-1] = 0
        pz.left = child_left
        pz.left.prev_move = "left"
        node_count += 1

    # Move right
    # Checks location of zero and the previous move; creates child node by deepcopy and moves the zero right
    if col < 2 and pz.prev_move != "left":
        child_right = copy.deepcopy(pz)
        temp = child_right.puzzle[row][col+1]
        child_right.puzzle[row][col] = temp
        child_right.puzzle[row][col+1] = 0
        pz.right = child_right
        pz.right.prev_move = "right"
        node_count += 1

    return pz.up, pz.down, pz.left, pz.right

# Prints the puzzle... Simple enough
def print_puzzle(puzzle):
        for i in range(3):
            for j in range(3):
                print("|", puzzle[i][j], "|", end="")
            print("\n---------------")

        print("\n")

# Compares node to goal state... Also simple enough
def test_goal_state(pz):
    solution = True
    for row in range(3):
        for col in range(3):
            if pz.puzzle[row][col] != goal_state[row][col]:
                solution = False

    return solution

# Implementation of the general search algorithm
def general_search(pz, q_func):
    queue = []
    visited = []
    queue.append(pz)
    visited.append(pz.puzzle)
    cost = 0

    if q_func == 1:
        cost = compute_misplaced(pz)
    elif q_func == 2:
        cost = compute_manhattan(pz)

    pz.cost = cost

    print("Starting Puzzle")
    print_puzzle(pz.puzzle)

    while True:
        if not queue:
            return False

        if q_func != 0:
            queue.sort(key=lambda x: x.cost)

        node = queue.pop(0)

        if test_goal_state(node):
            print_puzzle(node.puzzle)
            return True

        up, down, left, right = expand(node)
        a = [up, down, left, right]

        for i in a:
            if i is not None:
                if i.puzzle not in visited:
                    if q_func == 1:
                        i.cost = compute_misplaced(i)
                    elif q_func == 2:
                        i.cost = compute_manhattan(i)
                    visited.append(i.puzzle)
                    queue.append(i)
                

# Accepts node
def compute_misplaced(pz):
    distance = 0
    for i in range(3):
        for j in range(3):
            if pz.puzzle[i][j] != goal_state[i][j] and pz.puzzle[i][j] != 0:
                distance += 1
    return distance
                

def compute_manhattan(pz):
    distance = 0
    arr = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
    for i in range(3):
        for j in range(3):
            if pz.puzzle[i][j] == 0:
                continue
            else:
                num = pz.puzzle[i][j]
                x, y = arr[num-1]
                distance += (abs(x - i) + abs(y - j))

    return distance




if __name__ == "__main__":
    function = 0
    
    print("Welcome to my Eight-Puzzle solver!\n")
    print("Would you like to create your own puzzle (1) or choose a random puzzle (2)?\n")
    user_input = int(input())
    print("\n")

    print("What queueing function would you like?\n")
    print("0. Standard\n1. A* with misplaced tile\n2. A* with manhattan\n")
    function = int(input())

    if user_input == 1:

        r1, r2, r3 = input("Row 1: ")
        r4, r5, r6 = input("Row 2: ")
        r7, r8, r9 = input("Row 3: ")

        temp_puzzle = [[int(r1), int(r2), int(r3)], [int(r4), int(r5), int(r6)], [int(r7), int(r8), int(r9)]]
        user_puzzle = temp_puzzle

    
    elif user_input == 2:
        user_puzzle = puzzle_01 
    
    new_node = node(user_puzzle)
    if general_search(new_node, function):
        print("Goal reached!")
        winsound.Beep(frequency, duration)
    else:
        print("Goal not reached")

    print("Nodes Expanded: %d" % (node_count))