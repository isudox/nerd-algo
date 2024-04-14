package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 404. Sum of Left Leaves
 * https://leetcode.com/problems/sum-of-left-leaves/
 */
public class Problem404 {
    public int sumOfLeftLeaves(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int ans = 0;
        Deque<TreeNode> q = new ArrayDeque<>();
        q.addLast(root);
        while (!q.isEmpty()) {
            int n = q.size();
            for (int i = 0; i < n; i++) {
                TreeNode node = q.removeFirst();
                if (node.left != null) {
                    if (node.left.left == null && node.left.right == null) {
                        ans += node.left.val;
                    } else {
                        q.addLast(node.left);
                    }
                }
                if (node.right != null) {
                    q.addLast(node.right);
                }
            }
        }
        return ans;
    }
}
