package com.leetcode;

import com.common.ListNode;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

/**
 * 1019. Next Greater Node In Linked List
 * https://leetcode.com/problems/next-greater-node-in-linked-list/
 */
public class Problem1019 {
    public int[] nextLargerNodes(ListNode head) {
        List<Integer> ans = new ArrayList<>();
        Deque<int[]> q = new ArrayDeque<>();
        ListNode cur = head;
        int pos = -1;
        while (cur != null) {
            pos++;
            ans.add(0);
            while (!q.isEmpty() && q.peek()[0] < cur.val) {
                ans.set(q.pop()[1], cur.val);
            }
            q.push(new int[]{cur.val, pos});
            cur = cur.next;
        }
        int size = ans.size();
        int[] arr = new int[size];
        for (int i = 0; i < size; i++) {
            arr[i] = ans.get(i);
        }
        return arr;
    }
}
