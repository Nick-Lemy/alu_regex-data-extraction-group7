#!/usr/bin/python3
''' This module extracts URLs from user input '''
import re

# Prompt the user for input
url_string = input("Enter data to test for URL extraction: ")

# Regex pattern for URLs (e.g., http://, https://, etc.)
url_pattern = r"https?://[a-zA-Z\d\.-]+(?:/[^\s]*)?"

# Find all matches for the URL pattern
url_matches = re.findall(url_pattern, url_string)

# Display the found URLs
if url_matches:
    print("Extracted URL(s):", url_matches)
else:
    print("No valid URLs found.")
