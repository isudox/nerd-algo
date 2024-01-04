package com.leetcode;

/**
 * https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/
 */
public class Problem1599 {
    public int minOperationsMaxProfit(int[] customers, int boardingCost, int runningCost) {
        int max = 0, cur = 0,  waits = 0;
        int cnt = 0, ans = 0, i = 0;
        while (i < customers.length || waits > 0) {
            if (i < customers.length) {
                waits += customers[i];
            }
            cur += Math.min(waits, 4) * boardingCost - runningCost;
            cnt++;
            i++;
            if (cur > max) {
                max = cur;
                ans = cnt;
            }
            waits = Math.max(waits - 4, 0);
        }
        return max  > 0 ? ans : -1;
    }
}
