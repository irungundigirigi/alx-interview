#!/usr/bin/python3
"""Rotate a 2D matrix clockwise by 90 degrees"""

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix clockwise by 90 degrees

    Args:
        matrix (list of lists): The 2D matrix to rotate

    Returns:
        None
    """
    # Define indices for top and bottom boundaries
    top_index, bottom_index = 0, len(matrix) - 1

    # Loop until top index crosses bottom index
    while top_index < bottom_index:
        # Iterate through elements in the current loop range
        for i in range(bottom_index - top_index):
            # Store top left value
            top_left = matrix[top_index][top_index + i]
            # Move bottom left to top left
            matrix[top_index][top_index + i] = matrix[bottom_index - i][top_index]
            # Move bottom right to bottom left
            matrix[bottom_index - i][top_index] = matrix[bottom_index][bottom_index - i]
            # Move top right to bottom right
            matrix[bottom_index][bottom_index - i] = matrix[top_index + i][bottom_index]
            # Move top left to top right
            matrix[top_index + i][bottom_index] = top_left
        # Shrink the boundaries for the next loop iteration
        bottom_index -= 1
        top_index += 1

