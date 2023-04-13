package com.leetcode;

import com.common.TreeNode;

/**
 * 101. Symmetric Tree
 * https://leetcode.com/problems/symmetric-tree/
 */
public class Problem101 {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        return check(root.left, root.right);
    }

    private boolean check(TreeNode a, TreeNode b) {
        if (a == null && b == null) {
            return true;
        }
        if (a == null || b == null) {
            return false;
        }
        if (a.val != b.val) {
            return false;
        }
        return check(a.left, b.right) && check(a.right, b.left);
    }
}
