package com.misc;

public class OneWayEdit {
    private String first;
    private String second;

    public boolean oneEditAway(String first, String second) {
        this.first = first;
        this.second = second;
        return first.equals(second) || helper(0, 0, 1);
    }

    private boolean helper(int i, int j, int k) {
        if (i == first.length() && j == second.length() && k >= 0) {
            return true;
        }
        if (Math.abs(second.length() - j - (first.length() - i)) > k) {
            return false;
        }
        while (i < first.length() && j < second.length()) {
            if (first.charAt(i) == second.charAt(j)) {
                i++;
                j++;
                continue;
            }
            if (k == 0) {
                return false;
            }
            // 1. add
            if (helper(i, j + 1, k - 1)) {
                return true;
            }
            // 2. replace
            if (helper(i + 1, j + 1, k - 1)) {
                return true;
            }
            // 3. delete
            if (helper(i + 1, j, k - 1)) {
                return true;
            }
            return false;
        }
        return Math.abs(first.length() - i - (second.length() - j)) <= k;
    }
}
