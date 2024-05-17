package com.leetcode;

import com.common.TreeNode;

/**
 * 2331. Evaluate Boolean Binary Tree
 * https://leetcode.com/problems/evaluate-boolean-binary-tree/
 */
public class Problem2331 {
    public boolean evaluateTree(TreeNode root) {
        if (root.left == null && root.right == null) {
            return root.val == 1;
        }
        boolean left = evaluateTree(root.left);
        boolean right = evaluateTree(root.right);
        return root.val == 3 ? left && right : left || right;
    }
}
