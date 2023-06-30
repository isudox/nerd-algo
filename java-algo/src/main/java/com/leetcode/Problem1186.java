package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 1186. Maximum Subarray Sum with One Deletion
 * https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
 */
class Problem1186 {
    public int maximumSum(int[] arr) {
        int n = arr.length;
        int[] presum = new int[n + 1];
        List<Integer> negs = new ArrayList<>();
        negs.add(-1);
        for (int i = 0; i < n; i++) {
            presum[i + 1] = presum[i] + arr[i];
            if (arr[i] < 0) {
                negs.add(i);
            }
        }
        int ans = presum[n];
        for (int i = 1; i < negs.size(); i++) {
            int left = negs.get(i - 1), right = n - 1;
            if (i < negs.size() - 1) {
                right = negs.get(i + 1) - 1;
            }
            if (right - left == 1) {
                ans = Math.max(ans, arr[negs.get(i)]);
            } else {
                ans = Math.max(ans, presum[right + 1] - presum[left + 1] - arr[negs.get(i)]);
            }
        }
        return ans;
    }
}
