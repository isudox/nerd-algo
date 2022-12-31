package com.leetcode;

import java.util.Arrays;

/**
 * 2037. Minimum Number of Moves to Seat Everyone
 * https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
 */
public class Problem2037 {
    public int minMovesToSeat(int[] seats, int[] students) {
        Arrays.sort(seats);
        Arrays.sort(students);
        int ans = 0;
        for (int i = 0; i < students.length; i++) {
            ans += Math.abs(students[i] - seats[i]);
        }
        return ans;
    }
}
