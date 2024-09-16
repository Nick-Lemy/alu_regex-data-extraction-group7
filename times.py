#!/usr/bin/env python3

import re

pattern = r'\b((?:[01]\d|2[0-3]):[0-5]\d|(?:0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM))\b'

def extract_times(input_string):
    """Extract all times from the input string."""
    return re.findall(pattern, input_string)

if __name__ == '__main__':
    # Prompt the user for input
    user_input = input("Enter a string that contains times :")
    times = extract_times(user_input)
    if times:
        print("Extracted times:", times)
    else:
        print("No valid times found.")
