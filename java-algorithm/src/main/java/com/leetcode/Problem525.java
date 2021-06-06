package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 525. Contiguous Array
 * https://leetcode.com/problems/contiguous-array/
 *
 * Given a binary array nums, return the maximum length of a contiguous
 * subarray with an equal number of 0 and 1.
 *
 * Example 1:
 * Input: nums = [0,1]
 * Output: 2
 * Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
 *
 * Example 2:
 * Input: nums = [0,1,0]
 * Output: 2
 * Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 *
 * Constraints:
 *
 * 1 <= nums.length <= 10^5
 * nums[i] is either 0 or 1.
 */
public class Problem525 {
    public int findMaxLength(int[] nums) {
        Map<Integer, Integer> posMap = new HashMap<>();
        posMap.put(0, -1);
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            nums[i] = (nums[i] == 1 ? 1 : -1) + (i > 0 ? nums[i - 1] : 0);
            if (posMap.containsKey(nums[i]))
                ans = Math.max(ans, i - posMap.get(nums[i]));
            else
                posMap.put(nums[i], i);
        }
        return ans;
    }
}
