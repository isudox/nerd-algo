package com.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 133. Clone Graph
 * https://leetcode.com/problems/clone-graph/
 */

public class Problem133 {
    public Node cloneGraph(Node node) {
        Map<Integer, Node> store = new HashMap<>();
        return helper(node, store);
    }

    private Node helper(Node node, Map<Integer, Node> store) {
        if (node == null) {
            return null;
        }
        if (store.containsKey(node.val)) {
            return store.get(node.val);
        }
        Node newNode = new Node(node.val);
        store.put(node.val, newNode);
        for (Node neighbor : node.neighbors) {
            newNode.neighbors.add(helper(neighbor, store));
        }
        return newNode;
    }

    private static class Node {
        public int val;
        public List<Node> neighbors;

        public Node() {
            val = 0;
            neighbors = new ArrayList<>();
        }

        public Node(int _val) {
            val = _val;
            neighbors = new ArrayList<>();
        }

        public Node(int _val, ArrayList<Node> _neighbors) {
            val = _val;
            neighbors = _neighbors;
        }
    }
}



