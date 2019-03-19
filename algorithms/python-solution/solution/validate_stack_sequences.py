# -*- coding: utf-8 -*-
"""946. Validate Stack Sequences
https://leetcode.com/problems/validate-stack-sequences/

Given two sequences pushed and popped with distinct values,
return true if and only if this could have been the result of
a sequence of push and pop operations on an initially empty stack.

Example 1:

  Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
  Output: true
  Explanation: We might do the following sequence:
  push(1), push(2), push(3), push(4), pop() -> 4,
  push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:

  Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
  Output: false
  Explanation: 1 cannot be popped before 2.

Note:

  0 <= pushed.length == popped.length <= 1000
  0 <= pushed[i], popped[i] < 1000
  pushed is a permutation of popped.
  pushed and popped have distinct values.
"""
from typing import List


class Solution:
    def validate_stack_sequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if len(pushed) != len(popped):
            return False
        if len(pushed) == 0 and len(popped) == 0:
            return True

        stack = []
        size = len(pushed)
        pushed_index, popped_index = 0, 0
        while pushed_index < size:
            target = popped[popped_index]
            is_last = popped_index == size - 1
            if pushed[pushed_index] == target:
                # 1. if current num equals to target, then push and pop
                if is_last:
                    break
                popped_index += 1
                pushed_index += 1
            else:
                # 2. if current num doesn't equal to target
                # 2.1. if the top element of stack doesn't equal to target, push
                if len(stack) == 0 or stack[-1] != target:
                    stack.append(pushed[pushed_index])
                    pushed_index += 1
                # 2.2. if the top element of stack equals to target, then pop
                else:
                    stack.pop()
                    popped_index += 1
                    # remind, keep current i, don't add it because no pushing

        for num in reversed(stack):
            if num == popped[popped_index]:
                popped_index += 1
            else:
                return False
        return True
