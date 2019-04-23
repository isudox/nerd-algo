from typing import List

from common.tree_node import TreeNode


def tree_node_to_list_pre(tree_node: TreeNode) -> List:
    """
    convert tree node to list by preorder
    :param tree_node:
    :return:
    """
    res = [tree_node.val]
    if tree_node.left:
        res + tree_node_to_list_pre(tree_node.left)
    if tree_node.right:
        res + tree_node_to_list_pre(tree_node.right)
    return res
