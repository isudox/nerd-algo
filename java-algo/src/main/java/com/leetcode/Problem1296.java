package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 1296. Divide Array in Sets of K Consecutive Numbers
 * https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
 */
public class Problem1296 {
    public boolean isPossibleDivide(int[] nums, int k) {
        int n = nums.length;
        if (n % k > 0) {
            return false;
        }
        if (k == 1) {
            return true;
        }
        Map<Integer, Integer> cnts = new HashMap<>();
        int lo = nums[0], hi = nums[0];
        for (int num : nums) {
            lo = Math.min(lo, num);
            hi = Math.max(hi, num);
            cnts.put(num, cnts.getOrDefault(num, 0) + 1);
        }
        int start = lo;
        while (start <= hi) {
            for (int i = 0; i < k; i++) {
                int cnt = cnts.getOrDefault(start + i, 0);
                if (cnt == 0) {
                    return false;
                }
                cnts.put(start + i, cnt - 1);
            }
            while (start <= hi && cnts.getOrDefault(start, 0) == 0) {
                start++;
            }
        }
        return true;
    }
}
