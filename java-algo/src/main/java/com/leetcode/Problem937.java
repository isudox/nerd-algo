package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 937. Reorder Data in Log Files
 * https://leetcode.com/problems/reorder-data-in-log-files/
 */
public class Problem937 {
    public String[] reorderLogFiles(String[] logs) {
        int n = logs.length;
        String[] ans = new String[n];
        List<Combine> letLogs = new ArrayList<>();
        List<String> digLogs = new ArrayList<>();
        for (String log : logs) {
            String[] splits = log.split(" ");
            if (isDigLog(splits)) {
                digLogs.add(log);
            } else {
                letLogs.add(new Combine(splits[0], log.substring(splits[0].length())));
            }
        }
        letLogs.sort((o1, o2) -> {
            if (o1.log.equals(o2.log)) {
                return o1.pref.compareTo(o2.pref);
            }
            return o1.log.compareTo(o2.log);
        });
        for (int i = 0; i < n; i++) {
            if (i < letLogs.size()) {
                ans[i] = letLogs.get(i).pref + letLogs.get(i).log;
            } else {
                ans[i] = digLogs.get(i - letLogs.size());
            }
        }
        return ans;
    }

    private static class Combine {
        String pref;
        String log;

        public Combine(String pref, String log) {
            this.pref = pref;
            this.log = log;
        }
    }

    private boolean isDigLog(String[] splits) {
        for (int i = 1; i < splits.length; i++) {
            for (char ch : splits[i].toCharArray()) {
                if (ch - 'a' >= 0 && 'z' - ch >= 0) {
                    return false;
                }
            }
        }
        return true;
    }
}
