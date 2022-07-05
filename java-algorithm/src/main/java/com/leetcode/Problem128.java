package com.leetcode;

/**
 * 128. Longest Consecutive Sequence
 * https://leetcode.com/problems/longest-consecutive-sequence/
 * 
 * Given an unsorted array of integers nums,
 * return the length of the longest consecutive elements sequence.
 * 
 * Follow up: Could you implement the O(n) solution?
 * 
 * Example 1:
 * 
 * Input: nums = [100,4,200,1,3,2]
 * Output: 4
 * Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
 * Therefore its length is 4.
 * 
 * Example 2:
 * 
 * Input: nums = [0,3,7,2,5,8,4,6,0,1]
 * Output: 9
 * 
 * Constraints:
 * 
 *     0 <= nums.length <= 10^4
 *     -10^9 <= nums[i] <= 10^9
 */
class Problem128 {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        Arrays.sort(nums);
        int ans =1, cur = 1;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] + 1 == nums[i + 1]) {
                cur++;
            } else if (nums[i] == nums[i + 1]) {
                continue;
            } else {
                ans = Math.max(ans, cur);
                cur = 1;
            }
        }
        return Math.max(ans, cur);
    }
}
