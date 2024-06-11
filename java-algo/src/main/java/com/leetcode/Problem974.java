package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 974. Subarray Sums Divisible by K
 * https://leetcode.com/problems/subarray-sums-divisible-by-k/
 */
public class Problem974 {
    public int subarraysDivByK(int[] nums, int k) {
        Map<Integer, Integer> seen = new HashMap<>();
        seen.put(0, 1);
        int sum = 0, ans = 0;
        for (int num : nums) {
            sum = ((sum + num) % k + k) % k;
            ans += seen.getOrDefault(sum, 0);
            seen.put(sum, seen.getOrDefault(sum, 0) + 1);
        }
        return ans;
    }
}
