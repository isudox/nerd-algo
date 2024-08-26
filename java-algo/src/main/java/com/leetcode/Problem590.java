package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 590. N-ary Tree Postorder Traversal
 * https://leetcode.com/problems/n-ary-tree-postorder-traversal/
 */
public class Problem590 {
    public List<Integer> postorder(Node root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null) {
            return ans;
        }
        for (Node child : root.children) {
            List<Integer> list = postorder(child);
            ans.addAll(list);
        }
        ans.add(root.val);
        return ans;
    }

    static class Node {
        public int val;
        public List<Node> children;

        public Node() {
        }

        public Node(int _val) {
            val = _val;
        }

        public Node(int _val, List<Node> _children) {
            val = _val;
            children = _children;
        }
    }

    ;
}
