/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2017-2019 sudoz
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 *
 */

import common.ListNode;

/**
 * https://leetcode.com/problems/reverse-nodes-in-k-group/
 * <p>
 * Given a linked list, reverse the nodes of a linked list k at a time and
 * return its modified list.
 * <p>
 * k is a positive integer and is less than or equal to the length of the
 * linked list. If the number of nodes is not a multiple of k
 * then left-out nodes in the end should remain as it is.
 * <p>
 * Example:
 * <pre>
 *    Given this linked list: 1->2->3->4->5
 *
 *    For k = 2, you should return: 2->1->4->3->5
 *
 *    For k = 3, you should return: 3->2->1->4->5
 * </pre>
 * <p>
 * Note:
 * <p>
 * Only constant extra memory is allowed.
 * You may not alter the values in the list's nodes,
 * only nodes itself may be changed.
 */
public class ReverseNodesInKGroup {

    /**
     * A nerd approach.
     */
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || head.next == null || k < 2) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode pre = dummy;
        ListNode cur = head;
        int counter = 0;

        while (cur != null) {
            counter++;

            if (counter % k == 0) {
                pre = reverse(pre, cur.next);
                cur = pre.next;
            } else {
                cur = cur.next;
            }
        }

        return dummy.next;
    }

    private ListNode reverse(ListNode pre, ListNode end) {
        ListNode head = pre.next;
        ListNode curr = head.next;

        while (curr != end) {
            ListNode temp = curr.next;
            curr.next = pre.next;
            pre.next = curr;
            curr = temp;
        }

        head.next = end;
        return head;
    }
}
