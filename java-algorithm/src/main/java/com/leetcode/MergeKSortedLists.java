package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 23. Merge k Sorted Lists
 * https://leetcode.com/problems/merge-k-sorted-lists/
 * <p>
 * Merge k sorted linked lists and return it as one sorted list. Analyze and
 * describe its complexity.
 * <p>
 * Example:
 *
 * <pre>
 *     Input:
 *     [
 *       1->4->5,
 *       1->3->4,
 *       2->6
 *     ]
 *     Output: 1->1->2->3->4->4->5->6
 * </pre>
 */
public class MergeKSortedLists {

    /**
     * The nerd approach :(
     * Time complexity:
     */
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode res = new ListNode(0);
        ListNode cur = res;
        List<Integer> nums = new ArrayList<>();

        for (ListNode l : lists) {
            while (null != l) {
                nums.add(l.val);
                l = l.next;
            }
        }

        while (nums.size() > 0) {
            cur.next = new ListNode(min(nums));
            cur = cur.next;
        }

        return res.next;
    }

    private int min(List<Integer> nums) {
        int min = nums.get(0);

        for (Integer num : nums) {
            if (num < min) {
                min = num;
            }
        }

        nums.remove(nums.indexOf(min));

        return min;
    }
}
