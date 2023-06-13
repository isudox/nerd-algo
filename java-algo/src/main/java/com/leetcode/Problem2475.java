package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 2475. Number of Unequal Triplets in Array
 * https://leetcode.com/problems/number-of-unequal-triplets-in-array/
 */
public class Problem2475 {
    public int unequalTriplets(int[] nums) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        if (counter.size() < 3) {
            return 0;
        }
        int ans = 0, cnt = 0, n = nums.length;
        for (Map.Entry<Integer, Integer> entry : counter.entrySet()) {
            ans += cnt * entry.getValue() * (n - cnt - entry.getValue());
            cnt += entry.getValue();
        }
        return ans;
    }
}
