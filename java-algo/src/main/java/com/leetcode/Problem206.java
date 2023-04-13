package com.leetcode;

import com.common.ListNode;

import java.util.ArrayList;
import java.util.List;

/**
 * 206. Reverse Linked List
 * https://leetcode.com/problems/reverse-linked-list/
 *
 * Reverse a singly linked list.
 *
 * Example:
 *
 * Input: 1->2->3->4->5->NULL
 * Output: 5->4->3->2->1->NULL
 *
 *
 * Follow up:
 *
 * A linked list can be reversed either iteratively or recursively.
 * Could you implement both?
 */
public class Problem206 {

    public ListNode reverseList(ListNode head) {
        if (null == head)
            return null;
        List<ListNode> list = new ArrayList<>();
        while (head != null) {
            list.add(new ListNode(head.val));
            head = head.next;
        }
        for (int i = list.size() - 1; i > 0; i--) {
            list.get(i).next = list.get(i - 1);
        }
        return list.get(list.size() - 1);
    }
}
