#!/usr/bin/python3
''' This module checks weirdly formatted dates'''
import re


string = input("Enter data to Test")
pattern = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"

matches = re.findall(pattern, string)
print(matches)
