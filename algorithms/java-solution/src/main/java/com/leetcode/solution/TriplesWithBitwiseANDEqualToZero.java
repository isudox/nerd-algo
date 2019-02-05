/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2017-2019 sudoz
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

package com.leetcode.solution;

import java.util.HashMap;
import java.util.Map;

/**
 * 982. Triples with Bitwise AND Equal To Zero
 * https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/
 *
 * Given an array of integers A, find the number of triples of indices (i, j, k) such that:
 *
 *   0 <= i < A.length
 *   0 <= j < A.length
 *   0 <= k < A.length
 *   A[i] & A[j] & A[k] == 0, where & represents the bitwise-AND operator.
 *
 * Example 1:
 *
 *   Input: [2,1,3]
 *   Output: 12
 *   Explanation: We could choose the following i, j, k triples:
 *   (i=0, j=0, k=1) : 2 & 2 & 1
 *   (i=0, j=1, k=0) : 2 & 1 & 2
 *   (i=0, j=1, k=1) : 2 & 1 & 1
 *   (i=0, j=1, k=2) : 2 & 1 & 3
 *   (i=0, j=2, k=1) : 2 & 3 & 1
 *   (i=1, j=0, k=0) : 1 & 2 & 2
 *   (i=1, j=0, k=1) : 1 & 2 & 1
 *   (i=1, j=0, k=2) : 1 & 2 & 3
 *   (i=1, j=1, k=0) : 1 & 1 & 2
 *   (i=1, j=2, k=0) : 1 & 3 & 2
 *   (i=2, j=0, k=1) : 3 & 2 & 1
 *   (i=2, j=1, k=0) : 3 & 1 & 2
 *
 * Note:
 *
 *   1 <= A.length <= 1000
 *   0 <= A[i] < 2^16
 */
public class TriplesWithBitwiseANDEqualToZero {

    public int countTriplets(int[] A) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i : A) {
            for (int j : A) {
                int key = i & j;
                int value = map.get(key) == null ? 1 : map.get(key) + 1;
                map.put(key, value);
            }
        }

        int count = 0;
        for (int i : A) {
            for (int key : map.keySet()) {
                if ((key & i) == 0) {
                    count += map.get(key);
                }
            }
        }

        return count;
    }
}
