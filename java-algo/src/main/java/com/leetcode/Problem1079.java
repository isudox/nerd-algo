package com.leetcode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * 1079. Letter Tile Possibilities
 * https://leetcode.com/problems/letter-tile-possibilities/
 */
public class Problem1079 {
    public int numTilePossibilities(String tiles) {
        Map<Character, Integer> counter = new HashMap<>();
        for (int i = 0; i < tiles.length(); i++) {
            counter.put(tiles.charAt(i), counter.getOrDefault(tiles.charAt(i), 0) + 1);
        }
        Set<Character> set = new HashSet<>(counter.keySet());
        return dfs(tiles.length(), counter, set) - 1;
    }

    private int dfs(int len, Map<Character, Integer> counter, Set<Character> chars) {
        if (len == 0) {
            return 1;
        }
        int ret = 1;
        for (char c : chars) {
            if (counter.get(c) > 0) {
                counter.put(c, counter.get(c) - 1);
                ret += dfs(len - 1, counter, chars);
                counter.put(c, counter.get(c) + 1);
            }
        }
        return ret;
    }
}
