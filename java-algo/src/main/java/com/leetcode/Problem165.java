package com.leetcode;

/**
 * 165. Compare Version Numbers
 * https://leetcode.com/problems/compare-version-numbers/
 */
public class Problem165 {
    public int compareVersion(String version1, String version2) {
        String[] v1 = version1.split("\\.");
        String[] v2 = version2.split("\\.");
        int i = 0;
        while (i < v1.length && i < v2.length) {
            String n1 = v1[i];
            String n2 = v2[i];
            int ret = compare(n1, n2);
            if (ret != 0) {
                return ret;
            }
            i++;
        }
        String[] v3 = i < v1.length ? v1 : v2;
        int flag = i < v1.length ? 1 : -1;
        while (i < v3.length) {
            int ret = compare(v3[i], "0");
            if (ret != 0) {
                return ret * flag;
            }
            i++;
        }
        return 0;
    }

    private int compare(String n1, String n2) {
        long l1 = Long.parseLong(n1);
        long l2 = Long.parseLong(n2);
        return Long.compare(l1, l2);
    }

    public static void main(String[] args) {
        Problem165 p  = new Problem165();
        System.out.println(p.compareVersion("1", "1.1"));
    }
}
