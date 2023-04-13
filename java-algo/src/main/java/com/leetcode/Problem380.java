package com.leetcode;

import java.util.*;

/**
 * 380. Insert Delete GetRandom O(1)
 * https://leetcode.com/problems/insert-delete-getrandom-o1/
 */
public class Problem380 {
    private static class RandomizedSet {
        private List<Integer> list;
        private Map<Integer, Integer> map;  // key: num, value: index

        public RandomizedSet() {
            this.list = new ArrayList<>();
            this.map = new HashMap<>();
        }

        public boolean insert(int val) {
            if (map.containsKey(val)) {
                return false;
            }
            list.add(val);
            map.put(val, list.size() - 1);
            return true;
        }

        public boolean remove(int val) {
            if (!map.containsKey(val)) {
                return false;
            }
            int index = map.get(val);
            list.set(index, list.get(list.size() - 1));
            list.remove(list.size() - 1);
            map.remove(val);
            if (index < list.size()) {
                map.put(list.get(index), index);
            }
            return true;
        }

        public int getRandom() {
            Random r = new Random();
            int pos = r.nextInt(list.size());
            return list.get(pos);
        }
    }
}
