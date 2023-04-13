package com.leetcode;

import com.common.Logger;

import java.util.HashMap;
import java.util.Map;

/**
 * 1442. Count Triplets That Can Form Two Arrays of Equal XOR
 * https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
 *
 * Given an array of integers arr.
 *
 * We want to select three indices i, j and k where
 * (0 <= i < j <= k < arr.length).
 *
 * Let's define a and b as follows:
 *
 * a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
 * b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
 *
 * Note that ^ denotes the bitwise-xor operation.
 *
 * Return the number of triplets (i, j and k) Where a == b.
 *
 * Example 1:
 *
 * Input: arr = [2,3,1,6,7]
 * Output: 4
 * Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
 *
 * Example 2:
 *
 * Input: arr = [1,1,1,1,1]
 * Output: 10
 *
 * Example 3:
 *
 * Input: arr = [2,3]
 * Output: 0
 *
 * Example 4:
 *
 * Input: arr = [1,3,5,7,9]
 * Output: 3
 *
 * Example 5:
 *
 * Input: arr = [7,11,12,9,5,2,7,17,22]
 * Output: 8
 *
 * Constraints:
 *
 * 1 <= arr.length <= 300
 * 1 <= arr[i] <= 10^8
 */
public class Problem1442 {
    public int countTriplets(int[] arr) {
        int[] preXor = new int[arr.length + 1];
        for (int i = 0; i < arr.length; i++) {
            preXor[i + 1] = preXor[i] ^ arr[i];
        }
        int ans = 0;
        for (int i = 0; i < arr.length - 1; i++) {
            for (int k = i + 1; k < arr.length; k++) {
                if ((preXor[i] == preXor[k + 1])) {
                    ans += k - i;
                }
            }
        }
        return ans;
    }

    public int countTriplets2(int[] arr) {
        int[] preXor = new int[arr.length + 1];
        for (int i = 0; i < arr.length; i++) {
            preXor[i + 1] = preXor[i] ^ arr[i];
        }
        int ans = 0;
        Map<Integer, Integer> counter = new HashMap<>();
        Map<Integer, Integer> total = new HashMap<>();
        for (int k = 0; k < arr.length; k++) {
            int cur = preXor[k + 1];
            if (counter.containsKey(cur)) {
                ans += counter.get(cur) * k - total.get(cur);
            }
            counter.put(preXor[k], counter.getOrDefault(preXor[k], 0) + 1);
            total.put(preXor[k], total.getOrDefault(preXor[k], 0) + k);
        }
        return ans;
    }
}
