package com.leetcode;

import java.util.*;

/**
 * 398.
 */
public class Problem398 {
    private static class Solution {

        private final Map<Integer, List<Integer>> store;
        private final Random random;

        public Solution(int[] nums) {
            this.store = new HashMap<>();
            this.random = new Random();
            for (int i = 0; i < nums.length; i++) {
                int num = nums[i];
                List<Integer> list = store.getOrDefault(num, new ArrayList<>());
                list.add(i);
                store.put(num, list);
            }
        }

        public int pick(int target) {
            List<Integer> list = store.get(target);
            return list.get(random.nextInt(list.size()));
        }
    }
}
