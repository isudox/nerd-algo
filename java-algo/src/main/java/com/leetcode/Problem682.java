package com.leetcode;


import java.util.ArrayList;
import java.util.List;

/**
 * 682. Baseball Game
 * https://leetcode.com/problems/baseball-game/
 */
public class Problem682 {
    public int calPoints(String[] ops) {
        List<Integer> q = new ArrayList<>();
        boolean isNeg = false;
        for (String op : ops) {
            switch (op) {
                case "+": {
                    q.add(q.get(q.size() - 1) + q.get(q.size() - 2));
                    break;
                }
                case "D": {
                    q.add(q.get(q.size() - 1) * 2);
                    break;
                }
                case "C":
                    q.remove(q.size() - 1);
                    break;
                case "-":
                    isNeg = true;
                default:
                    int num = Integer.parseInt(op);
                    q.add(isNeg ? -num : num);
                    isNeg = false;
            }
        }
        int ans = 0;
        for (Integer n : q) {
            ans += n;
        }
        return ans;
    }
}
