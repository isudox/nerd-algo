package com.leetcode;

import com.common.TreeNode;

/**
 * 979. Distribute Coins in Binary Tree
 * https://leetcode.com/problems/distribute-coins-in-binary-tree/
 */
public class Problem979 {
    private int ans = 0;

    public int distributeCoins(TreeNode root) {
        dfs(root);
        return ans;
    }

    private int dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int leftCoins = dfs(node.left), rightCoins = dfs(node.right);
        ans += Math.abs(leftCoins) + Math.abs(rightCoins);
        return node.val - 1 + leftCoins + rightCoins;
    }
}
