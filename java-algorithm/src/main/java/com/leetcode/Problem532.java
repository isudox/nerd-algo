package com.leetcode;

import java.util.*;

/**
 * 532. K-diff Pairs in an Array
 * https://leetcode.com/problems/k-diff-pairs-in-an-array/
 */
public class Problem532 {
    public int findPairs(int[] nums, int k) {
        int ans = 0;
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            if (helper(counter, num, num - k)) {
                ans++;
            }
            if (k != 0 && helper(counter, num, num + k)) {
                ans++;
            }
            int cnt = counter.getOrDefault(num, 0) + 1;
            counter.put(num, cnt);
        }
        return ans;
    }

    private boolean helper(Map<Integer, Integer> counter, int num, int need) {
        if (need == num && counter.getOrDefault(need, 0) == 1) {
            return true;
        }
        if (counter.containsKey(need) && !counter.containsKey(num)) {
            return true;
        }
        return false;
    }
}
