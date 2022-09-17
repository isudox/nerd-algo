package com.leetcode;

import java.util.*;

/**
 * 336. Palindrome Pairs
 * https://leetcode.com/problems/palindrome-pairs/
 */
public class Problem336 {
    public List<List<Integer>> palindromePairs(String[] words) {
        List<List<Integer>> ans = new ArrayList<>();
        Trie trie = new Trie();
        for (int i = 0; i < words.length; i++) {
            add(trie, words[i], i);
        }
        for (int i = 0; i < words.length; i++) {
            search(trie, words, i, ans);
        }
        return ans;
    }

    private static class Trie {
        Trie[] children;
        int index;
        List<Integer> list;

        public Trie() {
            this.children = new Trie[26];
            this.index = -1;
            list = new ArrayList<>();
        }
    }

    private void add(Trie trie, String word, int index) {
        for (int i = word.length() - 1; i >= 0; i--) {
            int d = word.charAt(i) - 'a';
            if (trie.children[d] == null) {
                trie.children[d] = new Trie();
            }
            if (isPalindrome(word, 0, i)) {
                trie.list.add(index);
            }
            trie = trie.children[d];
        }
        trie.list.add(index);
        trie.index = index;
    }

    private void search(Trie trie, String[] words, int index, List<List<Integer>> store) {
        String word = words[index];
        for (int i = 0; i < word.length(); i++) {
            if (trie.index >= 0 && trie.index != index && isPalindrome(word, i, word.length() - 1)) {
                store.add(Arrays.asList(index, trie.index));
            }
            trie = trie.children[word.charAt(i) - 'a'];
            if (trie == null)
                return;
        }
        for (int i : trie.list) {
            if (i == index)
                continue;
            store.add(Arrays.asList(index, i));
        }
    }

    // TLE!
    public List<List<Integer>> palindromePairs2(String[] words) {
        Map<String, Integer> store = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            store.put(words[i], i);
        }
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            // case1: "aba" + ""
            if (words[i].length() > 0 && isPalindrome(words[i], 0, words.length - 1) && store.containsKey("")) {
                ans.add(Arrays.asList(i, store.get("")));
                ans.add(Arrays.asList(store.get(""), i));
            }
            // case2: "ab" + "ba"
            String rev = reverse(words[i]);
            if (!rev.equals(words[i]) && store.containsKey(rev)) {
                ans.add(Arrays.asList(i, store.get(rev)));
            }
            for (int j = 1; j < words[i].length(); j++) {
                String pref = words[i].substring(0, j);
                String suff = words[i].substring(j);
                String prefRev = reverse(pref);
                String suffRev = reverse(suff);
                // case3: "abacd" + "dc"
                if (isPalindrome(pref, 0, pref.length() - 1) && store.containsKey(suffRev)) {
                    ans.add(Arrays.asList(store.get(suffRev), i));
                }
                // case4: "cdaba" + "dc"
                if (isPalindrome(suff, 0, suff.length() - 1) && store.containsKey(prefRev)) {
                    ans.add(Arrays.asList(i, store.get(prefRev)));
                }
            }

        }
        return ans;
    }

    private boolean isPalindrome(String word, int l, int r) {
        while (l < r) {
            if (word.charAt(l++) != word.charAt(r--))
                return false;
        }
        return true;
    }

    private String reverse(String word) {
        StringBuilder sb = new StringBuilder();
        for (int i = word.length() - 1; i >= 0; i--) {
            sb.append(word.charAt(i));
        }
        return sb.toString();
    }
}
