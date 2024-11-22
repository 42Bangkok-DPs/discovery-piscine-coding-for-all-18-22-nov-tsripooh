#!/usr/bin/env python3
from checkmate import *
def main():
    
    board = [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', 'Q', '.', '.'],
        ['.', '.', '.', '.', 'B', '.', '.', '.'],
        ['.', '.', '.', 'K', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.']
    ]
    
    result = is_in_check(board)
    print(result)

if __name__ == "__main__":
    main()