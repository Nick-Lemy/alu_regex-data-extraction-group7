#!/usr/bin/env python
import re

pattern = r'\b((?:[01]\d|2[0-3]):[0-5]\d|(?:0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM)?)\b'

text = "During the day, I wake up at 06:30 or 6:30 AM, have breakfast around 08:00 or 8:00 AM, and attend a meeting at 13:15 or 1:15 PM. For lunch, I usually take a break at 12:30 or 12:30 PM, hit the gym at 18:45 or 6:45 PM, and enjoy dinner by 19:00 or 7:00 PM. Finally, I start winding down for bed at 22:00 or 10:00 PM and aim to be asleep by 23:59 or 11:59 PM."

match_strings = re.findall(pattern, text)

for char in match_strings:
    print(char)