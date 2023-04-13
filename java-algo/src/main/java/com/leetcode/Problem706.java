package com.leetcode;

/**
 * 706. Design HashMap
 * https://leetcode.com/problems/design-hashmap/
 */
public class Problem706 {
    private static class MyHashMap {

        private final Node[] nodes = new Node[751];

        public MyHashMap() {
        }

        public void put(int key, int value) {
            int hash = key % 751;
            if (nodes[hash] == null) {
                nodes[hash] = new Node(key, value);
            } else {
                Node pre = null;
                Node node = nodes[hash];
                while (node != null) {
                    if (node.key == key) {
                        node.val = value;
                        return;
                    }
                    pre = node;
                    node = node.next;
                }
                pre.next = new Node(key, value);
            }
        }

        public int get(int key) {
            int hash = key % 751;
            Node node = nodes[hash];
            while (node != null) {
                if (node.key == key) {
                    return node.val;
                }
                node = node.next;
            }
            return -1;
        }

        public void remove(int key) {
            int hash = key % 751;
            Node node = nodes[hash];
            if (node == null) {
                return;
            }
            if (node.key == key) {
                nodes[hash] = node.next;
                return;
            }
            Node pre = null;
            while (node != null && node.key != key) {
                pre = node;
                node = node.next;
            }
            if (node != null) {
                pre.next = node.next;
            }
        }

        static class Node {
            int key;
            int val;
            Node next;

            public Node(int key, int val) {
                this.key = key;
                this.val = val;
            }
        }
    }
}
