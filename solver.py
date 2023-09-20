import numpy as np

def board_print(board):
    """
    Prints 9x9 numpy array input board in an easier to read format.
    """
    
    # Some basic checks
    assert board.shape == (9, 9)
    assert type(board) == np.ndarray
    
    # Convert array elements to strings
    board_str = board.astype(str)
    
    # Our row separator
    row_sep = '-'*25

    # Loop through 9 rows
    for i in range(9):
        
        # At each multiple of 3, print row separator
        if i % 3 == 0:
            print(row_sep)

        # Get row data
        row = board_str[i]

        # Print
        print('| '+' '.join(row[0:3])+' | '+' '.join(row[3:6])+' | '+' '.join(row[6:])+' |')

    # Print final row separator at bottom after loops finish
    print(row_sep)


def roundup_to_nearest_three(index):
    roundup_float = np.ceil((index + 1) / 3) * 3 # Add 1 as indices start from 0
    roundup_int = np.int(roundup_float)
    
    return roundup_int

def check_unique(board, row, column):
    # Get distinct values from row and column
    row_values = np.unique(board[row,:])
    col_values = np.unique(board[:,column])
    
    # First define the sub cell that the row/column falls into
    # This will be a group of 3 in each axis
    row_end_pos = roundup_to_nearest_three(row)
    col_end_pos = roundup_to_nearest_three(column)
    
    # Then get distinct values from sub cells
    box_values = np.unique(board[row_end_pos-3:row_end_pos, 
                                 col_end_pos-3:col_end_pos])
    
    # Bring all into one list
    all_values = np.concatenate((row_values, col_values, box_values), axis=None)
    
    # Then take the unique values from all of them
    unique_values = np.unique(all_values)
    
    return unique_values

def solve(board_init):

    board_play = board_init.copy()

    # Restrict to max of 100 loops of the board
    for i in range(100):
        
        # Loop through table columns & rows
        for row in range(9):
            for column in range(9):
                # We're only interested in values not yet filled
                if board_play[row,column] == 0:
                
                    # Check unique numbers in row, column, and sub cell
                    existing_values = check_unique(board_play, row, column)
                    
                    # Get numbers from 1-9 that don't appear in unique numbers list
                    potential_values = [value for value in range(1,10) if value not in existing_values]
                     
                    # If there's only one potential solution, overwrite zero with that value
                    if len(potential_values) == 1:
                        board_play[row,column] = potential_values[0]
                        print('Row: ', str(row + 1), '& Col: ', str(column + 1), ' overwritten with ', str(potential_values[0]))
                    
        print('\n Loop number ', str(i + 1), ' complete \n')
        
        # Checks array for number of non-filled values remaining
        zeroes_remaining = np.count_nonzero(board_play == 0)
        
        if zeroes_remaining == 0:
            print('Finished!')
            break
        else:
            print(' ', str(zeroes_remaining), ' zeroes left\n')
    
    return board_play, zeroes_remaining
