package com.leetcode;

import java.util.*;

/**
 * 1202. Smallest String With Swaps
 * https://leetcode.com/problems/smallest-string-with-swaps/
 *
 * You are given a string s, and an array of pairs of indices in the string pairs
 * where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
 *
 * You can swap the characters at any pair of indices in the given pairs any number of times.
 *
 * Return the lexicographically smallest string that s can be changed to after using the swaps.
 *
 * Example 1:
 *
 * Input: s = "dcab", pairs = [[0,3],[1,2]]
 * Output: "bacd"
 * Explanation:
 * Swap s[0] and s[3], s = "bcad"
 * Swap s[1] and s[2], s = "bacd"
 *
 * Example 2:
 *
 * Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
 * Output: "abcd"
 * Explanation:
 * Swap s[0] and s[3], s = "bcad"
 * Swap s[0] and s[2], s = "acbd"
 * Swap s[1] and s[2], s = "abcd"
 *
 * Example 3:
 *
 * Input: s = "cba", pairs = [[0,1],[1,2]]
 * Output: "abc"
 * Explanation:
 * Swap s[0] and s[1], s = "bca"
 * Swap s[1] and s[2], s = "bac"
 * Swap s[0] and s[1], s = "abc"
 *
 * Constraints:
 *
 *     1 <= s.length <= 10^5
 *     0 <= pairs.length <= 10^5
 *     0 <= pairs[i][0], pairs[i][1] < s.length
 *     s only contains lower case English letters.
 */
public class Problem1202 {
    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        int size = s.length();
        UnionFind uf = new UnionFind(size);
        Map<Integer, PriorityQueue<Character>> graph = new HashMap<>();
        for (List<Integer> pair : pairs) {
            uf.union(pair.get(0), pair.get(1));
        }
        for (int i = 0; i < size; i++) {
            int root = uf.find(i);
            if (!graph.containsKey(root)) {
                graph.put(root, new PriorityQueue<>());
            }
            graph.get(root).add(s.charAt(i));
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < size; i++) {
            sb.append(graph.get(uf.find(i)).poll());
        }
        return sb.toString();
    }

    private static class UnionFind {
        private final int[] parent;

        public UnionFind(int size) {
            parent = new int[size];
            for (int i = 0; i < size; i++) {
                parent[i] = i;
            }
        }

        public int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        public void union(int a, int b) {
            parent[find(a)] = find(b);
        }
    }
}
