package com.leetcode;

/**
 * 2455. Average Value of Even Numbers That Are Divisible by Three
 * https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/
 */
public class Problem2455 {
    public int averageValue(int[] nums) {
        int sum = 0, cnt = 0;
        for (int num : nums) {
            if (num % 6 == 0) {
                sum += num;
                cnt++;
            }
        }
        return cnt > 0 ? sum / cnt : 0;
    }
}
