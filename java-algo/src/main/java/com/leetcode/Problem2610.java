package com.leetcode;

import java.util.*;

/**
 * 2610. Convert an Array Into a 2D Array With Conditions
 * https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
 */
public class Problem2610 {
    public List<List<Integer>> findMatrix(int[] nums) {
        List<Integer> list = new ArrayList<>();
        Map<Integer, Integer> store = new HashMap<>();
        for (int num : nums) {
            if (!store.containsKey(num)) {
                store.put(num, 1);
                list.add(num);
            } else {
                store.put(num, store.get(num) + 1);
            }
        }
        List<List<Integer>> ans = new ArrayList<>();
        while (!list.isEmpty()) {
            ans.add(new ArrayList<>(list));
            Iterator<Integer> it = list.iterator();
            while (it.hasNext()) {
                int num = it.next();
                store.put(num, store.get(num) - 1);
                if (store.get(num) == 0) {
                    it.remove();
                }
            }
        }
        return ans;
    }
}
