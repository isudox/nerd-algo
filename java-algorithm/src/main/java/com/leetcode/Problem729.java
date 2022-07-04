package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 729. My Calendar I
 * https://leetcode.cn/problems/my-calendar-i/
 */
public class Problem729 {
    private static class MyCalendar {
        private List<int[]> calendars;

        public MyCalendar() {
            calendars = new ArrayList<>();
        }

        public boolean book(int start, int end) {
            for (int[] calendar : calendars) {
                if (calendar[0] < end && calendar[1] > start) {
                    return false;
                }
            }
            calendars.add(new int[]{start, end});
            return true;
        }
    }
}
