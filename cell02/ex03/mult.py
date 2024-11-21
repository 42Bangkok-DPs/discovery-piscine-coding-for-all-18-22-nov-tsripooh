#!/usr/bin/env python3
print("Enter the first number:")
x = int(input())
print("Enter the second number: ")
y = int(input())
result = x * y
if result > 0:
    print(x,"X",y,"=",result)
    print("The result is positive.")
elif result == 0:
    print(x,"X",y,"=",result)
    print("The result positive and negative.")
else:
    print(x,"X",y,"=",result)
    print("The result is negative.")