package com.leetcode;

/**
 * 2427. Number of Common Factors
 * https://leetcode.com/problems/number-of-common-factors/
 */
public class Problem2427 {
    public int commonFactors(int a, int b) {
        int ans = 0;
        int i = 1;
        while (i <= a && i <= b) {
            if (a % i == 0 && b % i == 0) {
                ans++;
            }
            i++;
        }
        return ans;
    }
}
