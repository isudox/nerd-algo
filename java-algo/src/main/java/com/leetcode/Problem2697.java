package com.leetcode;

public class Problem2697 {
    public String makeSmallestPalindrome(String s) {
        char[] arr = s.toCharArray();
        int i = 0, j = arr.length - 1;
        while (i < j) {
            if (arr[i] != arr[j]) {
                if (arr[i] < arr[j]) {
                    arr[j] = arr[i];
                } else {
                    arr[i] = arr[j];
                }
            }
            i++;
            j--;
        }
        return new String(arr);
    }
}
