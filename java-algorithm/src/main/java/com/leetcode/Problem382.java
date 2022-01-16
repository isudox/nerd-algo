package com.leetcode;

import com.common.ListNode;

import java.util.Random;

/**
 * 382. Linked List Random Node
 * https://leetcode.com/problems/linked-list-random-node/
 */
public class Problem382 {

    private final ListNode head;
    private final Random random;

    public Problem382(ListNode head) {
        this.head = head;
        this.random = new Random();
    }

    public int getRandom() {
        int scope = 1;
        int chosen = 0;
        ListNode cur = this.head;
        while (cur != null) {
            if (this.random.nextInt(scope) == 0) {
                chosen = cur.val;
            }
            cur = cur.next;
            scope++;
        }
        return chosen;
    }
}
