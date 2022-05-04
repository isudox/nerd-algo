package com.leetcode;

import java.util.*;

public class Problem1679 {
    public int maxOperations(int[] nums, int k) {
        //Arrays.sort(nums);
        Map<Integer, Integer> store = new HashMap<>();
        int ans = 0;
        for (int num : nums) {
            int target = k - num;
            if (store.containsKey(target)) {
                ans++;
                if (store.get(target) == 1) {
                    store.remove(target);
                } else {
                    store.put(target, store.get(target) - 1);
                }
            } else {
                int cnt = store.getOrDefault(num, 0);
                store.put(num, cnt + 1);
            }
        }
        return ans;
    }
}
