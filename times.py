#!/usr/bin/env python3

import re

pattern = r'\b((?:[01]\d|2[0-3]):[0-5]\d|(?:0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM))\b'

def extract_times(input_string):
    """Extract all currency amounts from the input string."""
    return re.findall(pattern, input_string)

if __name__ == '__main__':
    # Prompt the user for input
    user_input = input("Enter a string that contains times: ")

<<<<<<< HEAD
for char in match_strings:
    print(f'The time is :{char}')
=======
    # Extract currencies
    currencies = extract_times(user_input)
    if currencies:
        print("Extracted Currencies:", currencies)
    else:
        print("No valid currencies found.")
>>>>>>> b5a40aa861f01c60968a7dc1d30b871e499e91db
