package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 546. Remove Boxes
 * https://leetcode.com/problems/remove-boxes/
 *
 * You are given several boxes with different colors represented by different
 * positive numbers.
 *
 * You may experience several rounds to remove boxes until there is no box left.
 * Each time you can choose some continuous boxes with the same color (i.e.,
 * composed of k boxes, k >= 1), remove them and get k * k points.
 *
 * Return the maximum points you can get.
 *
 * Example 1:
 *
 * Input: boxes = [1,3,2,2,2,3,4,3,1]
 * Output: 23
 * Explanation:
 * [1, 3, 2, 2, 2, 3, 4, 3, 1]
 * ----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
 * ----> [1, 3, 3, 3, 1] (1*1=1 points)
 * ----> [1, 1] (3*3=9 points)
 * ----> [] (2*2=4 points)
 *
 * Example 2:
 *
 * Input: boxes = [1,1,1]
 * Output: 9
 *
 * Example 3:
 *
 * Input: boxes = [1]
 * Output: 1
 *
 * Constraints:
 *
 * 1 <= boxes.length <= 100
 * 1 <= boxes[i] <= 100
 */
public class Problem546 {
    public int removeBoxes(int[] boxes) {
        Map<String, Integer> memo = new HashMap<>();
        return backtrack(boxes, memo);
    }

    private int backtrack(int[] nums, Map<String, Integer> memo) {
        String key = genKey(nums);
        if (memo.containsKey(key)) return memo.get(key);
        if (nums.length == 0) return 0;
        int ret = 0;
        int i = 0;
        while (i < nums.length) {
            int j = i;
            while (j < nums.length) {
                if (nums[i] != nums[j]) break;
                j++;
            }
            int[] newNums = new int[nums.length - j + i];
            int k = 0;
            for (int m = 0; m < nums.length; m++) {
                if (m < i || m >= j) {
                    newNums[k++] = nums[m];
                }
            }
            ret = Math.max(ret, backtrack(newNums, memo) + (j - i) * (j - i));
            i = j;
        }
        memo.put(key, ret);
        return ret;
    }

    private String genKey(int[] nums) {
        StringBuilder sb = new StringBuilder();
        for (int num : nums) {
            sb.append(num);
        }
        return sb.toString();
    }
}
