#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''

import sys

code_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
line_counter = 0

try:
    for line in sys.stdin:
        line_parts = line.split(" ")
        if len(line_parts) > 4:
            status_code = line_parts[-2]
            size = int(line_parts[-1])
            if status_code in code_counts:
                code_counts[status_code] += 1
            total_size += size
            line_counter += 1

        if line_counter == 10:
            line_counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(code_counts.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(code_counts.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

