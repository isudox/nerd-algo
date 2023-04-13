package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 736. Parse Lisp Expression
 * https://leetcode.com/problems/parse-lisp-expression/
 */
public class Problem736 {
    char[] cs;
    String s;
    public int evaluate(String _s) {
        s = _s;
        cs = s.toCharArray();
        return dfs(0, cs.length - 1, new HashMap<>());
    }
    int dfs(int l, int r, Map<String, Integer> map) {
        if (cs[l] == '(') {
            int idx = l;
            while (cs[idx] != ' ') idx++;
            String op = s.substring(l + 1, idx);
            r--;
            if (op.equals("let")) {
                for (int i = idx + 1; i <= r; ) {
                    int j = getRight(i, r);
                    String key = s.substring(i, j);
                    if (j >= r) return dfs(i, j - 1, new HashMap<>(map));
                    j++; i = j;
                    j = getRight(i, r);
                    int value = dfs(i, j - 1, new HashMap<>(map));
                    map.put(key, value);
                    i = j + 1;
                }
                return -1; // never
            } else {
                int j = getRight(idx + 1, r);
                int a = dfs(idx + 1, j - 1, new HashMap<>(map)), b = dfs(j + 1, r, new HashMap<>(map));
                return op.equals("add") ? a + b : a * b;
            }
        } else {
            String cur = s.substring(l, r + 1);
            if (map.containsKey(cur)) return map.get(cur);
            return Integer.parseInt(cur);
        }
    }
    int getRight(int left, int end) {
        int right = left, score = 0;
        while (right <= end) {
            if (cs[right] == '(') {
                score++; right++;
            } else if (cs[right] == ')') {
                score--; right++;
            } else if (cs[right] == ' ') {
                if (score == 0) break;
                right++;
            } else {
                right++;
            }
        }
        return right;
    }
}
