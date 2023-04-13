package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 904. Fruit Into Baskets
 * https://leetcode.com/problems/fruit-into-baskets/
 */
public class Problem904 {
    public int totalFruit(int[] fruits) {
        int ans = 0;
        int i = 0;
        Map<Integer, Integer> store = new HashMap<>();
        for (int j = 0; j < fruits.length; j++) {
            store.put(fruits[j], store.getOrDefault(fruits[j], 0) + 1);
            while (store.size() > 2) {
                store.put(fruits[i], store.get(fruits[i]) - 1);
                if (store.get(fruits[i]) == 0) {
                    store.remove(fruits[i]);
                }
                i++;
            }
            ans = Math.max(ans, j - i + 1);
        }
        return ans;
    }
}
