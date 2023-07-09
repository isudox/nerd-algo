package com.leetcode;

/**
 * 2600. K Items With the Maximum Sum
 * https://leetcode.com/problems/k-items-with-the-maximum-sum/
 */
class Problem2600 {
    public int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        int ans = 0;
        int[] cnt = new int[]{numOnes, numZeros, numNegOnes};
        for (int i = 0; i < 3; i++) {
            if (k <= 0) {
                break;
            }
            int n = Math.min(cnt[i], k);
            ans += (1 - i) * n;
            k -= n;
        }
        return ans;
    }
}
