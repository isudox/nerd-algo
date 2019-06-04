package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 41. First Missing Positive
 * https://leetcode.com/problems/first-missing-positive/
 *
 * Given an unsorted integer array, find the smallest missing positive integer.
 *
 * Example 1:
 *
 * Input: [1,2,0]
 * Output: 3
 *
 *
 * Example 2:
 *
 * Input: [3,4,-1,1]
 * Output: 2
 *
 *
 * Example 3:
 *
 * Input: [7,8,9,11,12]
 * Output: 1
 *
 *
 * Note:
 *
 * Your algorithm should run in O(n) time and uses constant extra space.
 */
public class FirstMissingPositive {

    public int firstMissingPositive(int[] nums) {
        Map<Integer, Boolean> checked = new HashMap<>();
        int ans = 1;
        for (int num : nums) {
            if (num > 0) {
                checked.put(num, true);
                if (num == ans) {
                    while (checked.getOrDefault(ans, false)) {
                        ans++;
                    }
                }
            }
        }
        return ans;
    }
}
