package com.leetcode;

import com.common.ListNode;

/**
 * 725. Split Linked List in Parts
 * https://leetcode.com/problems/split-linked-list-in-parts/
 */
public class Problem725 {
    public ListNode[] splitListToParts(ListNode head, int k) {
        int n = 0;
        ListNode ptr = head;
        while (ptr != null) {
            ptr = ptr.next;
            n++;
        }
        int avg = n / k;
        int rem = n % k;
        int bigSize = avg + (rem > 0 ? 1 : 0);
        ListNode[] ans = new ListNode[k];
        ptr = head;
        for (int i = 0; i < k; i++) {
            ans[i] = ptr;
            int size = i < rem ? bigSize : avg;
            for (int j = 1; j < size; j++) {
                ptr = ptr.next;
            }
            if (ptr == null) {
                break;
            }
            ListNode next = ptr.next;
            ptr.next = null;
            ptr = next;
        }
        return ans;
    }
}
