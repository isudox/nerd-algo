"""1305. All Elements in Two Binary Search Trees
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
"""
from typing import List

from common.tree_node import TreeNode


def get_all_elements(root1: TreeNode, root2: TreeNode) -> List[int]:
    def dfs(root: TreeNode) -> List[int]:
        if not root:
            return []
        left, right = dfs(root.left), dfs(root.right)
        left.append(root.val)
        left.extend(right)
        return left

    def merge(list1: List[int], list2: List[int]) -> List[int]:
        m, n = len(list1), len(list2)
        i = j = 0
        ret = []
        while i < m and j < n:
            if list1[i] < list2[j]:
                ret.append(list1[i])
                i += 1
            else:
                ret.append(list2[j])
                j += 1
        if i < m:
            ret.extend(list1[i:])
        elif j < n:
            ret.extend(list2[j:])
        return ret

    return merge(dfs(root1), dfs(root2))
