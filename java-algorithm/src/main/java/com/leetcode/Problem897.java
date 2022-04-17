package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * 897. Increasing Order Search Tree
 * https://leetcode.com/problems/increasing-order-search-tree/
 * <p>
 * Given the root of a binary search tree, rearrange the tree in in-order so
 * that the leftmost node in the tree is now the root of the tree, and every
 * node has no left child and only one right child.
 * <p>
 * Example 1:
 * <p>
 * Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
 * Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
 * <p>
 * Example 2:
 * <p>
 * Input: root = [5,1,7]
 * Output: [1,null,5,null,7]
 * <p>
 * Constraints:
 * <p>
 * The number of nodes in the given tree will be in the range [1, 100].
 * 0 <= Node.val <= 100
 */
public class Problem897 {
    public TreeNode increasingBst(TreeNode root) {
        TreeNode dummy = new TreeNode(-1), cur = dummy;
        List<TreeNode> stack = new ArrayList<>();
        while (null != root || !stack.isEmpty()) {
            if (null != root) {
                stack.add(root);
                root = root.left;
            } else {
                root = stack.remove(stack.size() - 1);
                root.left = null;
                cur.right = root;
                cur = cur.right;
                root = root.right;
            }
        }
        return dummy.right;
    }

    public TreeNode increasingBst2(TreeNode root) {
        if (root == null) {
            return null;
        }
        TreeNode dummy = new TreeNode(0);
        TreeNode cur = dummy;
        TreeNode node = root;
        Stack<TreeNode> stack = new Stack<>();
        while (!stack.isEmpty() || node != null) {
            while (node != null) {
                stack.add(node);
                node = node.left;
            }
            node = stack.pop();
            node.left = null;
            cur.right = node;
            cur = cur.right;
            node = node.right;
        }
        return dummy.right;
    }
}
