package com.leetcode;

/**
 * 985. Sum of Even Numbers After Queries
 * https://leetcode.com/problems/sum-of-even-numbers-after-queries/
 */
class Problem985 {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        int even = 0;
        for (int num : nums) {
            if (num % 2 == 0) even += num;
        }
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int[] query = queries[i];
            int old = nums[query[1]], cur = old + query[0];
            nums[query[1]] = cur;
            if (old % 2 == 0) {
                even -= old;
            }
            if (cur % 2 == 0) {
                even += cur;
            }
            ans[i] = even;
        }
        return ans;
    }
}
