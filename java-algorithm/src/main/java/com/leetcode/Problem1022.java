package com.leetcode;

import com.common.TreeNode;

/**
 * 1022. Sum of Root To Leaf Binary Numbers
 * https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
 */
public class Problem1022 {
    private int sum = 0;

    public int sumRootToLeaf(TreeNode root) {
        if (root == null) {
            return 0;
        }
        dfs(root, 0);
        return sum;
    }

    private void dfs(TreeNode node, int cur) {
        if (node == null) {
            sum += cur;
            return;
        }
        cur = (cur << 1) + node.val;
        if (node.left == null && node.right == null) {
            sum += cur;
            return;
        }
        if (node.left != null) {
            dfs(node.left, cur);
        }
        if (node.right != null) {
            dfs(node.right, cur);
        }
    }
}
