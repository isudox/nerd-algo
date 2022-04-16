package com.leetcode;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

/**
 * 385. Mini Parser
 * https://leetcode.com/problems/mini-parser/
 * "[123,[456,[789]]]"
 * "[123,[456],[789]]"
 */
public class Problem385 {
    public NestedInteger deserialize(String s) {
        if (s.charAt(0) != '[') {
            return new NestedInteger(Integer.parseInt(s));
        }
        Deque<NestedInteger> stack = new ArrayDeque<>();
        NestedInteger res = new NestedInteger();
        stack.push(res);
        int left = 1, right = 1;
        for (; right < s.length(); right++) {
            char ch = s.charAt(right);
            if (ch == '[') {
                NestedInteger ni = new NestedInteger();
                left = right + 1;
                stack.peek().add(ni);
                stack.push(ni);
            } else if (ch == ']' || ch == ',') {
                if (left < right) {
                    int val = Integer.parseInt(s.substring(left, right));
                    stack.peek().add(new NestedInteger(val));
                }
                left = right + 1;
                if (ch == ']') {
                    stack.pop();
                }
            }
        }
        return res;
    }

    private static class NestedInteger {
        private int val;
        private List<NestedInteger> list;

        public NestedInteger() {
        }

        NestedInteger(int value) {
            this.val = value;
        }

        public void add(NestedInteger ni) {
            if (list == null) {
                list = new ArrayList<>();
            }
            list.add(ni);
        }
    }
}
