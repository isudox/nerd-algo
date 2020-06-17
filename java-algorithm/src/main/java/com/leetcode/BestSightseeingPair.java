package com.leetcode;

/**
 * 1014. Best Sightseeing Pair
 * https://leetcode.com/problems/best-sightseeing-pair/
 *
 * Given an array A of positive integers, A[i] represents the value
 * of the i-th sightseeing spot, and two sightseeing spots i and
 * j have distance j - i between them.
 *
 * The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) :
 * the sum of the values of the sightseeing spots, minus the distance between them.
 *
 * Return the maximum score of a pair of sightseeing spots.
 *
 *
 * Example 1:
 *
 * Input: [8,1,5,2,6]
 * Output: 11
 * Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
 *
 *
 * Note:
 *
 * 2 <= A.length <= 50000
 * 1 <= A[i] <= 1000
 */
public class BestSightseeingPair {

    public int maxScoreSightseeingPair(int[] arr) {
        // time complexity: O(N)
        // space complexity: O(1)
        int n = arr.length;
        int left = arr[0];  // arr[i] + i
        int ans = 0;
        for (int i = 1; i < n; i++) {
            ans = Math.max(ans, left + arr[i] - i);
            left = Math.max(left, arr[i] + i);
        }
        return ans;
    }

    public int bruteForce(int[] arr) {
        // time complexity: O(N^2)
        // space complexity: O(1)
        int ans = 0;
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                int cur = arr[i] + arr[j] + i - j;
                ans = Math.max(ans, cur);
            }
        }
        return ans;
    }
}
