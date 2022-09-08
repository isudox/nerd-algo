package com.leetcode;

/**
 * 1598. Crawler Log Folder
 * https://leetcode.com/problems/crawler-log-folder/
 */
public class Problem1598 {
    public int minOperations(String[] logs) {
        int depth = 0;
        for (String log : logs) {
            if ("./".equals(log)) continue;
            if ("../".equals(log)) depth--;
            else depth++;
            if (depth < 0) depth = 0;
        }
        return depth;
    }
}
