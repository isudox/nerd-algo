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

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 3. Longest Substring Without Repeating Characters
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 *
 * Given a string, find the length of the longest substring without repeating
 * characters.
 *
 * Example 1:
 *
 * Input: "abcabcbb"
 * Output: 3
 * Explanation: The answer is "abc", with the length of 3.
 *
 * Example 2:
 *
 * Input: "bbbbb"
 * Output: 1
 * Explanation: The answer is "b", with the length of 1.
 *
 * Example 3:
 *
 * Input: "pwwkew"
 * Output: 3
 * Explanation: The answer is "wke", with the length of 3.
 *              Note that the answer must be a substring,
 *              "pwke" is a subsequence and not a substring.
 */
public class SubstringWithConcatenationOfAllWords {

    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        if (words.length == 0)
            return result;
        List<String> wordList = Arrays.asList(words);
        int len = words[0].length();
        int sLen = s.length();
        if (len > sLen)
            return result;
        int wordsLen = len * (words.length);
        int i = 0;
        while (i <= sLen - wordsLen) {
            String word = s.substring(i, i + len);
            if (wordList.contains(word)) {
                String substr = s.substring(i, i + wordsLen);
                if (isValid(substr, wordList, len))
                    result.add(i);
            }
            i++;
        }
        return result;
    }

    private boolean isValid(String str, List<String> wordList, int len) {
        List<String> list = new ArrayList<String>();
        for (int i = 0; i < str.length() / len; i++) {
            String s = str.substring(i * len, (i + 1) * len);
            list.add(s);
        }
        for (String s : wordList) {
            if (list.contains(s)) {
                list.remove(s);
            } else {
                return false;
            }
        }
        return true;
    }
}
