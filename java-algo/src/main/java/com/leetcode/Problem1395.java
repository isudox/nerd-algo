package com.leetcode;

/**
 * 1395. Count Number of Teams
 * https://leetcode.com/problems/count-number-of-teams/
 */
public class Problem1395 {
    public int numTeams(int[] rating) {
        int ans = 0, n = rating.length;
        for (int j = 1; j < n - 1; j++) {
            int iless = 0, imore = 0;
            int kless = 0, kmore = 0;
            for (int i = 0; i < j; i++) {
                if (rating[i] < rating[j]) {
                    iless++;
                } else if (rating[i] > rating[j]) {
                    imore++;
                }
            }
            for (int k = j + 1; k < n; k++) {
                if (rating[k] > rating[j]) {
                    kmore++;
                } else if (rating[k] < rating[j]) {
                    kless++;
                }
            }
            ans += iless * kmore + imore * kless;
        }
        return ans;
    }
}
