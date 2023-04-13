package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

/**
 * 199. Binary Tree Right Side View
 * https://leetcode.com/problems/binary-tree-right-side-view/
 */
class Problem199 {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null) return ans;
        Deque<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        while (!q.isEmpty()) {
            ans.add(q.peekLast().val);
            int n = q.size();
            for (int i = 0; i < n; i++) {
                TreeNode node = q.pollFirst();
                if (node.left != null) q.offerLast(node.left);
                if (node.right != null) q.offerLast(node.right);
            }
        }
        return ans;
    }
}
