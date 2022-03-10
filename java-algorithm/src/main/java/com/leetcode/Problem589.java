package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 589. N-ary Tree Preorder Traversal
 * https://leetcode.com/problems/n-ary-tree-preorder-traversal/
 */
public class Problem589 {
    public List<Integer> preorder(Node root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null) return ans;
        ans.add(root.val);
        for (Node child : root.children) {
            ans.addAll(preorder(child));
        }
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
