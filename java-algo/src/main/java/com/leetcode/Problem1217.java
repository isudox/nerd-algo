package com.leetcode;

/**
 * 1217. Minimum Cost to Move Chips to The Same Position
 * https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
 */
public class Problem1217 {
    public int minCostToMoveChips(int[] position) {
        int even = 0, odd = 0;
        for (int p : position) {
            if (p % 2 == 0) {
                even++;
            } else {
                odd++;
            }
        }
        return Math.min(even, odd);
    }
}
