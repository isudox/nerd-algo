package com.leetcode;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 1200. Minimum Absolute Difference
 * https://leetcode.com/problems/minimum-absolute-difference/
 */
class Problem1200 {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);
        int diff = arr[arr.length - 1] - arr[0];
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] - arr[i - 1] > diff) {
                continue;
            }
            List<Integer> cur = new ArrayList<>();
            cur.add(arr[i - 1]);
            cur.add(arr[i]);
            if (arr[i] - arr[i - 1] < diff) {
                diff = arr[i] - arr[i - 1];
                ans.clear();
                ans.add(cur);
            } else {
                ans.add(cur);
            }
        }
        return ans;
    }
}
