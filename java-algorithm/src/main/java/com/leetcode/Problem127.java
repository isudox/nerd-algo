package com.leetcode;

import java.util.*;

/**
 * 127. Word Ladder
 * https://leetcode.com/problems/word-ladder/
 * <p>
 * Given two words (beginWord and endWord), and a dictionary's word list,
 * find the length of shortest transformation sequence from beginWord to endWord, such that:
 * <p>
 * Only one letter can be changed at a time.
 * Each transformed word must exist in the word list.
 * <p>
 * Note:
 * <p>
 * Return 0 if there is no such transformation sequence.
 * All words have the same length.
 * All words contain only lowercase alphabetic characters.
 * You may assume no duplicates in the word list.
 * You may assume beginWord and endWord are non-empty and are not the same.
 * <p>
 * Example 1:
 * <p>
 * Input:
 * beginWord = "hit",
 * endWord = "cog",
 * wordList = ["hot","dot","dog","lot","log","cog"]
 * <p>
 * Output: 5
 * <p>
 * Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
 * return its length 5.
 * <p>
 * Example 2:
 * <p>
 * Input:
 * beginWord = "hit"
 * endWord = "cog"
 * wordList = ["hot","dot","dog","lot","log"]
 * <p>
 * Output: 0
 * <p>
 * Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
 */
public class Problem127 {

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Map<String, Boolean> wordSet = new HashMap<>(wordList.size());
        for (String word : wordList)
            wordSet.put(word, true);
        if (wordSet.size() == 0 || !wordSet.containsKey(endWord)) return 0;
        List<String> queue = new ArrayList<>();
        queue.add(beginWord);
        int ans = 1;
        while (!queue.isEmpty()) {
            int n = queue.size();
            for (int i = 0; i < n; i++) {
                String word = queue.get(0);
                queue.remove(0);
                if (word.equals(endWord)) return ans;
                wordSet.remove(word);
                for (int j = 0; j < word.length(); j++) {
                    for (int k = 0; k < 26; k++) {
                        String newWord = word.substring(0, j) + (char) (97 + k) + word.substring(j + 1);
                        if (wordSet.containsKey(newWord)) {
                            queue.add(newWord);
                        }
                    }
                }
            }
            ans++;
        }
        return 0;
    }

    public static void main(String[] args) {
        Problem127 sol = new Problem127();
        // 5
        System.out.println(sol.ladderLength("hit", "cog", new ArrayList<>(Arrays.asList("hot", "dot", "dog", "lot", "log", "cog"))));
        System.out.println(sol.ladderLength("hit", "cog", new ArrayList<>(Arrays.asList("hot", "dog"))));
        System.out.println(sol.ladderLength("talk", "tail", new ArrayList<>(Arrays.asList("talk", "tons", "fall", "tail", "gale", "hall", "negs"))));

    }
}
