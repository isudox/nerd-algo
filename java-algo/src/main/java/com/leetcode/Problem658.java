package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 658. Find K Closest Elements
 * https://leetcode.com/problems/find-k-closest-elements/
 */
public class Problem658 {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int idx = 0;
        int diff = 0;
        for (int i = 0; i < k; i++) {
            diff += Math.abs(arr[i] - x);
        }
        for (int i = 1; i <= arr.length - k; i++) {
            int curDiff = diff - Math.abs(arr[i - 1] - x) + Math.abs(arr[i + k - 1] - x);
            if (curDiff < diff) {
                diff = curDiff;
                idx = i;
            }
        }
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            ans.add(arr[idx + i]);
        }
        return ans;
    }
}
