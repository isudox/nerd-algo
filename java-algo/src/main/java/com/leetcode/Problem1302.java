package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 1302. Deepest Leaves Sum
 * https://leetcode.com/problems/deepest-leaves-sum/
 */
public class Problem1302 {
    public int deepestLeavesSum(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.addLast(root);
        int ans = 0;
        while (!queue.isEmpty()) {
            ans = 0;
            int n = queue.size();
            for (int i = 0; i < n; i++) {
                TreeNode node = queue.pollFirst();
                ans += node.val;
                if (node.left != null) {
                    queue.addLast(node.left);
                }
                if (node.right != null) {
                    queue.addLast(node.right);
                }
            }
        }
        return ans;
    }
}
