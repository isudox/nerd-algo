package com.leetcode;

import java.util.*;

/**
 * 763. Partition Labels
 * https://leetcode.com/problems/partition-labels/
 */
public class Problem763 {
    public List<Integer> partitionLabels(String s) {
        int n = s.length();
        Map<Character, Integer> first = new HashMap<>();
        Map<Character, Integer> last = new HashMap<>();
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            if (!first.containsKey(ch)) {
                first.put(ch, i);
            }
        }
        for (int i = n - 1; i >= 0; i--) {
            char ch = s.charAt(i);
            if (!last.containsKey(ch)) {
                last.put(ch, i);
            }
        }
        List<int[]> segments = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            char ch = (char) ('a' + i);
            if (first.containsKey(ch)) {
                int[] ints = new int[]{first.get(ch), last.get(ch)};
                segments.add(ints);
            }
        }
        segments.sort((o1, o2) -> o1[0] - o2[0]);
        List<int[]> merged = merge(segments);
        List<Integer> ans = new ArrayList<>();
        for (int[] m : merged) {
            ans.add(m[1] - m[0] + 1);
        }
        return ans;
    }

    private List<int[]> merge(List<int[]> segments) {
        List<int[]> result = new ArrayList<>();
        result.add(segments.get(0));
        for (int i = 1; i < segments.size(); i++) {
            if (segments.get(i)[0] < result.get(result.size() - 1)[1]) {
                result.get(result.size() - 1)[1] = Math.max(segments.get(i)[1], result.get(result.size() - 1)[1]);
            } else {
                result.add(segments.get(i));
            }
        }
        return result;
    }
}
