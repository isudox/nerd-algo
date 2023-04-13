package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

/**
 * 102.
 */
class Problem102 {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if (root == null) return ans;
        Deque<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        while (!q.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int n = q.size();
            for (int i = 0; i < n; i++) {
                TreeNode node = q.pollFirst();
                level.add(node.val);
                if (node.left != null) q.offerLast(node.left);
                if (node.right != null) q.offerLast(node.right);
            }
            ans.add(level);
        }
        return ans;
    }
}
