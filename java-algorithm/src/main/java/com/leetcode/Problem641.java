package com.leetcode;

/**
 * 641. Design Circular Deque
 * https://leetcode.com/problems/design-circular-deque/
 */
public class Problem641 {

    static class MyCircularDeque {

        private int capacity;
        private int size;
        private Node head;
        private Node tail;

        public MyCircularDeque(int k) {
            this.capacity = k;
            head = new Node();
            tail = new Node();
            head.next = tail;
            tail.prev = head;
        }

        public boolean insertFront(int value) {
            if (isFull()) return false;
            Node start = head.next;
            Node cur = new Node(value);
            head.next = cur;
            cur.prev = head;
            cur.next = start;
            start.prev = cur;
            size++;
            return true;
        }

        public boolean insertLast(int value) {
            if (isFull()) return false;
            Node end = tail.prev;
            Node cur = new Node(value);
            cur.next = tail;
            tail.prev = cur;
            cur.prev = end;
            end.next = cur;
            size++;
            return true;
        }

        public boolean deleteFront() {
            if (isEmpty()) return false;
            Node deleted = head.next;
            head.next = deleted.next;
            deleted.next.prev = head;
            size--;
            return true;
        }

        public boolean deleteLast() {
            if (isEmpty()) return false;
            Node deleted = tail.prev;
            tail.prev = deleted.prev;
            deleted.prev.next = tail;
            size--;
            return true;
        }

        public int getFront() {
            if (isEmpty()) return -1;
            return head.next.val;
        }

        public int getRear() {
            if (isEmpty()) return -1;
            return tail.prev.val;
        }

        public boolean isEmpty() {
            return size == 0;
        }

        public boolean isFull() {
            return capacity == size;
        }
    }

    private static class Node {
        int val;
        Node prev;
        Node next;


        public Node() {
        }

        public Node(int val) {
            this.val = val;
        }
    }
}
