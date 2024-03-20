#!/usr/bin/python3
'''Python 3 Challenge for Minimum Operations'''

def minOperations(n):
    '''Calculates the minimum number of operations required to obtain exactly n 'H' characters in this file.
    Returns:
        Integer: If n is impossible to achieve, return 0.
    '''
    pasted_chars = 1  # Number of characters currently in the file
    clipboard = 0     # Number of 'H's copied
    counter = 0       # Operations counter

    while pasted_chars < n:
        # If nothing has been copied yet
        if clipboard == 0:
            # Copy all
            clipboard = pasted_chars
            # Increment operations counter
            counter += 1

        # If nothing has been pasted yet
        if pasted_chars == 1:
            # Paste
            pasted_chars += clipboard
            # Increment operations counter
            counter += 1
            # Continue to the next iteration
            continue

        remaining = n - pasted_chars  # Remaining characters to be pasted
        # Check if it's impossible by verifying if the clipboard has more 'H's than needed to reach the desired count
        # This condition also implies that the number of characters in the file is equal to or more than the number in the clipboard,
        # which makes achieving n characters impossible.
        if remaining < clipboard:
            return 0

        # If division is not possible
        if remaining % pasted_chars != 0:
            # Paste the current clipboard
            pasted_chars += clipboard
            # Increment operations counter
            counter += 1
        else:
            # Copy all
            clipboard = pasted_chars
            # Paste
            pasted_chars += clipboard
            # Increment operations counter
            counter += 2

    # If the desired result is achieved
    if pasted_chars == n:
        return counter
    else:
        return 0
