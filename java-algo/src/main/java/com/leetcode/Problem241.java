package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 241. Different Ways to Add Parentheses
 * https://leetcode.com/problems/different-ways-to-add-parentheses/
 */
public class Problem241 {
    public List<Integer> diffWaysToCompute(String expression) {
        return dfs(expression.toCharArray(), 0, expression.length() - 1);
    }

    private List<Integer> dfs(char[] chars, int l, int r) {
        List<Integer> ret = new ArrayList<>();
        for (int i = l; i <= r; i++) {
            char c = chars[i];
            if (c >= '0' && c <= '9') {
                continue;
            }
            List<Integer> left = dfs(chars, l, i - 1), right = dfs(chars, i + 1, r);
            for (int x : left) {
                for (int y : right) {
                    int cur = 0;
                    if (c == '+') {
                        cur = x + y;
                    } else if (c == '-') {
                        cur = x - y;
                    } else if (c == '*') {
                        cur = x * y;
                    }
                    ret.add(cur);
                }
            }
        }
        if (ret.isEmpty()) {
            int cur = 0;
            for (int i = l; i <= r; i++) {
                cur = cur * 10 + (chars[i] - '0');
            }
            ret.add(cur);
        }
        return ret;
    }
}
