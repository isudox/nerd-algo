"""717. 1-bit and 2-bit Characters
https://leetcode.com/problems/1-bit-and-2-bit-characters/
"""
from typing import List


def is_one_bit_character(bits: List[int]) -> bool:
    i = 0
    move = False
    while i < len(bits):
        if bits[i] == 0:
            i += 1
            move = True
        else:
            i += 2
            move = False
    return move
