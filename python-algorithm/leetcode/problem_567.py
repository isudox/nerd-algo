"""567. Permutation in String
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, write a function to return true if s2 contains
the permutation of s1. In other words, one of the first string's permutations
is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

Constraints:

    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].
"""
import copy


def check_inclusion(s1: str, s2: str) -> bool:
    len1, len2 = len(s1), len(s2),
    if len1 > len2:
        return False
    memo = dict()
    for ch in s1:
        memo[ch] = (memo[ch] if ch in memo else 0) + 1
    copy_memo = copy.deepcopy(memo)
    i = j = 0
    while j < len2:
        if s2[j] not in memo:
            i = j = j + 1
            memo = copy.deepcopy(copy_memo)
        elif memo[s2[j]] > 0:
            memo[s2[j]] -= 1
            j += 1
            if j - i == len1:
                return True
        else:
            while memo[s2[j]] == 0:
                memo[s2[i]] += 1
                i += 1
    return False


def check_inclusion_2(s1: str, s2: str) -> bool:
    len1, len2 = len(s1), len(s2),
    if len1 > len2:
        return False
    memo = [0] * 26
    for ch in s1:
        memo[ord(ch) - ord('a')] += 1
    i = j = 0
    while j < len2:
        pos = ord(s2[j]) - ord('a')
        memo[pos] -= 1
        j += 1
        while memo[pos] < 0:  # move the left pointer
            memo[ord(s2[i]) - ord('a')] += 1
            i += 1
        if j - i == len1:
            return True
    return False


def check_inclusion_3(s1: str, s2: str) -> bool:
    len1, len2 = len(s1), len(s2),
    if len1 > len2:
        return False
    store1, store2 = [0] * 26, [0] * 26
    for i in range(len1):
        store1[ord(s1[i]) - ord('a')] += 1
        store2[ord(s2[i]) - ord('a')] += 1
    if store1 == store2:
        return True
    for i in range(len1, len2):
        store2[ord(s2[i]) - ord('a')] += 1
        store2[ord(s2[i - len1]) - ord('a')] -= 1
        if store1 == store2:
            return True
    return False


def check_inclusion_4(s1: str, s2: str) -> bool:
    """
    optimize method 2
    """
    len1, len2 = len(s1), len(s2),
    if len1 > len2:
        return False
    diff = [0] * 26
    for i in range(len1):
        diff[ord(s1[i]) - ord('a')] -= 1
        diff[ord(s2[i]) - ord('a')] += 1
    diff_count = 0
    for cnt in diff:
        if cnt != 0:
            diff_count += 1
    if diff_count == 0:
        return True
    for i in range(len1, len2):
        if s2[i] != s2[i - len1]:
            if diff[ord(s2[i - len1]) - ord('a')] == 0:
                diff_count += 1
            diff[ord(s2[i - len1]) - ord('a')] -= 1
            if diff[ord(s2[i - len1]) - ord('a')] == 0:
                diff_count -= 1

            if diff[ord(s2[i]) - ord('a')] == 0:
                diff_count += 1
            diff[ord(s2[i]) - ord('a')] += 1
            if diff[ord(s2[i]) - ord('a')] == 0:
                diff_count -= 1
            if diff_count == 0:
                return True
    return False
