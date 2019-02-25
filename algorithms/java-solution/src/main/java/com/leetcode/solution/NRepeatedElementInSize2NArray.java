package com.leetcode.solution;

import java.util.HashMap;
import java.util.Map;

/**
 * 961. N-Repeated Element in Size 2N Array
 * https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
 *
 * In a array A of size 2N, there are N+1 unique elements, and exactly one of
 * these elements is repeated N times.
 *
 * Return the element repeated N times.
 *
 * Example 1:
 *
 * Input: [1,2,3,3]
 * Output: 3
 *
 * Example 2:
 *
 * Input: [2,1,2,5,3,2]
 * Output: 2
 *
 * Example 3:
 *
 * Input: [5,1,5,2,5,3,5,4]
 * Output: 5
 *
 * Note:
 *
 * 4 <= A.length <= 10000
 * 0 <= A[i] < 10000
 * A.length is even
 */
public class NRepeatedElementInSize2NArray {

    public int repeatedNTimes(int[] a) {
        int n = a.length / 2;
        Map<Integer, Integer> counter = new HashMap<>();
        for (int i : a) {
            counter.put(i, counter.getOrDefault(i, 0) + 1);
            if (counter.get(i) == n) {
                return i;
            }
        }
        throw new IllegalArgumentException();
    }
}
