package com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class Problem767 {
    public String reorganizeString(String s) {
        Map<Character, Integer> store = new HashMap<>(26);
        int size = s.length();
        for (int i = 0; i < size; i++) {
            store.put(s.charAt(i), store.getOrDefault(s.charAt(i), 0) + 1);
        }
        return greed(store, size);
    }

    private String greed(Map<Character, Integer> store, int size) {
        StringBuilder ans = new StringBuilder();
        int cnt = 0;
        while (cnt < size) {
            StringBuilder cur = new StringBuilder();
            for (Character k : store.keySet()) {
                if (store.get(k) > 0) {
                    store.put(k, store.get(k) - 1);
                    cur.append(k);
                    cnt += 1;
                }
            }
            if (ans.toString().equals("") || ans.charAt(ans.length() - 1) != cur.charAt(0))
                ans.append(cur);
            else if (ans.charAt(0) != cur.charAt(cur.length() - 1))
                ans.insert(0, cur);
            else {
                boolean flag = false;
                for (int i = 1; i < ans.length(); i++) {
                    if (ans.charAt(i) != cur.charAt(0) && ans.charAt(i - 1) != cur.charAt(0)) {
                        ans = new StringBuilder(ans.substring(0, i) + cur.charAt(0) + ans.substring(i));
                        flag = true;
                        break;
                    }
                }
                if (!flag)
                    return "";
                ans.append(cur.substring(1));
            }
        }
        return ans.toString();
    }
}
