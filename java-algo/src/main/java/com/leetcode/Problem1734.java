package com.leetcode;

/**
 * 1734. Decode XORed Permutation
 * https://leetcode.com/problems/decode-xored-permutation/
 *
 * There is an integer array perm that is a permutation of the first n positive
 * integers, where n is always odd.
 *
 * It was encoded into another integer array encoded of length n - 1, such that
 * encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then
 * encoded = [2,1].
 *
 * Given the encoded array, return the original array perm. It is guaranteed
 * that the answer exists and is unique.
 *
 * Example 1:
 *
 * Input: encoded = [3,1]
 * Output: [1,2,3]
 * Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
 *
 * Example 2:
 *
 * Input: encoded = [6,5,4,6]
 * Output: [2,4,1,5,3]
 *
 * Constraints:
 *
 * 3 <= n < 10^5
 * n is odd.
 * encoded.length == n - 1
 */
public class Problem1734 {
    public int[] decode(int[] encoded) {
        int n = encoded.length + 1;
        int[] ans = new int[n];
        int total = 0;
        for (int i = 1; i <= n; i++) {
            total ^= i;
        }
        ans[0] = total;
        for (int i = 1; i < n - 1; i += 2) {
            ans[0] ^= encoded[i];
        }
        for (int i = 0; i < n - 1; i++) {
            ans[i + 1] = ans[i] ^ encoded[i];
        }
        return ans;
    }

    public int[] decode2(int[] encoded) {
        int n = encoded.length + 1;
        int[] ans = new int[n];
        ans[0] = n % 4 == 1 ? 1 : 0;
        for (int i = 1; i < n - 1; i += 2) {
            ans[0] ^= encoded[i];
        }
        for (int i = 0; i < n - 1; i++) {
            ans[i + 1] = ans[i] ^ encoded[i];
        }
        return ans;
    }
}
