package com.leetcode;

import com.common.TreeNode;

/**
 * 814. Binary Tree Pruning
 * https://leetcode.com/problems/binary-tree-pruning/
 */
public class Problem814 {
    public TreeNode pruneTree(TreeNode root) {
        TreeNode dummy = new TreeNode(0, root, null);
        dfs(dummy, root, true);
        return dummy.left;
    }

    private int dfs(TreeNode par, TreeNode node, boolean flag) {
        if (node == null) return 0;
        int left = dfs(node, node.left, true);
        int right = dfs(node, node.right, false);
        int sum = node.val + left + right;
        if (sum == 0) {
            if (flag) {
                par.left = null;
            } else {
                par.right = null;
            }
        }
        return sum;
    }
}
