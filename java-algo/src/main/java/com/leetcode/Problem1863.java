package com.leetcode;

/**
 * 1863. Sum of All Subset XOR Totals
 * https://leetcode.com/problems/sum-of-all-subset-xor-totals/
 */
public class Problem1863 {
    public int subsetXORSum(int[] nums) {
        int n = nums.length;
        int ans = 0;
        for (int i = 0; i < 1 << n; i++) {
            int x = i;
            int cur = 0;
            for (int num : nums) {
                if ((x & 1) == 1) {
                    cur ^= num;
                }
                x >>= 1;
            }
            ans += cur;
        }
        return ans;
    }
}
