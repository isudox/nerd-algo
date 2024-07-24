package com.leetcode;

import com.common.TreeNode;

/**
 * 1530. Number of Good Leaf Nodes Pairs
 * https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
 */
public class Problem1530 {
    public int countPairs(TreeNode root, int distance) {
        return postOrder(root, distance)[11];
    }

    private int[] postOrder(TreeNode node, int distance) {
        if (node == null) {
            return new int[12];
        }
        if (node.left == null && node.right == null) {
            int[] current = new int[12];
            current[0] = 1;
            return current;
        }
        int[] left = postOrder(node.left, distance);
        int[] right = postOrder(node.right, distance);

        int[] current = new int[12];
        for (int i = 0; i < 10; i++) {
            current[i + 1] += left[i] + right[i];
        }
        current[11] += left[11] + right[11];
        for (int d1 = 0; d1 <= distance; d1++) {
            for (int d2 = 0; d2 <= distance; d2++) {
                if (2 + d1 + d2 <= distance) {
                    current[11] += left[d1] * right[d2];
                }
            }
        }
        return current;
    }
}
