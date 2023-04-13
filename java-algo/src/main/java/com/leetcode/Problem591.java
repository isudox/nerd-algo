package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 591. Tag Validator
 * https://leetcode.com/problems/tag-validator/
 */
public class Problem591 {
    public boolean isValid(String code) {
        Deque<String> queue = new ArrayDeque<>();
        int n = code.length();
        int i = 0;
        while (i < n) {
            if (code.charAt(i) == '<') {
                if (i == n - 1) {
                    return false;
                }
                if (code.charAt(i + 1) == '/') {
                    int j = code.indexOf('>', i);
                    if (j < 0) {
                        return false;
                    }
                    String tagName = code.substring(i + 2, j);
                    if (queue.isEmpty() || !queue.peek().equals(tagName)) {
                        return false;
                    }
                    queue.pop();
                    i = j + 1;
                    if (queue.isEmpty() && i != n) {
                        return false;
                    }
                } else if (code.charAt(i + 1) == '!') {
                    if (queue.isEmpty()) {
                        return false;
                    }
                    if (i + 9 > n) {
                        return false;
                    }
                    String cdata = code.substring(i + 2, i + 9);
                    if (!"[CDATA[".equals(cdata)) {
                        return false;
                    }
                    int j = code.indexOf("]]>", i);
                    if (j < 0) {
                        return false;
                    }
                    i = j + 1;
                } else {
                    int j = code.indexOf('>', i);
                    if (j < 0) {
                        return false;
                    }
                    String tagName = code.substring(i + 1, j);
                    if (tagName.length() < 1 || tagName.length() > 9) {
                        return false;
                    }
                    for (int k = 0; k < tagName.length(); ++k) {
                        if (!Character.isUpperCase(tagName.charAt(k))) {
                            return false;
                        }
                    }
                    queue.push(tagName);
                    i = j + 1;
                }
            } else {
                if (queue.isEmpty()) {
                    return false;
                }
                ++i;
            }
        }
        return queue.isEmpty();
    }
}
