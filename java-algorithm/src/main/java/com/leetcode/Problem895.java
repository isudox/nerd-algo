package com.leetcode;

import java.util.*;

/**
 * 895. Maximum Frequency Stack
 * https://leetcode.com/problems/maximum-frequency-stack/
 */
public class Problem895 {
    static class FreqStack {
        List<Integer> list;
        Map<Integer, Integer> counter;
        Map<Integer, Deque<Integer>> mapper;
        int maxCnt;

        public FreqStack() {
            list = new ArrayList<>();
            counter = new HashMap<>();
            mapper = new HashMap<>();
        }

        public void push(int val) {
            counter.put(val, counter.getOrDefault(val, 0) + 1);
            mapper.putIfAbsent(counter.get(val), new ArrayDeque<>());
            mapper.get(counter.get(val)).push(val);
            maxCnt = Math.max(maxCnt, counter.get(val));
        }

        public int pop() {
            int val = mapper.get(maxCnt).peek();
            counter.put(val, counter.get(val) - 1);
            mapper.get(maxCnt).pop();
            if (mapper.get(maxCnt).isEmpty()) {
                maxCnt--;
            }
            return val;
        }
    }
}
