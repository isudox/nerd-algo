package com.leetcode;

/**
 * 2437. Number of Valid Clock Times
 * https://leetcode.com/problems/number-of-valid-clock-times/
 */
public class Problem2437 {
    public int countTime(String time) {
        String[] t = time.split(":");
        return count(t[0], 24) * count(t[1], 60);
    }

    private int count(String time, int limit) {
        int cnt = 0;
        for (int i = 0; i < limit; i++) {
            int x = i / 10, y = i % 10;
            if ((time.charAt(0) == '?' || time.charAt(0) - '0' == x) && (time.charAt(1) == '?' || time.charAt(1) - '0' == y)) {
                cnt++;
            }
        }
        return cnt;
    }
}
