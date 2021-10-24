package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 222. Count Complete Tree Nodes
 * https://leetcode.com/problems/count-complete-tree-nodes/
 */
public class Problem222 {
    public int countNodes(TreeNode root) {
        if (null == root) return 0;
        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.add(root);
        int ans = 0;
        while (queue.size() > 0) {
            int n = queue.size();
            ans += n;
            for (int i = 0; i < n; i++) {
                TreeNode node = queue.pollFirst();
                if (node.left != null)
                    queue.add(node.left);
                if (node.right != null)
                    queue.add(node.right);
            }
        }
        return ans;
    }
}
