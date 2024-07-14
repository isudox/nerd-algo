package com.leetcode;

import java.util.*;

/**
 * 726. Number of Atoms
 * https://leetcode.com/problems/number-of-atoms/
 * TODO
 */
public class Problem726 {
    int i, n;
    String formula;

    public String countOfAtoms(String formula) {
        this.i = 0;
        this.n = formula.length();
        this.formula = formula;
        Deque<Map<String, Integer>> stack = new LinkedList<>();
        stack.push(new HashMap<>());
        while (i < formula.length()) {
            char c = formula.charAt(i);
            if (c == '(') {
                i++;
                stack.push(new HashMap<>());
            } else if (c == ')') {
                i++;
                int num = parseNum();
                Map<String, Integer> pop = stack.pop();
                Map<String, Integer> top = stack.peek();
                for (Map.Entry<String, Integer> e : pop.entrySet()) {
                    String atom = e.getKey();
                    int v = e.getValue();
                    top.put(atom, top.getOrDefault(atom, 0) + v * num);
                }
            } else {
                String atom = parseAtom();
                int num = parseNum();
                Map<String, Integer> top = stack.peek();
                top.put(atom, top.getOrDefault(atom, 0) + num);
            }
        }
        Map<String, Integer> map = stack.pop();
        TreeMap<String, Integer> treeMap = new TreeMap<String, Integer>(map);
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, Integer> entry : treeMap.entrySet()) {
            String atom = entry.getKey();
            int count = entry.getValue();
            sb.append(atom);
            if (count > 1) {
                sb.append(count);
            }
        }
        return sb.toString();
    }

    private int parseNum() {
        if (i == formula.length() || !Character.isDigit(formula.charAt(i))) {
            return 1;
        }
        int num = 0;
        while (i < formula.length() && Character.isDigit(formula.charAt(i))) {
            num = num * 10 + formula.charAt(i++) - '0';
        }
        return num;
    }

    private String parseAtom() {
        StringBuilder sb = new StringBuilder();
        do {
            sb.append(formula.charAt(i++));
        } while (i < n && Character.isLowerCase(formula.charAt(i)));
        return sb.toString();
    }
}
