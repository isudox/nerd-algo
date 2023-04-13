package com.leetcode;

import java.util.*;

/**
 * 630. Course Schedule III
 * https://leetcode.com/problems/course-schedule-iii/
 */
public class Problem630 {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, Comparator.comparingInt(o -> o[1]));
        PriorityQueue<Integer> queue = new PriorityQueue<>((a, b) -> b - a);
        int days = 0;
        for (int[] course : courses) {
            days += course[0];
            queue.add(course[0]);
            if (days > course[1]) {
                days -= queue.poll();
            }
        }
        return queue.size();
    }
}
