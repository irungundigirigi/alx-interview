#!/usr/bin/python3

def validUTF8(data):
    """
    Checks if the given data is a valid UTF-8 encoding.

    Args:
    - data: A list of integers representing bytes of data.

    Returns:
    - True if data is a valid UTF-8 encoding, else returns False.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # If the byte starts with 0, it's a single byte character
        if num_bytes == 0:
            if byte >> 5 == 0b110:  # 2-byte character
                num_bytes = 1
            elif byte >> 4 == 0b1110:  # 3-byte character
                num_bytes = 2
            elif byte >> 3 == 0b11110:  # 4-byte character
                num_bytes = 3
            elif byte >> 7 == 1:  # Invalid start byte
                return False
        else:
            # If the byte doesn't start with 10, it's not a valid continuation byte
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    # If there are remaining bytes, it's not a valid UTF-8 encoding
    return num_bytes == 0
