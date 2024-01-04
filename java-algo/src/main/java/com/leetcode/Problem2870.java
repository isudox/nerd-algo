package com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class Problem2870 {
    public int minOperations(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }
        int ans = 0;
        for (int cnt : counts.values()) {
            if (cnt == 1) {
                return -1;
            }
            ans +=  cnt / 3 + (cnt % 3 == 0 ? 0 : 1);
        }
        return ans;
    }
}
