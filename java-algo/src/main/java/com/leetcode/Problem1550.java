package com.leetcode;

/**
 * 1550. Three Consecutive Odds
 * https://leetcode.com/problems/three-consecutive-odds/
 */
public class Problem1550 {
    public boolean threeConsecutiveOdds(int[] arr) {
        int i = 0, j = 0;
        while (i < arr.length) {
            if (arr[i] % 2 == 0) {
                i++;
                continue;
            }
            j = i;
            while (j < arr.length && arr[j] % 2 == 1) {
                j++;
                if (j - i == 3) {
                    return true;
                }
            }
            i = j;
        }
        return false;
    }
}
