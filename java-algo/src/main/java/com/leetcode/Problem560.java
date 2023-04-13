package com.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 560. Subarray Sum Equals K
 * https://leetcode.com/problems/subarray-sum-equals-k/
 *
 * Given an array of integers and an integer k, you need to find
 * the total number of continuous subarrays whose sum equals to k.
 *
 * Example 1:
 *
 * Input:nums = [1,1,1], k = 2
 * Output: 2
 *
 * Constraints:
 *
 * The length of the array is in range [1, 20,000].
 * The range of numbers in the array is [-1000, 1000] and the range
 * of the integer k is [-1e7, 1e7].
 */
public class Problem560 {
    /**
     * Time complexity: O(N)
     * Space complexity: O(N)
     */
    public int subarraySum(int[] nums, int k) {
        int sum = 0;
        int ans = 0;
        Map<Integer, Integer> memo = new HashMap<>();
        memo.put(0, 1);
        for (int num : nums) {
            sum += num;
            if (memo.containsKey(sum - k)) {
                ans += memo.get(sum - k);
            }
            memo.put(sum, memo.getOrDefault(sum, 0) + 1);
        }
        return ans;
    }

    /**
     * Brute force.
     * Time complexity: O(N^2)
     * Space complexity: O(1)
     */
    public int bruteForce(int[] nums, int k) {
        int n = nums.length;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int curSum = 0;
            for (int j = i; j < n; j++) {
                curSum += nums[j];
                if (curSum == k)
                    ans++;
            }
        }
        return ans;
    }
}
