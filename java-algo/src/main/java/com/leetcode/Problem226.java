package com.leetcode;

import com.common.TreeNode;

/**
 * 226. Invert Binary Tree
 * https://leetcode.com/problems/invert-binary-tree/description/
 */
public class Problem226 {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        TreeNode left = root.left;
        root.left = root.right;
        root.right = left;
        invertTree(root.left);
        invertTree(root.right);
        return root;
    }
}
