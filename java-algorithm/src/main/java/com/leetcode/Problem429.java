package com.leetcode;

import java.util.*;

/**
 * 429. N-ary Tree Level Order Traversal
 * https://leetcode.com/problems/n-ary-tree-level-order-traversal/
 */
public class Problem429 {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> ans = new ArrayList<>();
        if (root == null)
            return ans;
        Deque<Node> queue = new LinkedList<>();
        queue.add(root);
        while (queue.size() > 0) {
            int n = queue.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                Node cur = queue.removeFirst();
                level.add(cur.val);
                queue.addAll(cur.children);
            }
            ans.add(level);
        }
        return ans;
    }

    private static class Node {
        public int val;
        public List<Node> children;

        public Node() {}

        public Node(int _val) {
            val = _val;
        }

        public Node(int _val, List<Node> _children) {
            val = _val;
            children = _children;
        }
    }
}
