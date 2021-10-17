package com.leetcode;

import com.common.TreeNode;

/**
 * 437. Path Sum III
 * https://leetcode.com/problems/path-sum-iii/
 */
public class Problem437 {
    public int pathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return 0;
        }
        return dfs(root, targetSum) + pathSum(root.left, targetSum) + pathSum(root.right, targetSum);
    }

    private int dfs(TreeNode node, int target) {
        if (node == null) {
            return 0;
        }
        int ret = 0;
        if (node.val == target) {
            ret++;
        }
        return ret + dfs(node.left, target - node.val) + dfs(node.right, target - node.val);
    }
}
