package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 198. House Robber
 * https://leetcode.com/problems/house-robber/
 *
 * You are a professional robber planning to rob houses along a street.
 * Each house has a certain amount of money stashed, the only constraint stopping
 * you from robbing each of them is that adjacent houses have security system
 * connected and it will automatically contact the police if two adjacent houses
 * were broken into on the same night.
 *
 * Given a list of non-negative integers representing the amount of money of
 * each house, determine the maximum amount of money you can rob tonight
 * without alerting the police.
 *
 * Example 1:
 *
 * Input: nums = [1,2,3,1]
 * Output: 4
 * Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
 *              Total amount you can rob = 1 + 3 = 4.
 *
 * Example 2:
 *
 * Input: nums = [2,7,9,3,1]
 * Output: 12
 * Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
 *              Total amount you can rob = 2 + 9 + 1 = 12.
 *
 * Constraints:
 *
 * 0 <= nums.length <= 100
 * 0 <= nums[i] <= 400
 */
public class Problem198 {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        List<int[]> dp = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            dp.add(new int[2]);
        }
        dp.set(0, new int[]{0, nums[0]});
        for (int i = 1; i < n; i++) {
            dp.set(i, new int[]{Math.max(dp.get(i - 1)[0], dp.get(i - 1)[1]), dp.get(i - 1)[0] + nums[i]});
        }
        return Math.max(dp.get(n - 1)[0], dp.get(n - 1)[1]);
    }
}
