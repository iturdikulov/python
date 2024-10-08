#!/usr/bin/env python
# Single line comments start with a number symbol.

"""Multiline strings can be written
using three "s, and are often used
as documentation.
"""

####################################################
## 1. Primitive Datatypes and Operators
####################################################

#  ____       _           _ _   _
# |  _ \ _ __(_)_ __ ___ (_) |_(_)_   _____
# | |_) | '__| | '_ ` _ \| | __| \ \ / / _ \
# |  __/| |  | | | | | | | | |_| |\ V /  __/
# |_|   |_|  |_|_| |_| |_|_|\__|_| \_/ \___|

print(
    f"The number {2} is the only even prime number."
)

# Math is what I expect it to be.
print(f"2 + 2 = {2 + 2}")
print(f"7 - (-7) = {7 - (-7)}")
print(f"3 * 4 = 3 + 3 + 3 + 3 = {3 * 4}")
print(f"12 - 3 - 3 - 3 - 3 = 0, here is 4 substracting. 12/4 = {12/4}")

# Floor division rounds towards -> negative infinity
print(f"5 // 3 = {5 // 3}")
print(f"-5 // 3 = {-5 // 3} => 5 // -3 = {5 // -3}")
print(f"-5.0 // 3 = {-5.0 // 3} => 5 // -3 = {5 // -3.0}")

# If there one number is a float, result if float
print(f"10.0 / 3 = {10.0 / 3}")

for i in range(1, 13):
    print(r"\(o_o)/")
    if i % 3 == 0:
        print("---")
