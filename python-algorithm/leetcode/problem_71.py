"""71. Simplify Path
https://leetcode.com/problems/simplify-path/

Given an absolute path for a file (Unix-style), simplify it.
Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory.
Furthermore, a double period .. moves the directory up a level.

Note that the returned canonical path must always begin with a slash /,
and there must be only a single slash / between two directory names.
The last directory name (if it exists) must not end with a trailing /. Also,
the canonical path must be the shortest string representing the absolute path.

Example 1:

Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op,
as the root level is the highest level you can go.
"""


class Solution:
    def simplify_path(self, path: str) -> str:
        # TODO
        return ''
