package com.leetcode;

import java.util.*;

/**
 * 126. Word Ladder II
 * https://leetcode.com/problems/word-ladder-ii/
 *
 * Given two words (beginWord and endWord), and a dictionary's word list,
 * find `all shortest` transformation sequence(s) from beginWord to endWord,
 * such that:
 *
 *     Only one letter can be changed at a time
 *     Each transformed word must exist in the word list.
 *     Note that beginWord is not a transformed word.
 *
 * Note:
 *
 *     Return an empty list if there is no such transformation sequence.
 *     All words have the same length.
 *     All words contain only lowercase alphabetic characters.
 *     You may assume no duplicates in the word list.
 *     You may assume beginWord and endWord are non-empty and are not the same.
 *
 * Example 1:
 *
 * Input:
 * beginWord = "hit",
 * endWord = "cog",
 * wordList = ["hot","dot","dog","lot","log","cog"]
 *
 * Output:
 * [
 *   ["hit","hot","dot","dog","cog"],
 *   ["hit","hot","lot","log","cog"]
 * ]
 *
 * Example 2:
 *
 * Input:
 * beginWord = "hit"
 * endWord = "cog"
 * wordList = ["hot","dot","dog","lot","log"]
 *
 * Output: []
 *
 * Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
 */
public class Problem126 {
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        List<List<String>> ans = new ArrayList<>();
        Map<String, Set<String>> nextWordMap = new HashMap<>();
        int count = getSteps(beginWord, endWord, wordList, nextWordMap);
        if (count == 0)
            return ans;
        List<String> candidate = new ArrayList<>();
        candidate.add(beginWord);
        Set<String> wordSet = new HashSet<>(wordList);
        wordSet.remove(beginWord);
        dfs(ans, candidate, wordSet, nextWordMap, count, endWord);
        return ans;
    }

    private void dfs(List<List<String>> ans, List<String> candidate, Set<String> wordSet, Map<String, Set<String>> nextWordMap, int count, String endWord) {
        if (candidate.size() > count) return;
        String word = candidate.get(candidate.size() - 1);
        if (!nextWordMap.containsKey(word)) return;
        for (String nextWord : nextWordMap.get(word)) {
            if (wordSet.contains(nextWord)) {
                candidate.add(nextWord);
                wordSet.remove(nextWord);
                if (candidate.size() == count) {
                    if (nextWord.equals(endWord))
                        ans.add(new ArrayList<>(candidate));
                } else if (candidate.size() < count) {
                    dfs(ans, candidate, wordSet, nextWordMap, count, endWord);
                }
                candidate.remove(nextWord);
                wordSet.add(nextWord);
            }
        }
    }

    public int getSteps(String beginWord, String endWord, List<String> wordList, Map<String, Set<String>> nextWordMap) {
        Set<String> wordSet = new HashSet<>(wordList);
        if (wordSet.size() == 0 || !wordSet.contains(endWord))
            return 0;
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
                        String nextWord = word.substring(0, j) + c + word.substring(j + 1);
                        if (wordSet.contains(nextWord)) {
                            Set<String> nextWords = nextWordMap.getOrDefault(word, new HashSet<>());
                            nextWords.add(nextWord);
                            nextWordMap.put(word, nextWords);
                            queue.add(nextWord);
                        }
                    }
                }
            }
            ans++;
        }
        return 0;
    }
}
