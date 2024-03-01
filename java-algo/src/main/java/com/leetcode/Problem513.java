package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 513. Find Bottom Left Tree Value
 * https://leetcode.com/problems/find-bottom-left-tree-value/
 */
public class Problem513 {
    public int findBottomLeftValue(TreeNode root) {
        Deque<TreeNode> q = new ArrayDeque<>();
        q.push(root);
        while (!q.isEmpty()) {
            TreeNode first = q.getFirst();
            boolean hasChild = false;
            int n = q.size();
            for (int i = 0; i < n; i++) {
                TreeNode node = q.pollFirst();
                if (node.left != null) {
                    hasChild = true;
                    q.offerLast(node.left);
                }
                if (node.right != null) {
                    hasChild = true;
                    q.offerLast(node.right);
                }
            }
            if (!hasChild) {
                return first.val;
            }
        }
        return 0;
    }
}
