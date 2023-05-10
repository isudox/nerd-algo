package com.leetcode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * 1015. Smallest Integer Divisible by K
 * https://leetcode.com/problems/smallest-integer-divisible-by-k/
 */
public class Problem1015 {
    public int smallestRepunitDivByK(int k) {
        if (k % 2 == 0) {
            return -1;
        }
        Map<Integer, Integer> store = new HashMap<>();
        Set<Integer> seen = new HashSet<>();
        store.put(0, 0);
        int x = 1, rem = 0;
        while (!seen.contains(rem)) {
            seen.add(rem);
            rem = (store.get(x - 1) * 10 + 1) % k;
            if (rem == 0) {
                return x;
            }
            if (seen.contains(rem)) {
                return -1;
            }
            store.put(x, rem % k);
            x++;
        }
        return -1;
    }
}
