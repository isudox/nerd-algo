package com.leetcode;

import com.common.ListNode;

import java.util.ArrayList;
import java.util.List;

/**
 * 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
 * https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
 */
public class Problem2058 {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        int pre = head.val, cur;
        int i = 1;
        List<Integer> positions = new ArrayList<>();
        head = head.next;
        while (head.next != null) {
            cur = head.val;
            if ((pre < cur && head.next.val < cur) || (pre > cur && head.next.val > cur)) {
                positions.add(i);
            }
            pre = cur;
            head = head.next;
            i++;
        }
        if (positions.size() < 2) {
            return new int[]{-1, -1};
        }
        int min = positions.get(positions.size() - 1) - positions.get(0);
        int max = min;
        for (int j = 1; j < positions.size(); j++) {
            min = Math.min(min, positions.get(j) - positions.get(j - 1));
        }
        return new int[]{min, max};
    }
}
