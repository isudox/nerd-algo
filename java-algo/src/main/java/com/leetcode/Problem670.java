package com.leetcode;

/**
 * 670. Maximum Swap
 * https://leetcode.com/problems/maximum-swap/
 */
public class Problem670 {
    public int maximumSwap(int num) {
        char[] charArray = String.valueOf(num).toCharArray();
        int n = charArray.length;
        int maxIdx = n - 1;
        int idx1 = -1, idx2 = -1;
        for (int i = n - 1; i >= 0; i--) {
            if (charArray[i] > charArray[maxIdx]) {
                maxIdx = i;
            } else if (charArray[i] < charArray[maxIdx]) {
                idx1 = i;
                idx2 = maxIdx;
            }
        }
        if (idx1 < 0) {
            return num;
        }
        char temp = charArray[idx1];
        charArray[idx1] = charArray[idx2];
        charArray[idx2] = temp;
        return Integer.parseInt(new String(charArray));
    }
}
