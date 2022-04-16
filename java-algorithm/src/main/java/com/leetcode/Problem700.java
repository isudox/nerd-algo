package com.leetcode;

import com.common.TreeNode;

/**
 *
 */
public class Problem700 {
    public TreeNode searchBST(TreeNode root, int val) {
        TreeNode node = root;
        while (node != null) {
            if (node.val == val) {
                return node;
            }
            if (node.val < val) {
                node = node.right;
            } else {
                node = node.left;
            }
        }
        return null;
    }
}
