package com.leetcode;

import java.util.TreeSet;

/**
 * 220. Contains Duplicate III
 * https://leetcode.com/problems/contains-duplicate-iii/
 *
 * Given an integer array nums and two integers k and t, return true if there
 * are two distinct indices i and j in the array such that abs(nums[i] -
 * nums[j]) <= t and abs(i - j) <= k.
 *
 * Example 1:
 * Input: nums = [1,2,3,1], k = 3, t = 0
 * Output: true
 *
 * Example 2:
 * Input: nums = [1,0,1,1], k = 1, t = 2
 * Output: true
 *
 * Example 3:
 * Input: nums = [1,5,9,1,5,9], k = 2, t = 3
 * Output: false
 *
 * Constraints:
 *
 * 0 <= nums.length <= 2 * 10^4
 * -2^31 <= nums[i] <= 2^31 - 1
 * 0 <= k <= 10^4
 * 0 <= t <= 2^31 - 1
 */
public class Problem220 {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        int n = nums.length;
        TreeSet<Long> store = new TreeSet<>();
        for (int i = 0; i < n; i++) {
            long num = (long) nums[i];
            // to find a ceiling which between [nums[i] - t, nums[i] + t]
            Long ceiling = store.ceiling(num - (long) t);
            if (null != ceiling && ceiling <= num + (long) t) {
                return true;
            }
            store.add(num);
            if (i >= k) {
                store.remove((long) nums[i - k]);
            }
        }
        return false;
    }
}
