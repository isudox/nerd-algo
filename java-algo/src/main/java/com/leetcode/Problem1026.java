package com.leetcode;

import com.common.TreeNode;

/**
 * 1026. Maximum Difference Between Node and Ancestor
 * https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
 */
class Problem1026 {
    private int ans = 0;

    public int maxAncestorDiff(TreeNode root) {
        if (root == null) {
            return 0;
        }
        helper(root, root.val, root.val);
        return ans;
    }

    private void helper(TreeNode node, int curMax, int curMin) {
        if (node == null) {
            return;
        }
        ans = Math.max(ans, Math.max(Math.abs(node.val - curMax), Math.abs(node.val - curMin)));
        curMax = Math.max(curMax, node.val);
        curMin = Math.min(curMin, node.val);
        helper(node.left, curMax, curMin);
        helper(node.right, curMax, curMin);
    }

    public int maxAncestorDiff2(TreeNode root) {
        if (root == null) {
            return 0;
        }
        dfs(root);
        return ans;
    }

    // find the minimum & maximum val of current TreeNode
    private int[] dfs(TreeNode node) {
        int max = node.val, min = node.val;
        if (node.left == null && node.right == null) {
            return new int[]{max, min};
        }
        if (node.left != null) {
            int[] leftArr = dfs(node.left);
            max = Math.max(max, leftArr[0]);
            min = Math.min(min, leftArr[1]);
            int diff = Math.max(Math.abs(leftArr[0] - node.val), Math.abs(leftArr[1] - node.val));
            if (diff > ans) {
                ans = diff;
            }
        }
        if (node.right != null) {
            int[] rightArr = dfs(node.right);
            max = Math.max(max, rightArr[0]);
            min = Math.min(min, rightArr[1]);
            int diff = Math.max(Math.abs(rightArr[0] - node.val), Math.abs(rightArr[1] - node.val));
            if (diff > ans) {
                ans = diff;
            }
        }
        return new int[]{max, min};
    }
}
