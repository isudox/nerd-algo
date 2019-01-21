/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2017-2019 sudoz
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 *
 */

/**
 * 9. Palindrome Number
 * https://leetcode.com/problems/palindrome-number/
 *
 * Determine whether an integer is a palindrome. An integer is a palindrome
 * when it reads the same backward as forward.
 *
 * Example 1:
 *
 * Input: 121
 * Output: true
 * Example 2:
 *
 * Input: -121
 * Output: false
 * Explanation: From left to right, it reads -121. From right to left,
 * it becomes 121-. Therefore it is not a palindrome.
 * Example 3:
 *
 * Input: 10
 * Output: false
 * Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 * Follow up:
 *
 * Could you solve it without converting the integer to a string?
 */
public class PalindromeNumber {
    public boolean isPalindrome1(int x) {
        if (x < 0) return false;
        int y = 0;
        int bak = x;
        while (x > 0) {
            int temp = x;
            x = temp / 10;
            y = y * 10 + temp % 10;
        }
        if (y == bak) return true;

        return false;
    }

    public boolean isPalindrome2(int x) {
        if (x < 0) return false;
        if (x == 0) return true;
        int count = 0;
        int temp = x;
        while (temp > 0) {
            temp /= 10;
            count++;
        }
        for (int i = count; i > 0; i -= 2) {
            if (x / this.pow(10, i - 1) != x % 10) return false;
            x = (x % this.pow(10, i - 1)) / 10;
        }
        return true;
    }

    private int pow(int x, int y) {
        int z = 1;
        for (; y > 0; y--) z *= x;
        return z;
    }

    public boolean isPalindrome3(int x) {
        if (x < 0) return false;
        int digits = 0;
        int temp = x;
        while (temp > 0) {
            temp /= 10;
            digits++;
        }
        int j = digits;
        for (int i = 1; j > i; i++, j--) {
            if (digit(x, digits, j) != digit(x, digits, i)) return false;
        }
        return true;
    }

    private int digit(int x, int i, int j) {
        return x / pow(10, j - 1) % 10;
    }
}