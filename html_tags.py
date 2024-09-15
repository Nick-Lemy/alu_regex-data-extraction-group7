#!/usr/bin/python3
''' This module extracts HTML tags from user input '''
import re

# Prompt the user for input
html_string = input("Enter data to test for HTML tag extraction: ")

# Regex pattern for HTML tags (e.g., <p>, <div class="example">, <img src="image.jpg" alt="description">)
html_pattern = r"<[^>]+>"

# Find all matches for the HTML tag pattern
html_matches = re.findall(html_pattern, html_string)

# Display the found HTML tags
if html_matches:
    print("Extracted HTML tag(s):", html_matches)
else:
    print("No valid HTML tags found.")
