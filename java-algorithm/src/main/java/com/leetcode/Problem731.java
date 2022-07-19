package com.leetcode;

import java.util.*;

public class Problem731 {
    private static class MyCalendarTwo {
        private final List<int[]> calendars;

        public MyCalendarTwo() {
            this.calendars = new ArrayList<>();
        }

        public boolean book(int start, int end) {
            Set<int[]> overlaps = new HashSet<>();
            int[] cur = new int[]{start, end};
            int cnt = 0;
            for (int[] cal : calendars) {
                int[] overlap = getOverlap(cal, cur);
                if (overlap != null) {
                    for (int[] o : overlaps) {
                        if (getOverlap(o, overlap) != null) {
                            return false;
                        }
                    }
                    overlaps.add(overlap);
                }
            }
            calendars.add(cur);
            return true;
        }

        private int[] getOverlap(int[] a, int[] b) {
            if (a[0] < b[1] && b[0] < a[1]) {
                return new int[]{Math.max(a[0], b[0]), Math.min(a[1], b[1])};
            }
            return null;
        }
    }
}
