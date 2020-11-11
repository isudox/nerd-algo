package com.leetcode;

import java.util.*;

/**
 * 514. Freedom Trail
 * https://leetcode.com/problems/freedom-trail/
 *
 * Input: ring = "godding", key = "gd"
 * Output: 4
 * Explanation:
 * For the first key character 'g', since it is already in place, we just need 1 step to spell this character.
 * For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
 * Also, we need 1 more step for spelling.
 * So the final output is 4.
 *
 * Note:
 *
 *     Length of both ring and key will be in range 1 to 100.
 *     There are only lowercase letters in both strings and might be some duplicate characters in both strings.
 *     It's guaranteed that string key could always be spelled by rotating the string ring.
 */
public class Problem514 {

    public int findRotateSteps(String ring, String key) {
        int keyLen = key.length(), ringLen = ring.length();
        Map<Character, List<Integer>> charPos = new HashMap<>();
        for (int i = 0; i < ringLen; i++) {
            char c = ring.charAt(i);
            if (charPos.containsKey(c))
                charPos.get(c).add(i);
            else
                charPos.put(c, new ArrayList<>(Arrays.asList(i)));
        }
        int[][] memo = new int[ringLen][keyLen];
        for (int i = 0; i < ringLen; i++) {
            for (int j = 0; j < keyLen; j++) {
                memo[i][j] = 0;
            }
        }
        return dfs(key, ring,0, 0, memo, charPos);
    }

    private int dfs(String key, String ring, int keyIdx, int ringIdx, int[][] memo, Map<Character, List<Integer>> charPos) {
        if (memo[ringIdx][keyIdx] != 0)
            return memo[ringIdx][keyIdx];
        int result = Integer.MAX_VALUE;
        char c = key.charAt(keyIdx);
        List<Integer> positions = charPos.get(c);
        for (int pos : positions) {
            int curSteps = 1 + minDiff(pos, ringIdx, ring.length());
            if (keyIdx == key.length() - 1) {
                result = Math.min(result, curSteps);
                continue;
            }
            int nextSteps = dfs(key, ring, keyIdx + 1, pos, memo, charPos);
            result = Math.min(result, curSteps + nextSteps);
        }
        memo[ringIdx][keyIdx] = result;
        return result;
    }

    private int minDiff(int x, int y, int n) {
        int abs = Math.abs(x - y);
        return Math.min(abs, n - abs);
    }
}
