#!/usr/bin/python3
'''Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
'''

import sys

def makeChange(coins, total):
    # If the total is 0 or less, return 0
    if total <= 0:
        return 0
    
    # Initialize an array to store the minimum number of coins needed for each total
    min_coins = [sys.maxsize for _ in range(total + 1)]
    min_coins[0] = 0  # Zero coins are needed to make a total of 0
    
    # Get the number of different coin denominations
    num_coins = len(coins)
    
    # Iterate through each possible total
    for curr_total in range(1, total + 1):
        # Iterate through each coin denomination
        for coin_index in range(num_coins):
            # Check if the current coin denomination can be used to make up the current total
            if coins[coin_index] <= curr_total:
                # Calculate the total number of coins needed if the current coin is used
                sub_result = min_coins[curr_total - coins[coin_index]]
                
                # Update the minimum number of coins needed for the current total
                if sub_result != sys.maxsize and sub_result + 1 < min_coins[curr_total]:
                    min_coins[curr_total] = sub_result + 1

    # If the minimum number of coins for the target total is still sys.maxsize, it means it cannot be reached
    if min_coins[total] == sys.maxsize:
        return -1
    # Otherwise, return the minimum number of coins needed for the target total
    return min_coins[total]

