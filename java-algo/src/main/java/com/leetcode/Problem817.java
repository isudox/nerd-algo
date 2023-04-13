package com.leetcode;

import com.common.ListNode;

import java.util.HashSet;
import java.util.Set;

/**
 * 817. Linked List Components
 * https://leetcode.com/problems/linked-list-components/
 */
class Problem817 {
    public int numComponents(ListNode head, int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        int ans = 0;
        int cnt = 0;
        while (head != null) {
            if (set.contains(head.val)) {
                cnt++;
            } else {
                if (cnt > 0) {
                    ans++;
                }
                cnt = 0;
            }
            head = head.next;
        }
        return cnt == 0 ? ans : ans + 1;
    }
}
