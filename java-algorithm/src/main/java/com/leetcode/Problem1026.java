package com.leetcode;

import com.common.TreeNode;

/**
 * 1026. Maximum Difference Between Node and Ancestor
 * https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/
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
        ans = getMax(ans, Math.abs(node.val - curMax), Math.abs(node.val - curMin));
        curMax = Math.max(curMax, node.val);
        curMin = Math.min(curMin, node.val);
        helper(node.left, curMax, curMin);
        helper(node.right, curMax, curMin);
    }

    private int getMax(int a, int b, int c) {
        return Math.max(a, Math.max(b, c));
    }
}
