package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

/**
 * 103. Binary Tree Zigzag Level Order Traversal
 * https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
 */
public class Problem103 {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if (root == null)
            return ans;
        Deque<TreeNode> deque = new ArrayDeque<>();
        deque.offer(root);
        boolean flag = true;
        while (!deque.isEmpty()) {
            int n = deque.size();
            List<Integer> level = new ArrayList<>(n);
            for (int i = 0; i < n; i++) {
                TreeNode node = deque.pollFirst();
                if (flag)
                    level.add(node.val);
                else
                    level.add(0, node.val);
                if (node.left != null)
                    deque.offer(node.left);
                if (node.right != null)
                    deque.offer(node.right);
            }
            ans.add(level);
            flag = !flag;
        }
        return ans;
    }
}
