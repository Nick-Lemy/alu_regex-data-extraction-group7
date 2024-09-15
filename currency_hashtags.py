#!/usr/bin/env python3

import re

# Define regex patterns for currency amounts and hashtags
currency_pattern = r"\$[0-9]{1,3}(?:,[0-9]{3})*(?:\.[0-9]{2})?"
hashtag_pattern = r"#[A-Za-z0-9_]+"

def extract_currency(input_string):
    """Extract all currency amounts from the input string."""
    return re.findall(currency_pattern, input_string)

def extract_hashtags(input_string):
    """Extract all hashtags from the input string."""
    return re.findall(hashtag_pattern, input_string)

if __name__ == '__main__':
    # Prompt the user for input
    user_input = input("Enter a string that contains currency amounts and/or hashtag:")
    currencies = extract_currency(user_input)
    if currencies:
        print("Extracted Currencies:", currencies)
    else:
        print("No valid currencies found.")

    # Extract hashtags
    hashtags = extract_hashtags(user_input)
    if hashtags:
        print("Extracted Hashtags:", hashtags)
    else:
        print("No valid hashtags found.")
