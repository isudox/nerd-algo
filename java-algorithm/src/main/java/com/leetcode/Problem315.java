package com.leetcode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * 315. Count of Smaller Numbers After Self
 * https://leetcode.com/problems/count-of-smaller-numbers-after-self/
 *
 * You are given an integer array nums and you have to return a new counts array.
 * The counts array has the property where counts[i] is the number of smaller
 * elements to the right of nums[i].
 *
 * Example:
 *
 * Input: [5,2,6,1]
 * Output: [2,1,1,0]
 * Explanation:
 * To the right of 5 there are 2 smaller elements (2 and 1).
 * To the right of 2 there is only 1 smaller element (1).
 * To the right of 6 there is 1 smaller element (1).
 * To the right of 1 there is 0 smaller element.
 */
public class Problem315 {
    public List<Integer> countSmaller(int[] nums) {
        int n = nums.length;
        List<Integer> ans = new ArrayList<>(n);
        List<Integer> sortedNums = new ArrayList<>(n);
        for (int i = n - 1; i > -1; i--) {
            int index = binarySearch(sortedNums, nums[i]);
            sortedNums.add(index, nums[i]);
            ans.add(index);
        }
        Collections.reverse(ans);
        return ans;
    }

    private int binarySearch(List<Integer> list, int target) {
        int lo = 0, hi = list.size();
        while (lo < hi) {
            // int mid = lo + (hi - lo) >> 1;
            int mid = lo + (hi - lo) / 2;
            if (list.get(mid) < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
