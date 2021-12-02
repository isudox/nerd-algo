package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 1005. Maximize Sum Of Array After K Negations
 * https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
 */
public class Problem1005 {
    public int largestSumAfterKNegations(int[] nums, int k) {
        Arrays.sort(nums);
        List<Integer> negatives = new ArrayList<>(nums.length);
        List<Integer> positives = new ArrayList<>(nums.length);
        int sum = 0;
        for (int num : nums) {
            if (num < 0) {
                negatives.add(num);
            } else {
                positives.add(num);
            }
            sum += num;
        }
        if (negatives.isEmpty()) {
            return k % 2 == 0 ? sum : sum - positives.get(0) * 2;
        }
        if (negatives.size() >= k) {
            for (int i = 0; i < k; i++) {
                sum -= negatives.get(i) * 2;
            }
            return sum;
        }
        for (int num : negatives) {
            sum -= num * 2;
        }
        k -= negatives.size();
        if (k % 2 == 0) {
            return sum;
        }
        if (positives.isEmpty()) {
            return sum + negatives.get(negatives.size() - 1) * 2;
        }
        return Math.max(sum - positives.get(0) * 2, sum + negatives.get(negatives.size() - 1) * 2);
    }
}
