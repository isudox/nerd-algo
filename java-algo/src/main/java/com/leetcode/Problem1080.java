package com.leetcode;

import com.common.TreeNode;

/**
 * 1080. Insufficient Nodes in Root to Leaf Paths
 * https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/
 */
public class Problem1080 {
    private int limit;

    public TreeNode sufficientSubset(TreeNode root, int limit) {
        this.limit = limit;
        boolean ret = dfs(root, 0);
        return ret ? root : null;
    }

    private boolean dfs(TreeNode node, int pre) {
        if (node == null) {
            return false;
        }
        int cur = pre + node.val;
        if (node.left == null && node.right == null) {
            return cur >= limit;
        }
        boolean l = dfs(node.left, cur), r = dfs(node.right, cur);
        if (!l) {
            node.left = null;
        }
        if (!r) {
            node.right = null;
        }
        return l || r;
    }
}
