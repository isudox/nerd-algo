package com.leetcode;

import com.common.TreeNode;

/**
 * 606. Construct String from Binary Tree
 * https://leetcode.com/problems/construct-string-from-binary-tree/
 */
class Problem606 {
    public String tree2str(TreeNode root) {
        if (root == null) return "";
        String left = tree2str(root.left);
        String right = tree2str(root.right);
        if (root.left != null && root.right != null)
            return String.format("%d(%s)(%s)", root.val, left, right);
        if (root.left != null)
            return String.format("%d(%s)", root.val, left);
        if (root.right != null)
            return String.format("%d()(%s)", root.val, right);
        return "" + root.val;
    }
}
