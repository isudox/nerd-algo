package com.leetcode;

/**
 * 707. Design Linked List
 * https://leetcode.com/problems/design-linked-list/
 */
class Problem707 {
    static class MyLinkedList {
        ListNode head;
        int size;

        public MyLinkedList() {
        }
        
        public int get(int index) {
            if (index >= size) {
                return -1;
            }
            ListNode ptr = head;
            for (int i = 0; i < index; i++) {
                ptr = ptr.next;
            }
            return ptr.val;
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
            ListNode ptr = new ListNode(-1, head);
            for (int i = 0; i < index; i++) {
                ptr = ptr.next;
            }
            ListNode next = ptr.next;
            ptr.next = new ListNode(val, next);
            size++;
        }
        
        public void deleteAtIndex(int index) {
            if (index >= size) {
                return;
            }
            ListNode ptr = new ListNode(-1, head);
            for (int i = 0; i < index; i++) {
                ptr = ptr.next;
            }
            ListNode next = ptr.next;
            ptr.next = next.next;
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
