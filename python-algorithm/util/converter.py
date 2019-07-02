# -*- coding: utf-8 -*-
from typing import List, Optional

from common.list_node import ListNode
from common.tree_node import TreeNode


class Converter:
    @staticmethod
    def list_to_tree(l: List[int]) -> Optional[TreeNode]:
        if l is None or l[0] is None:
            return None

        size = len(l)
        last = size // 2 - 1
        node_list = [TreeNode(l[i]) if l[i] is not None else None
                     for i in range(size)]

        for i in range(last):
            node = node_list[i]
            node.left = node_list[i * 2 + 1]
            node.right = node_list[i * 2 + 2]

        last_node = node_list[last]
        last_node.left = node_list[last * 2 + 1]

        if size % 2 != 0:
            last_node.right = node_list[last * 2 + 2]

        return node_list[0]

    @staticmethod
    def list2tree(l: List[int]) -> Optional[TreeNode]:
        if not l:
            return None

        root = TreeNode(int(l[0]))
        node_queue = [root]
        front = 0
        index = 1
        while index < len(l):
            node = node_queue[front]
            front = front + 1

            item = l[index]
            index = index + 1
            if item is not None:
                left_number = int(item)
                node.left = TreeNode(left_number)
                node_queue.append(node.left)

            if index >= len(l):
                break

            item = l[index]
            index = index + 1
            if item is not None:
                right_number = int(item)
                node.right = TreeNode(right_number)
                node_queue.append(node.right)
        return root

    @staticmethod
    def list2node(l: List[int]) -> ListNode:
        node = None
        for ele in l:
            node = ListNode(ele)

        return node
