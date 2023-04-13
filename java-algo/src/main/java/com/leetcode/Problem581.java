package com.leetcode;

import java.util.Arrays;

/**
 * 581. Shortest Unsorted Continuous Subarray
 * https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
 */
public class Problem581 {
    /**
     * Time complexity: O(N)
     * Space complexity: O(1)
     */
    public int findUnsortedSubarray(int[] nums) {
        int n = nums.length;
        if (n <= 1)
            return 0;
        int l = -1, r = -1;
        int curMax = nums[0];
        for (int i = 1; i < n; i++) {
            if (nums[i] >= nums[i - 1] && nums[i] >= curMax) {
                curMax = nums[i];
                continue;
            }
            if (l < 0)
                l = i - 1;
            while (l > 0 && nums[l - 1] > nums[i])
                l--;
            r = i;
        }
        if (l == -1)
            return 0;
        return r - l + 1;
    }

    /**
     * Time complexity: O(N log N)
     * Space complexity: O(N)
     */
    public int findUnsortedSubarray2(int[] nums) {
        int n = nums.length;
        if (n < 2) {
            return 0;
        }
        int[] sortedNums = new int[n];
        System.arraycopy(nums, 0, sortedNums, 0, n);
        Arrays.sort(sortedNums);
        int i = 0, j = n - 1;
        while (i < n && sortedNums[i] == nums[i]) {
            i++;
        }
        while (j >= 0 && sortedNums[j] == nums[j]) {
            j--;
        }
        return i < j ? j - i + 1 : 0;
    }

    /**
     * Time complexity: O(N log N)
     * Space complexity: O(N)
     */
    public int findUnsortedSubarray3(int[] nums) {
        int n = nums.length;
        if (n < 2) {
            return 0;
        }
        int max = nums[0], right = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] > max) {
                max = nums[i];
                continue;
            }
            if (nums[i] < max) {
                right = i;
            }
        }
        int min = nums[n - 1], left = n - 1;
        for (int j = n - 2; j >= 0; j--) {
            if (nums[j] < min) {
                min = nums[j];
                continue;
            }
            if (nums[j] > min) {
                left = j;
            }
        }
        return left > right ? 0 : right - left + 1;
    }
}
