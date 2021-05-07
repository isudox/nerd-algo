package com.leetcode;

import java.util.Arrays;
import java.util.Comparator;

/**
 * 253. Meeting Rooms II
 * https://leetcode.com/problems/meeting-rooms-ii/
 *
 * Given an array of meeting time intervals intervals where
 * intervals[i] = [start_i, end_i], return the minimum number
 * of conference rooms required.
 *
 * Example 1:
 *
 * Input: intervals = [[0,30],[5,10],[15,20]]
 * Output: 2
 *
 * Example 2:
 *
 * Input: intervals = [[7,10],[2,4]]
 * Output: 1
 *
 * Constraints:
 *
 * 1 <= intervals.length <= 10^4
 * 0 <= starti < endi <= 10^6
 */
public class Problem253 {
    public int minMeetingRooms(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        int cnt = 0;
        int[] visited = new int[intervals.length];
        for (int i = 0; i < intervals.length; i++) {
            if (visited[i] == 0) {
                int end = intervals[i][1];
                for (int j = i + 1; j < intervals.length; j++) {
                    if (visited[j] == 0 && end <= intervals[j][0]) {
                        cnt++;
                        end = intervals[j][1];
                        visited[j] = 1;
                    }
                }
            }
        }
        return intervals.length - cnt;
    }
}
