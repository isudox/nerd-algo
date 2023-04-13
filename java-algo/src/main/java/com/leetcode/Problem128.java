package com.leetcode;

import java.util.HashSet;
import java.util.Set;

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
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        int ans = 0;
        for (int num : set) {
            if (!set.contains(num - 1)) {
                int curNum = num;
                int curCnt = 1;
                while (set.contains(curNum + 1)) {
                    curNum++;
                    curCnt++;
                }
                ans = Math.max(ans, curCnt);
            }
        }
        return ans;
    }
}
