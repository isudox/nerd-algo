package com.leetcode;

import java.util.*;

/**
 * 1481. Least Number of Unique Integers after K Removals
 * https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals
 */
public class Problem1481 {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : arr) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        Map<Integer, List<Integer>> freq2nums = new TreeMap<>();
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            List<Integer> nums = freq2nums.getOrDefault(entry.getValue(), new ArrayList<>());
            nums.add(entry.getKey());
            freq2nums.put(entry.getValue(), nums);
        }
        int deleted = 0;
        for (Map.Entry<Integer, List<Integer>> entry : freq2nums.entrySet()) {
            int freq = entry.getKey(), nums = entry.getValue().size();
            if (k <= freq * nums) {
                deleted += k / freq;
                break;
            }
            k -= freq * nums;
            deleted += nums;
        }
        return count.size() - deleted;
    }
}
