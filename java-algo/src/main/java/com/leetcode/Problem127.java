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
        Set<String> wordSet = new HashSet<>(wordList);
        if (wordSet.size() == 0 || !wordSet.contains(endWord))
            return 0;
        // BFS
        Queue<String> queue = new LinkedList<>();
        queue.add(beginWord);
        int ans = 1;
        while (!queue.isEmpty()) {
            int n = queue.size();
            for (int i = 0; i < n; i++) {
                String word = queue.poll();
                if (endWord.equals(word))
                    return ans;
                wordSet.remove(word);
                for (int j = 0; j < word.length(); j++) {
                    for (char c = 'a'; c <= 'z'; c++) {
                        String newWord = word.substring(0, j) + c + word.substring(j + 1);
                        if (wordSet.contains(newWord)) {
                            queue.add(newWord);
                        }
                    }
                }
            }
            ans++;
        }
        return 0;
    }

    public int ladderLength2(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordSet = new HashSet<>(wordList);
        if (wordSet.size() == 0 || !wordSet.contains(endWord))
            return 0;
        int ans = 1;
        // Bi-BFS
        // be aware that use HashSet rather than Queue here.
        Set<String> beginSet = new HashSet<>();
        Set<String> endSet = new HashSet<>();
        beginSet.add(beginWord);
        endSet.add(endWord);
        while (!beginSet.isEmpty() && !endSet.isEmpty()) {
            // swap if needed to keep beginSet to be the little one.
            if (beginSet.size() > endSet.size()) {
                Set<String> temp = beginSet;
                beginSet = endSet;
                endSet = temp;
            }
            Set<String> nextBeginSet = new HashSet<>();
            for (String word : beginSet) {
                if (endSet.contains(word))
                    return ans;
                wordSet.remove(word);
                for (int j = 0; j < word.length(); j++) {
                    for (char c = 'a'; c <= 'z'; c++) {
                        String newWord = word.substring(0, j) + c + word.substring(j + 1);
                        if (wordSet.contains(newWord)) {
                            nextBeginSet.add(newWord);
                        }
                    }
                }
            }
            beginSet = nextBeginSet;
            ans++;
        }
        return 0;
    }
}
