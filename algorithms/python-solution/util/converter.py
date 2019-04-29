# -*- coding: utf-8 -*-
from typing import List, Optional

from common.tree_node import TreeNode


class Converter:
    @staticmethod
    def list_to_tree(l: 'List[int]') -> Optional[TreeNode]:
        if l is None or l[0] is None:
            return None

        size = len(l)
        last = size // 2 - 1
        node_list = [TreeNode(l[i]) if l[i] is not None else None for i in range(size)]

        for i in range(last):
            node = node_list[i]
            node.left = node_list[i * 2 + 1]
            node.right = node_list[i * 2 + 2]

        last_node = node_list[last]
        last_node.left = node_list[last * 2 + 1]

        if size % 2 != 0:
            last_node.right = node_list[last * 2 + 2]

        return node_list[0]


if __name__ == "__main__":
    converter = Converter()
    converter.list_to_tree([1, None, 2, 3])
