package com.leetcode;

import com.common.TreeNode;

import java.util.HashMap;
import java.util.Map;

/**
 * 543. Diameter of Binary Tree
 * https://leetcode.com/problems/diameter-of-binary-tree/
 */
public class Problem543 {
    private Map<TreeNode, int[]> memo = new HashMap<>();
    private int ans = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null) {
            return 0;
        }
        getDepth(root);
        return this.ans;
    }

    private int[] getDepth(TreeNode node) {
        if (memo.containsKey(node)) {
            return memo.get(node);
        }
        int x = 0, y = 0;
        if (node.left != null) {
            int[] left = getDepth(node.left);
            x = Math.max(left[0], left[1]) + 1;
        }
        if (node.right != null) {
            int[] right = getDepth(node.right);
            y = Math.max(right[0], right[1]) + 1;
        }
        ans = Math.max(ans, x + y);
        memo.put(node, new int[]{x, y});
        return memo.get(node);
    }
}
