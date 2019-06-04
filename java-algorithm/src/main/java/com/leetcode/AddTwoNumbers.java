package com.leetcode;

import java.math.BigInteger;

/**
 * 2. Add Two Numbers
 * https://leetcode.com/problems/add-two-numbers/
 * <p>
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order and each of their nodes
 * contain a single digit. Add the two numbers and return it as a linked list.
 * <p>
 * You may assume the two numbers do not contain any leading zero, except the
 * number 0 itself.
 * <p>
 * Example:
 * <pre>
 *     Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 *     Output: 7 -> 0 -> 8
 *     Explanation: 342 + 465 = 807.
 * </pre>
 */
public class AddTwoNumbers {

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
