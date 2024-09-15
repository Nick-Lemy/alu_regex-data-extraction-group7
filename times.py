#!/usr/bin/env python
import re

pattern = r'\b((?:[01]\d|2[0-3]):[0-5]\d|(?:0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM)?)\b'

text_input = input("Enter data to test: ")

match_strings = re.findall(pattern, text_input)

for char in match_strings:
    print(char)