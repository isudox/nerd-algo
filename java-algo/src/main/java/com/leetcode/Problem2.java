package com.leetcode;

import com.common.ListNode;

import java.math.BigInteger;

/**
 * 2. Add Two Numbers
 * https://leetcode.com/problems/add-two-numbers/
 */
public class Problem2 {

    /**
     * The nerd approach with the big help of {@link BigInteger}.
     */
    public ListNode addTwoNumbers1(ListNode l1, ListNode l2) {
        BigInteger sum = listNode2Num(l1).add(listNode2Num(l2));
        if (BigInteger.ZERO.compareTo(sum) == 0) {
            return new ListNode(0);
        }

        return num2ListNode(sum);
    }

    private BigInteger listNode2Num(ListNode listNode) {
        if (listNode == null) {
            return BigInteger.valueOf(0);
        }

        return BigInteger.valueOf(listNode.val).add(listNode2Num(listNode.next)
                .multiply(BigInteger.valueOf(10)));
    }

    private ListNode num2ListNode(BigInteger num) {
        ListNode listNode = new ListNode(0);
        if (BigInteger.ZERO.compareTo(num) == 0) {
            return null;
        }

        listNode.val = num.mod(BigInteger.valueOf(10)).intValue();
        listNode.next = num2ListNode(num.divide(BigInteger.valueOf(10)));

        return listNode;
    }

    /**
     * A better recursive approach.
     */
    public ListNode addTwoNumbers2(ListNode l1, ListNode l2) {
        return addTwoNumbers2(l1, l2, 0);
    }

    private ListNode addTwoNumbers2(ListNode l1, ListNode l2, int carry) {
        ListNode node = new ListNode(0);

        if (l1 == null && l2 == null) {
            if (carry > 0) {
                node.val = carry;
            } else {
                return null;
            }
        }

        if (l1 != null && l2 == null) {
            node.val = (l1.val + carry) % 10;
            node.next = addTwoNumbers2(l1.next, null, (l1.val + carry) / 10);
        }

        if (l1 == null && l2 != null) {
            node.val = (l2.val + carry) % 10;
            node.next = addTwoNumbers2(null, l2.next, (l2.val + carry) / 10);
        }

        if (l1 != null && l2 != null) {
            node.val = (l1.val + l2.val + carry) % 10;
            node.next = addTwoNumbers2(l1.next, l2.next, (l1.val + l2.val + carry) / 10);
        }

        return node;
    }

}
