package com.leetcode;

import com.common.TreeNode;

/**
 * 1372. Longest ZigZag Path in a Binary Tree
 * https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
 */
public class Problem1372 {
    private int ans = 0;

    public int longestZigZag(TreeNode root) {
        dfs(root);
        return ans;
    }

    private int[] dfs(TreeNode node) {
        int left = 0, right = 0;
        if (node.left != null) { // pick left
            int[] ret = dfs(node.left);
            left = Math.max(left, ret[1] + 1);
        }
        if (node.right != null) { // pick right
            int[] ret = dfs(node.right);
            right = Math.max(right, ret[0] + 1);
        }
        ans = Math.max(ans, Math.max(left, right));
        return new int[]{left, right};
    }
}
