package com.leetcode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * 1331. Rank Transform of an Array
 * https://leetcode.com/problems/rank-transform-of-an-array/
 */
public class Problem1331 {
    public int[] arrayRankTransform(int[] arr) {
        if (arr.length == 0) return arr;
        int[] sortedArr = Arrays.copyOf(arr, arr.length);
        Arrays.sort(sortedArr);
        Map<Integer, Integer> store = new HashMap<>();
        store.put(sortedArr[0], 1);
        for (int i = 1; i < sortedArr.length; i++) {
            if (sortedArr[i] == sortedArr[i - 1]) continue;
            store.put(sortedArr[i], store.get(sortedArr[i - 1]) + 1);
        }
        int[] ranks = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            ranks[i] = store.get(arr[i]);
        }
        return ranks;
    }
}
