package com.leetcode;

/**
 * 829. Consecutive Numbers Sum
 * https://leetcode.com/problems/consecutive-numbers-sum/
 */
public class Problem829 {
    public int consecutiveNumbersSum(int n) {
        int ans = 0;
        int max = (int) Math.sqrt(n * 2);
        for (int i = 1; i <= max; i++) {
            if (2 * n % i != 0) {
                continue;
            }
            int tmp = 2 * n / i - i + 1;
            if (tmp % 2 == 0) {
                ans++;
            }
        }
        return ans;
    }
}
