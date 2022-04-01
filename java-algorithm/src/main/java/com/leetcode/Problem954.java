package com.leetcode;

import java.util.*;

public class Problem954 {
    public boolean canReorderDoubled(int[] arr) {
        List<Integer> posList = new ArrayList<>();
        List<Integer> negList = new ArrayList<>();
        for (int num : arr) {
            if (num >= 0) {
                posList.add(num);
            } else {
                negList.add(num);
            }
        }
        if (posList.size() % 2 == 1) {
            return false;
        }
        posList.sort((o1, o2) -> o1 - o2);
        negList.sort((o1, o2) -> o2 - o1);
        return check(posList) && check(negList);
    }

    private boolean check(List<Integer> nums) {
        if (nums.size() == 0) return true;
        Map<Integer, Integer> memo = new HashMap<>();
        for (Integer num : nums) {
            if (num % 2 != 0 || (!memo.containsKey(num / 2))) {
                int cnt = memo.getOrDefault(num, 0) + 1;
                memo.put(num, cnt);
            } else {
                int cnt = memo.get(num / 2) - 1;
                if (cnt == 0) {
                    memo.remove(num / 2);
                } else {
                    memo.put(num / 2, cnt);
                }
            }
        }
        return memo.size() == 0;
    }
}
