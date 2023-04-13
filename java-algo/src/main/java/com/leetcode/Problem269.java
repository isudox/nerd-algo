package com.leetcode;

import java.util.*;

/**
 * 269. Alien Dictionary
 * https://leetcode.com/problems/alien-dictionary/
 */
public class Problem269 {
    private final Map<Character, List<Character>> graph = new HashMap<>();
    private final boolean[] visited = new boolean[26];
    private final boolean[] onPath = new boolean[26];
    private boolean hasCycle;
    private final StringBuilder path = new StringBuilder();

    public String alienOrder(String[] words) {
        Set<Character> characters = new HashSet<>();
        for (String word : words) {
            for (char ch : word.toCharArray()) {
                characters.add(ch);
            }
        }
        for (int i = 1; i < words.length; i++) {
            String w1 = words[i - 1], w2 = words[i];
            int size = Math.max(w1.length(), w2.length());
            for (int j = 0; j < size; j++) {
                if (j == w1.length()) {
                    break;
                }
                if (j == w2.length()) {
                    return "";
                }
                if (w1.charAt(j) != w2.charAt(j)) {
                    char s = w1.charAt(j), b = w2.charAt(j); // small, big
                    if (!graph.containsKey(s)) {
                        graph.put(s, new LinkedList<>());
                    }
                    graph.get(s).add(b);
                    break;
                }
            }
        }
        for (char ch : graph.keySet()) {
            dfs(ch);
            if (hasCycle) {
                return "";
            }
        }
        for (char ch : characters) {
            if (path.indexOf(String.valueOf(ch)) == -1) {
                path.append(ch);
            }
        }
        return path.reverse().toString();
    }

    private void dfs(char ch) {
        if (onPath[ch - 'a']) {
            hasCycle = true;
        }
        if (hasCycle || visited[ch - 'a']) {
            return;
        }
        visited[ch - 'a'] = true;
        onPath[ch - 'a'] = true;
        if (graph.containsKey(ch)) {
            for (char next : graph.get(ch)) {
                dfs(next);
            }
        }
        path.append(ch);
        onPath[ch - 'a'] = false;
    }
}
