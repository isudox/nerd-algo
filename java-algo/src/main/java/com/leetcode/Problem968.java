package com.leetcode;

import com.common.TreeNode;

/**
 * 968. Binary Tree Cameras
 * https://leetcode.com/problems/binary-tree-cameras/
 */
public class Problem968 {
    private int cnt;

    public int minCameraCover(TreeNode root) {
        if (dfs(root) < 1) {
            cnt++;
        }
        return cnt;
    }

    private int dfs(TreeNode node) {
        if (node == null) {
            return 2;  //
        }
        int left = dfs(node.left);
        int right = dfs(node.right);
        if (left == 0 || right == 0) {
            cnt++;
            return 1;
        }
        return left == 1 || right == 1 ? 2 : 0;
    }
}
