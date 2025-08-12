# import copy

def adjacent ():
    pass

def find_group(board, start_row, start_col, color):
    # Finds all connected stones of the same color starting from a given position
    # checks for the stones of the same color and groups them
    # Returns a set of (row, col) coordinates for the entire connected group

    group = set()
    check_position = [(start_row, start_col)]

    while check_position:
        row, col = check_position.pop()
        if (row, col) in group:
            continue

        if board[row][col] == color:
            group.add((row, col))

            for neighbor in adjacent(row, col):
                if neighbor not in group:
                    check_position.append(neighbor)

    return group
    # pass


def has_liberties(board, group):
    # for row, col in group:
    #     for neighbor_row, neighbor_col in adjacent(row, col):
    #
    #         if board[neighbor_row][neighbor_col] == '.':
    #             return True
    # return False
    pass


def try_move():
   pass