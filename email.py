#!/usr/bin/python3
''' This module extracts email addresses from user input '''
import re

# Prompt the user for input
string = input("Enter data to test for email extraction: ")

# Email regex pattern
pattern = r"[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}"

# Find all matches for the email pattern
matches = re.findall(pattern, string)

# Display the found email addresses
if matches:
    print("Extracted email(s):", matches)
else:
    print("No valid email addresses found.")
