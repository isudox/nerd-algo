package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

public class Problem117 {
    public Node connect(Node root) {
        if (root == null) {
            return null;
        }
        Deque<Node> deque = new ArrayDeque<>();
        deque.offer(root);
        while (deque.size() > 0) {
            int n = deque.size();
            Node pre = null;
            for (int i = 0; i < n; i++) {
                Node node = deque.pollFirst();
                if (pre != null) {
                    pre.next = node;
                }
                pre = node;
                if (node.left != null) {
                    deque.offer(node.left);
                }
                if (node.right != null) {
                    deque.offer(node.right);
                }
            }
        }
        return root;
    }

    private static class Node {
        public int val;
        public Node left;
        public Node right;
        public Node next;
    }
}
