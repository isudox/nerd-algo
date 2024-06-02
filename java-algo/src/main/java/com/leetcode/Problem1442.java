package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 1442. Count Triplets That Can Form Two Arrays of Equal XOR
 * https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
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
