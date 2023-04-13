package com.leetcode;

/**
 * 849. Maximize Distance to Closest Person
 * https://leetcode.com/problems/maximize-distance-to-closest-person/
 */
public class Problem849 {
    public int maxDistToClosest(int[] seats) {
        int maxInterval = 1;
        int prePos = -1;
        int ans = 1;
        for (int i = 0; i < seats.length; i++) {
            if (seats[i] == 1) {
                if (prePos == -1) {
                    // find first `1`
                    ans = i;
                }
                int curInterval = i - prePos;
                if (curInterval > maxInterval) {
                    maxInterval = curInterval;
                }
                prePos = i;
            }
        }
        ans = Math.max(ans, seats.length - 1 - prePos);
        return Math.max(ans, maxInterval / 2);
    }
}
