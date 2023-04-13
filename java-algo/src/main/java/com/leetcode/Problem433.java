package com.leetcode;

import java.util.*;

/**
 * 433. Minimum Genetic Mutation
 * https://leetcode.com/problems/minimum-genetic-mutation/
 */
public class Problem433 {
    public int minMutation(String start, String end, String[] bank) {
        String[] chars = new String[]{"A", "C", "G", "T"};
        Queue<String> queue = new LinkedList<>();
        Set<String> set = new HashSet<>();
        Collections.addAll(set, bank);
        if (!set.contains(end)) {
            return -1;
        }
        queue.offer(start);
        int level = 0;
        Set<String> seen = new HashSet<>();
        while (!queue.isEmpty()) {
            level++;
            for (int n = queue.size(); n > 0; n--) {
                String cur = queue.poll();
                for (int i = 0; i < 8; i++) {
                    String left = cur.substring(0, i), right = cur.substring(i + 1, 8);
                    for (String ch : chars) {
                        String tmp = left + ch + right;
                        if (set.contains(tmp) && !seen.contains(tmp)) {
                            seen.add(tmp);
                            if (tmp.equals(end)) {
                                return level;
                            } else {
                                queue.offer(tmp);
                            }
                        }
                    }
                }
            }
        }
        return -1;
    }
}
