package com.leetcode;

/**
 * 135. Candy
 * https://leetcode.com/problems/candy/
 * There are N children standing in a line. Each child is assigned a rating value.
 *
 * You are giving candies to these children subjected to the following requirements:
 *
 *     Each child must have at least one candy.
 *     Children with a higher rating get more candies than their neighbors.
 *
 * What is the minimum candies you must give?
 *
 * Example 1:
 *
 * Input: [1,0,2]
 * Output: 5
 * Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
 *
 * Example 2:
 *
 * Input: [1,2,2]
 * Output: 4
 * Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
 *              The third child gets 1 candy because it satisfies the above two conditions.
 */
class Problem135 {
    public int candy(int[] ratings) {
        int n = ratings.length;
        int[] leftCandies = helper(ratings, 0, n, 1);
        int[] rightCandies = helper(ratings, n - 1, -1, -1);
        int ans= 0;
        for (int i = 0; i < n; i++) {
            ans += Math.max(leftCandies[i], rightCandies[i]);
        }
        return ans;
    }

    private int[] helper(int[] ratings, int start, int end, int step) {
        int[] candies = new int[ratings.length];
        candies[start] = 1;
        int i = start + step;
        while (i != end) {
            if (ratings[i] > ratings[i - step]) {
                candies[i] = candies[i - step] + 1;
            } else {
                candies[i] = 1;
            }
            i += step;
        }
        return candies;
    }
}
