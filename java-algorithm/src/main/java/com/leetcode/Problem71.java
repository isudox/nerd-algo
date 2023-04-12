package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 71. Simplify Path
 * https://leetcode.com/problems/simplify-path/
 */
public class Problem71 {
    public String simplifyPath(String path) {
        String[] splits = path.split("/");
        Deque<String> queue = new ArrayDeque<>();
        for (String split : splits) {
            if (split.equals("") || split.equals("."))
                continue;
            if (split.equals("..")) {
                if (!queue.isEmpty()) {
                    queue.removeLast();
                }
            } else {
                queue.offer(split);
            }
        }
        return "/" + String.join("/", queue);
    }
}
