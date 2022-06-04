package com.leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * 929. Unique Email Addresses
 * https://leetcode.com/problems/unique-email-addresses/
 */
public class Problem929 {
    public int numUniqueEmails(String[] emails) {
        Set<String> set = new HashSet<>();
        for (String email : emails) {
            String ret = helper(email);
            set.add(ret);
        }
        return set.size();
    }

    private String helper(String email) {
        String[] segments = email.split("@");
        String local = segments[0], domain = segments[1];
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < local.length(); i++) {
            char ch = local.charAt(i);
            if (ch == '.') {
                continue;
            }
            if (ch == '+') {
                break;
            }
            sb.append(ch);
        }
        sb.append("@").append(domain);
        return sb.toString();
    }
}
