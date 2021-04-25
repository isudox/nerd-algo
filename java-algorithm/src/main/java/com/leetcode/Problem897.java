package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * 897. Increasing Order Search Tree
 * https://leetcode.com/problems/increasing-order-search-tree/
 *
 * Given the root of a binary search tree, rearrange the tree in in-order so
 * that the leftmost node in the tree is now the root of the tree, and every
 * node has no left child and only one right child.
 *
 * Example 1:
 *
 * Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
 * Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
 *
 * Example 2:
 *
 * Input: root = [5,1,7]
 * Output: [1,null,5,null,7]
 *
 * Constraints:
 *
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
}
