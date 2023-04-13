package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 213. House Robber II
 * https://leetcode.com/problems/house-robber-ii/
 *
 * You are a professional robber planning to rob houses along a street.
 * Each house has a certain amount of money stashed. All houses at this place
 * are arranged in a circle. That means the first house is the neighbor of the
 * last one. Meanwhile, adjacent houses have security system connected and it
 * will automatically contact the police if two adjacent houses were broken
 * into on the same night.
 *
 * Given a list of non-negative integers representing the amount of money of
 * each house, determine the maximum amount of money you can rob tonight
 * without alerting the police.
 *
 * Example 1:
 *
 * Input: [2,3,2]
 * Output: 3
 * Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
 *              because they are adjacent houses.
 * Example 2:
 *
 * Input: [1,2,3,1]
 * Output: 4
 * Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
 *              Total amount you can rob = 1 + 3 = 4.
 */
public class Problem213 {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        if (n == 2) return Math.max(nums[0], nums[1]);
        // if rob the first house
        List<int[]> dp = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            dp.add(new int[2]);
        }
        dp.set(0, new int[]{nums[0], nums[0]});
        dp.set(1, new int[]{nums[0], nums[0]});
        for (int i = 2; i < n - 1; i++) {
            dp.get(i)[0] = Math.max(dp.get(i - 1)[0], dp.get(i - 1)[1]);
            dp.get(i)[1] = dp.get(i - 1)[0] + nums[i];
        }
        int ans = Math.max(dp.get(n - 2)[0], dp.get(n - 2)[1]);
        // if not rob the first house
        dp.set(0, new int[]{0, 0});
        for (int i = 1; i < n; i++) {
            dp.get(i)[0] = Math.max(dp.get(i - 1)[0], dp.get(i - 1)[1]);
            dp.get(i)[1] = dp.get(i - 1)[0] + nums[i];
        }
        return Math.max(ans, Math.max(dp.get(n - 1)[0], dp.get(n - 1)[1]));
    }

}
