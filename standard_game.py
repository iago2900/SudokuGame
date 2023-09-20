import csv
import random
import numpy as np

def get_puzzle(csv_file_path):
    '''
    Get random puzzle from ddbb.
    '''
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)[1:]  # Skip the first row (header)
        random_row = random.choice(rows)
        return random_row
 
def string2grid(string):
    '''
    Map the string of 81 nubers to get the grid.
    '''
    board_zeroes = np.zeros([9,9], dtype=int)
    board = board_zeroes.copy()
    for i in range(9):
        for j in range(9):
            board[i,j] = string[i*9+j]

    return board

def grid2string(grid):
    '''
    Map the grid to 81 number string.
    '''
    string = ''
    for i in range(9):
        for j in range(9):
            string += str(grid[i,j])
    return string

def check_answer(input, solution):
    """
    Counts the number of different characters at corresponding positions between two strings.

    Returns:
    int: Number of different characters at corresponding positions.
    """
    # Ensure both strings have the same length
    if len(input) != len(solution):
        raise ValueError("Input strings must have the same length")

    # Iterate through the strings and count differing characters
    count = sum(1 for i, j in zip(input, solution) if i != j)

    return count