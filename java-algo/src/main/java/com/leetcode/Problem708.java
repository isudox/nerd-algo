package com.leetcode;

/**
 * 708. Insert into a Sorted Circular Linked List
 * https://leetcode.cn/problems/insert-into-a-sorted-circular-linked-list/
 */
public class Problem708 {
    public Node insert(Node head, int insertVal) {
        if (head == null) { // []
            Node ret = new Node(insertVal);
            ret.next = ret;
            return ret;
        }
        if (head.next == head) { // [1]
            head.next = new Node(insertVal, head);
            return head;
        }
        if (head.next.next == head) {
            if ((head.val <= insertVal && insertVal <= head.next.val)) { // [1,3], 2
                head.next = new Node(insertVal, head.next);
                return head;
            }
            if (head.next.val <= insertVal && insertVal <= head.val) { // [3,1], 2
                head.next.next = new Node(insertVal, head);
                return head;
            }
        }
        Node node = head.next;
        Node maxNode = head;
        int size = 1;
        while (node != head) {
            size++;
            if (node.val >= maxNode.val) {
                maxNode = node;
            }
            node = node.next;
        }
        for (int i = 0; i < size; i++) {
            if (node.val <= insertVal && insertVal <= node.next.val) {
                node.next = new Node(insertVal, node.next);
                return head;
            }
            node = node.next;
        }
        maxNode.next = new Node(insertVal, maxNode.next);
        return head;
    }

    private static class Node {
        public int val;
        public Node next;

        public Node() {
        }

        public Node(int _val) {
            val = _val;
        }

        public Node(int _val, Node _next) {
            val = _val;
            next = _next;
        }
    }
}
