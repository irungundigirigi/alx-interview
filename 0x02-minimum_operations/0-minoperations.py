#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def min_operations(target_chars):
    '''Computes the fewest number of operations needed to result
    in exactly target_chars H characters.
    '''
    if not isinstance(target_chars, int):
        return 0
    operations_count = 0
    clipboard = 0
    done = 1
    # print('H', end='')
    while done < target_chars:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = done
            done += clipboard
            operations_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif target_chars - done > 0 and (target_chars - done) % done == 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            operations_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif clipboard > 0:
            # paste
            done += clipboard
            operations_count += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return operations_count

