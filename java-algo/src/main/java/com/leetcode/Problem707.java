package com.leetcode;

/**
 * 707. Design Linked List
 * https://leetcode.com/problems/design-linked-list/
 */
class Problem707 {
    class MyLinkedList {
        ListNode head;
        int size;

        public MyLinkedList() {
        }

        public int get(int index) {
            if (index >= size) {
                return -1;
            }
            ListNode cur = head;
            for (int i = 0; i < index; i++) {
                cur = cur.next;
            }
            return cur.val;
        }

        public void addAtHead(int val) {
            head = new ListNode(val, head);
            size++;
        }

        public void addAtTail(int val) {
            size++;
            if (head == null) {
                head = new ListNode(val, null);
                return;
            }
            ListNode ptr = head;
            while (ptr.next != null) {
                ptr = ptr.next;
            }
            ptr.next = new ListNode(val, null);
        }

        public void addAtIndex(int index, int val) {
            if (index > size) {
                return;
            }
            if (index == 0) {
                head = new ListNode(val, head);
                size++;
                return;
            }
            ListNode cur = head, pre = null;
            for (int i = 0; i < index; i++) {
                pre = cur;
                cur = cur.next;
            }
            if (pre == null) {

            }
            pre.next = new ListNode(val, cur);
            size++;
        }

        public void deleteAtIndex(int index) {
            if (index >= size) {
                return;
            }
            ListNode cur = head, pre = null;
            for (int i = 0; i < index; i++) {
                pre = cur;
                cur = cur.next;
            }
            if (pre == null) {
                head = cur.next;
            } else if (cur.next != null) {
                pre.next = cur.next;
            } else {
                pre.next = null;
            }
            size--;
        }

        private class ListNode {
            ListNode next;
            int val;

            public ListNode(int val, ListNode next) {
                this.val = val;
                this.next = next;
            }
        }
    }
}
