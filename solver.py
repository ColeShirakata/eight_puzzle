"""
Cole Shirakata
SID-862290103
10-31-2022
"""

from variables import *
import copy
from queue import Queue
from node import *
import sys
import winsound
import time

# Finds the empty space on the puzzle
def find_zero(pz):
    row, col = 0, 0
    for row in range(3):
        for col in range(3):
            if pz.puzzle[row][col] == 0:
                return row, col

# Implementation of the tree data structure
# Finds the empty space and considers valid moves based on location
# Accepts puzzle node
def expand(pz):
    row, col = find_zero(pz)
    global node_count

    # MOVE UP
    # Checks location of zero and the previous move; creates child node by deepcopy
    # Switches location of top value with zero, then makes the puzzle an "up" child node
    if row > 0 and pz.prev_move != "down":
        child_up = copy.deepcopy(pz.puzzle)
        temp = child_up[row-1][col]

        child_up[row][col] = temp
        child_up[row-1][col] = 0

        pz.up = node(child_up)
        pz.up.prev_move = "up"
        node_count += 1

    # MOVE DOWN
    # Checks location of zero and the previous move; creates child node by deepcopy
    # Switches location of bottom value with zero, then makes the puzzle a "down" child node
    if row < 2 and pz.prev_move != "up":
        child_down = copy.deepcopy(pz)
        temp = child_down.puzzle[row+1][col]

        child_down.puzzle[row][col] = temp
        child_down.puzzle[row+1][col] = 0

        pz.down = child_down
        pz.down.prev_move = "down" 
        node_count += 1

    # MOVE LEFT
    # Checks location of zero and the previous move; creates child node by deepcopy
    # Switches location of left value with zero, then makes the puzzle a "left" child node
    if col > 0 and pz.prev_move != "right":
        child_left = copy.deepcopy(pz)
        temp = child_left.puzzle[row][col-1]

        child_left.puzzle[row][col] = temp
        child_left.puzzle[row][col-1] = 0

        pz.left = child_left
        pz.left.prev_move = "left"
        node_count += 1

    # MOVE RIGHT
    # Checks location of zero and the previous move; creates child node by deepcopy
    # Switches location of right value with zero, then makes the puzzle a "right" child node
    if col < 2 and pz.prev_move != "left":
        child_right = copy.deepcopy(pz)
        temp = child_right.puzzle[row][col+1]

        child_right.puzzle[row][col] = temp
        child_right.puzzle[row][col+1] = 0
        
        pz.right = child_right
        pz.right.prev_move = "right"
        node_count += 1

    #Returns the child nodes
    return pz.up, pz.down, pz.left, pz.right

# Prints the puzzle... Simple enough
# Accepts puzzle argument
def print_puzzle(puzzle):
        print("\n---------------")
        for i in range(3):
            for j in range(3):
                print("|", puzzle[i][j], "|", end="")
            print("\n---------------")

        print("\n")

# Compares node to goal state... Also simple enough
# Accepts puzzle node
def test_goal_state(pz):
    solution = True
    for row in range(3):
        for col in range(3):
            if pz.puzzle[row][col] != goal_state[row][col]:
                solution = False

    return solution

# Implementation of the general search algorithm
# Accepts puzzle node and queueing function
def general_search(pz, q_func):
    queue = []
    visited = []
    queue.append(pz)
    visited.append(pz.puzzle)
    cost = 0
    depth = 0

    # Selects the queueing function
    if q_func == 2:
        cost = compute_misplaced(pz)
    elif q_func == 3:
        cost = compute_manhattan(pz)

    pz.cost = cost

    print("Starting Puzzle")
    print_puzzle(pz.puzzle)

    # Beginning of general search algorithm
    while True:
        # Checks if queue is empty
        if not queue:
            return False

        # Sorts the queue with regards to the queueing function (cost)
        # Referenced techiedelight.com for sorting list of objects
        # https://www.techiedelight.com/sort-list-of-objects-python/
        if q_func != 1:
            queue.sort(key=lambda x: x.total_cost())

        node = queue.pop(0)

        # Test if most recent node is the goal node
        if test_goal_state(node):
            print_puzzle(node.puzzle)
            return True

        # Create child nodes using the expand function
        up, down, left, right = expand(node)
        a = [up, down, left, right]

        # Check if child nodes are not in visited and if they have value
        # If so, add to visited[] and queue[] and compute their heuristic costs
        for i in a:
            if i is not None:
                if i.puzzle not in visited:
                    if q_func == 1:
                        i.depth = node.depth+1
                    elif q_func == 2:
                        i.cost = compute_misplaced(i)
                        i.depth = node.depth+1
                    elif q_func == 3:
                        i.cost = compute_manhattan(i)
                        i.depth = node.depth+1
                    visited.append(i.puzzle)
                    queue.append(i)
                
# Misplaced heuristic
# Accepts puzzle node
def compute_misplaced(pz):
    distance = 0
    for i in range(3):
        for j in range(3):
            if pz.puzzle[i][j] != goal_state[i][j] and pz.puzzle[i][j] != 0:
                distance += 1
    return distance
                
# Manhattan heuristic
# Accepts puzzle node
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

# Main
# UI implementation
if __name__ == "__main__":
    function = 0
    
    print("Welcome to my Eight-Puzzle solver!\n")
    print("(1) Would you like to create your own puzzle\n(2) Choose a premade puzzle\n")
    user_input = int(input())
    print("\n")

    print("What queueing function would you like?\n")
    print("(1) Uniform Cost\n(2) A* with misplaced tile\n(3) A* with Manhattan\n")
    function = int(input())

    # Custom puzzle
    if user_input == 1:

        r1, r2, r3 = input("Row 1: ")
        r4, r5, r6 = input("Row 2: ")
        r7, r8, r9 = input("Row 3: ")

        temp_puzzle = [[int(r1), int(r2), int(r3)], [int(r4), int(r5), int(r6)], [int(r7), int(r8), int(r9)]]
        user_puzzle = temp_puzzle

    
    elif user_input == 2:
        print("\nWhich puzzle would you like?\n")
        print("(1) Depth 2\n(2) Depth 4\n(3) Depth 8\n(4) Depth 12\n(5) Depth 16\n(6) Depth 20\n(7) Depth 24")
        inp = int(input())
        if inp == 1:
            user_puzzle = puzzle_01
        elif inp == 2:
            user_puzzle = puzzle_02
        elif inp == 3:
            user_puzzle = puzzle_03
        elif inp == 4:
            user_puzzle = puzzle_04
        elif inp == 5:
            user_puzzle = puzzle_05
        elif inp == 6:
            user_puzzle = puzzle_06
        elif inp == 7:
            user_puzzle = puzzle_07
        
    
    new_node = node(user_puzzle)
    start = float(time.perf_counter())

    if general_search(new_node, function):
        print("Goal Reached!")
        winsound.Beep(frequency, duration)
    else:
        print("Goal not reached")

    end = time.perf_counter()
    total = end - start

    print("Nodes Expanded: %d" % (node_count))
    print("Time: %f" % total)