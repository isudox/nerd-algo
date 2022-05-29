package com.leetcode;

/**
 * 468. Validate IP Address
 * https://leetcode.com/problems/validate-ip-address/
 */
public class Problem468 {
    private String[] segments;

    public String validIPAddress(String queryIP) {
        if (queryIP.length() == 0 || queryIP.charAt(queryIP.length() - 1) == '.' || queryIP.charAt(queryIP.length() - 1) == ':') {
            return "Neither";
        }
        if (check(queryIP, "\\.", 4)) {
            return verify(false) ? "IPv4" : "Neither";
        } else if (check(queryIP, ":", 8)) {
            return verify(true) ? "IPv6" : "Neither";
        }
        return "Neither";
    }

    private boolean check(String ip, String split, int len) {
        segments = ip.split(split);
        return segments.length == len;
    }

    private boolean verify(boolean mode) {
        if (!mode) {
            for (String seg : segments) {
                if (seg.length() > 3) {
                    return false;
                }
                if (seg.length() > 1 && seg.charAt(0) == '0') {
                    return false;
                }
                try {
                    int num = Integer.parseInt(seg);
                    if (num < 0 || num > 255) {
                        return false;
                    }
                } catch (NumberFormatException e) {
                    return false;
                }
            }
            return true;
        }
        for (String seg : segments) {
            if (seg.length() < 1 || seg.length() > 4) {
                return false;
            }
            for (int i = 0; i < seg.length(); i++) {
                char ch = seg.charAt(i);
                int diff1 = ch - '0';
                int diff2 = ch - 'a';
                int diff3 = ch - 'A';
                if ((0 <= diff1 && diff1 < 10) || (0 <= diff2 && diff2 < 6) || (0 <= diff3 && diff3 < 6)) {
                    continue;
                }
                return false;
            }
        }
        return true;
    }
}
