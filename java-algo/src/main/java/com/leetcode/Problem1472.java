package com.leetcode;

/**
 * 1472. Design Browser History
 * https://leetcode.com/problems/design-browser-history/
 */
public class Problem1472 {
    static class BrowserHistory {
        private Node cur;

        public BrowserHistory(String homepage) {
            cur = new Node(homepage);
        }

        public void visit(String url) {
            Node next = new Node(url);
            next.prev = cur;
            cur.next = next;
            cur = next;
        }

        public String back(int steps) {
            while (steps > 0 && cur.prev != null) {
                cur = cur.prev;
                steps--;
            }
            return cur.val;
        }

        public String forward(int steps) {
            while (steps > 0 && cur.next != null) {
                cur = cur.next;
                steps--;
            }
            return cur.val;
        }
    }

    static class Node {
        Node prev;
        Node next;
        String val;

        public Node(String val) {
            this.val = val;
        }
    }
}
