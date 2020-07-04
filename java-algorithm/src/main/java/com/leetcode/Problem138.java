package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 138. Copy List with Random Pointer
 * https://leetcode.com/problems/copy-list-with-random-pointer/
 * <p>
 * A linked list is given such that each node contains an additional random
 * pointer which could point to any node in the list or null.
 * <p>
 * Return a deep copy of the list.
 * <p>
 * The Linked List is represented in the input/output as a list of n nodes.
 * Each node is represented as a pair of [val, random_index] where:
 * <p>
 * val: an integer representing Node.val
 * random_index: the index of the node (range from 0 to n-1) where
 * random pointer points to, or null if it does not point to any node.
 */
public class Problem138 {
    public Node copyRandomList(Node head) {
        if (null == head)
            return null;
        Map<Integer, Node> store = new HashMap<>();
        Map<Node, Integer> index = new HashMap<>();
        Node p = head;
        int i = 0;
        while (p != null) {
            store.put(i, new Node(p.val));
            index.put(p, i);
            p = p.next;
            i++;
        }
        p = head;
        for (int j = 0; j < i; j++) {
            if (j < i - 1) {
                store.get(j).next = store.get(j + 1);
            }
            if (p.random != null) {
                store.get(j).random = store.get(index.get(p.random));
            }
            p = p.next;
        }

        return store.get(0);
    }

    public Node copyRandomList2(Node head) {
        if (null == head)
            return null;
        Map<Node, Node> store = new HashMap<>();
        Node p = head;
        while (p != null) {
            store.put(p, new Node(p.val));
            p = p.next;
        }
        p = head;
        while (p != null) {
            if (p.next != null)
                store.get(p).next = store.get(p.next);
            if (p.random != null)
                store.get(p).random = store.get(p.random);
            p = p.next;
        }
        return store.get(head);
    }

    static class Node {
        int val;
        Node next;
        Node random;

        public Node(int val) {
            this.val = val;
            this.next = null;
            this.random = null;
        }
    }

}
