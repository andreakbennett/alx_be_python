#!/usr/bin/env python3
size = int(input("Enter the size of the pattern: "))
if size > 0:
 row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    row += 1
    print()
else:
    print("Please enter a positive integer.")