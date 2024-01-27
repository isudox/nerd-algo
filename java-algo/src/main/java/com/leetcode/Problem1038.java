package com.leetcode;

import com.common.TreeNode;

/**
 * 1038. Binary Search Tree to Greater Sum Tree
 * https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
 */
public class Problem1038 {
    private int sum = 0;

    public TreeNode bstToGst(TreeNode root) {
        if (root == null) {
            return null;
        }
        bstToGst(root.right);
        sum += root.val;
        root.val = sum;
        bstToGst(root.left);
        return root;
    }
}
