#!/usr/bin/python3
if __name__ == "__main__":
    s = input()
    for c in s:
        if c.isupper():
            print(c.lower(), end="")
        else:
            print(c.upper(), end="")
    print()