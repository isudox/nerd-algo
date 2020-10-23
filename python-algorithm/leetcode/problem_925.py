"""925. Long Pressed Name
https://leetcode.com/problems/long-pressed-name/

Your friend is typing his name into a keyboard.
Sometimes, when typing a character c, the key might get long pressed,
and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible
that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true

Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.

Constraints:

1 <= name.length <= 1000
1 <= typed.length <= 1000
The characters of name and typed are lowercase letters.
"""


class Solution:
    def is_long_pressed_name(self, name: str, typed: str) -> bool:
        def find_same(text: str, start: int) -> int:
            x = text[start]
            while start < len(text):
                if text[start] == x:
                    start += 1
                else:
                    return start - 1
            return start - 1

        n1, n2 = len(name), len(typed)
        i, j = 0, 0
        while i < n1 and j < n2:
            if name[i] == typed[j]:
                next_i = find_same(name, i)
                next_j = find_same(typed, j)
                if next_i - i > next_j - j:
                    return False
                else:
                    i = next_i + 1
                    j = next_j + 1
            else:
                return False
        if i == n1 and j == n2:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.is_long_pressed_name("alex", "aaleex"))  # t
    print(sol.is_long_pressed_name("saeed", "ssaaedd"))  # f
    print(sol.is_long_pressed_name("leelee", "lleeelee"))  # t
    print(sol.is_long_pressed_name("laiden", "laiden"))  # t
    print(sol.is_long_pressed_name("pyplrz", "ppyypllr"))  # f
