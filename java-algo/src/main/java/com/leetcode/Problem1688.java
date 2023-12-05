package com.leetcode;

/**
 * 1688. Count of Matches in Tournament
 * https://leetcode.com/problems/count-of-matches-in-tournament/
 */
public class Problem1688 {
    public int numberOfMatches(int n) {
        int ans = 0;
        while (n > 1) {
            boolean flag = n % 2 == 0;
            if (flag) {
                ans += n / 2;
                n /= 2;
            } else {
                ans += (n - 1) / 2;
                n = n / 2 + 1;
            }
        }
        return ans;
    }
}
