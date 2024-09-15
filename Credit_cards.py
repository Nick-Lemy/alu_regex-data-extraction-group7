#!/usr/bin/python3
import re
pattern = r'^(\d{4}[-\s]?){3}\d{4}$'
usrinput = input("Enter the the credit card number:\n")
matche = re.findall(pattern, usrinput)
print(matche)