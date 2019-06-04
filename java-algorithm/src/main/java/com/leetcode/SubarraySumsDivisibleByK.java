package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 974. Subarray Sums Divisible by K
 * https://leetcode.com/problems/subarray-sums-divisible-by-k/
 *
 * Given an array A of integers, return the number of (contiguous, non-empty)
 * subarrays that have a sum divisible by K.
 *
 * Example 1:
 *
 * Input: A = [4,5,0,-2,-3,1], K = 5
 * Output: 7
 * Explanation: There are 7 subarrays with a sum divisible by K = 5:
 * [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 *
 *
 * Note:
 *
 * 1 <= A.length <= 30000
 * -10000 <= A[i] <= 10000
 * 2 <= K <= 10000
 */
public class SubarraySumsDivisibleByK {
    public int subarraysDivByK(int[] A, int K) {
        int ans = 0;
        int sum = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);

        for (int i : A) {
            sum = ((sum + i) % K + K) % K;
            if (map.containsKey(sum)) {
                ans += map.get(sum);
                map.put(sum, map.get(sum) + 1);
            } else {
                map.put(sum, 1);
            }
        }

        return ans;
    }
}
