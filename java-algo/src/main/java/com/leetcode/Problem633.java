package com.leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * 633. Sum of Square Numbers
 * https://leetcode.com/problems/sum-of-square-numbers/
 */
public class Problem633 {
    public boolean judgeSquareSum(int c) {
        int limit = (int) Math.sqrt(c) + 1;
        int mid = (int) Math.sqrt((double) c / 2) + 1;
        Set<Integer> store = new HashSet<>();
        for (int i = 0; i <= limit; i++) {
            store.add(i * i);
        }
        for (int i = 0; i <= mid; i++) {
            if (store.contains(c - i * i)) {
                return true;
            }
        }
        return false;
    }
}
