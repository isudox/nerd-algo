package com.leetcode;

import java.util.*;

/**
 * 731. My Calendar II
 * https://leetcode.com/problems/my-calendar-ii/
 */
public class Problem731 {
    private static class MyCalendarTwo {
        Map<Integer, int[]> tree;

        public MyCalendarTwo() {
            this.tree = new HashMap<>();
        }

        public boolean book(int start, int end) {
            update(start, end - 1, 1, 0, 1000000000, 1);
            tree.putIfAbsent(1, new int[2]);
            if (tree.get(1)[0] > 2) {
                update(start, end - 1, -1, 0, 1000000000, 1);
                return false;
            }
            return true;
        }

        private void update(int start, int end, int val, int l, int r, int idx) {
            if (r < start || l > end) return;
            tree.putIfAbsent(idx, new int[2]);
            if (start <= l && r <= end) {
                tree.get(idx)[0] += val;
                tree.get(idx)[1] += val;
            } else {
                int mid = l + (r - l) / 2;
                update(start, end, val, l, mid, 2 * idx);
                update(start, end, val, mid + 1, r, 2 * idx + 1);
                tree.putIfAbsent(2 * idx, new int[2]);
                tree.putIfAbsent(2 * idx + 1, new int[2]);
                tree.get(idx)[0] = tree.get(idx)[1] + Math.max(tree.get(2 * idx)[0], tree.get(2 * idx + 1)[0]);
            }
        }
    }
}
