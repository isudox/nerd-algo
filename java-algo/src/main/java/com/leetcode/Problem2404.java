package com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class Problem2404 {
    public int mostFrequentEven(int[] nums) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            if (num % 2 == 0) {
                counter.put(num, counter.getOrDefault(num, 0) + 1);
            }
        }
        int ans = -1, cnt = 0;
        for (Map.Entry<Integer, Integer> e : counter.entrySet()) {
            if (e.getValue() > cnt || (e.getValue() == cnt && e.getKey() < ans)) {
                ans = e.getKey();
                cnt = e.getValue();
            }
        }
        return ans;
    }
}
