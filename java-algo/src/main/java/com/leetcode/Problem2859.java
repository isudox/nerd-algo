package com.leetcode;

import java.util.List;

/**
 * https://leetcode.cn/problems/sum-of-values-at-indices-with-k-set-bits
 */
public class Problem2859 {
    public int sumIndicesWithKSetBits(List<Integer> nums, int k) {
        int ans = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (Integer.bitCount(i) == k) {
                ans += nums.get(i);
            }
        }
        return ans;
    }
}
