package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 992. Subarrays with K Different Integers
 * https://leetcode.com/problems/subarrays-with-k-different-integers/
 */
public class Problem992 {
    public int subarraysWithKDistinct(int[] nums, int k) {
        return slidingWindowAtMost(nums, k) - slidingWindowAtMost(nums, k - 1);
    }

    private int slidingWindowAtMost(int[] nums, int distinctK) {
        int cnt = 0;
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int i = 0, j = 0; j < nums.length; j++) {
            freqMap.put(nums[j], freqMap.getOrDefault(nums[j], 0) + 1);
            while (freqMap.size() > distinctK) {
                freqMap.put(nums[i], freqMap.get(nums[i]) - 1);
                if (freqMap.get(nums[i]) == 0) {
                    freqMap.remove(nums[i]);
                }
                i++;
            }
            cnt += (j - i + 1);
        }
        return cnt;
    }
}
