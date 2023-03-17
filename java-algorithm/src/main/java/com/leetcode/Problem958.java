package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 958. Check Completeness of a Binary Tree
 * https://leetcode.com/problems/check-completeness-of-a-binary-tree/
 */
public class Problem958 {
    public boolean isCompleteTree(TreeNode root) {
        if (root == null) return true;
        Deque<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        boolean hasNull = false;
        while (!q.isEmpty()) {
            int n = q.size();
            for (int i = 0; i < n; i++) {
                TreeNode node = q.pollFirst();
                if (node.left != null) {
                    if (hasNull) {
                        return false;
                    }
                    q.offerLast(node.left);
                } else {
                    hasNull = true;
                }
                if (node.right != null) {
                    if (hasNull) {
                        return false;
                    }
                    q.offerLast(node.right);
                } else {
                    hasNull = true;
                }
            }
        }
        return true;
    }
}
