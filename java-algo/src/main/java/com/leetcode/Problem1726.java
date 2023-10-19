package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 1726. Tuple with Same Product
 * https://leetcode.com/problems/tuple-with-same-product
 */
public class Problem1726 {
    public int tupleSameProduct(int[] nums) {
        int n = nums.length;
        Map<Integer, Integer> counter = new HashMap<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int x = nums[i] * nums[j];
                counter.put(x, counter.getOrDefault(x, 0) + 1);
            }
        }
        int ans = 0;
        for (int v : counter.values()) {
            ans += 4 * v * (v - 1);
        }
        return ans;
    }
}
