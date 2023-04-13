package com.leetcode;

import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

/**
 * 854. K-Similar Strings
 * https://leetcode.com/problems/k-similar-strings/
 */
class Problem854 {
    public int kSimilarity(String s1, String s2) {
        int n = s1.length();
        Queue<String> q1 = new ArrayDeque<>();
        Queue<Integer> q2 = new ArrayDeque<>();
        q1.offer(s1);
        q2.offer(0);
        Set<String> seen = new HashSet<>();
        int ans = 0;
        while (!q1.isEmpty()) {
            int size = q1.size();
            for (int i = 0; i < size; i++) {
                String s = q1.poll();
                int x = q2.poll();
                if (s2.equals(s)) {
                    return ans;
                }
                while (x < n && s.charAt(x) == s2.charAt(x)) {
                    x++;
                }
                for (int j = x + 1; j < n; j++) {
                    if (s2.charAt(j) == s.charAt(j)) {
                        continue;
                    }
                    if (s2.charAt(x) == s.charAt(j)) {
                        String next = swap(s, x, j);
                        if (!seen.contains(next)) {
                            seen.add(next);
                            q1.offer(next);
                            q2.offer(x + 1);
                        }
                    }
                }
            }
            ans++;
        }
        return ans;
    }

    private String swap(String s, int i, int j) {
        char[] arr = s.toCharArray();
        char tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
        return new String(arr);
    }
}
