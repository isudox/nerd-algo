public class Solution {
    public String longestPalindrome(String s) {
        int len = s.length();
        if (len <= 1) {
            return s;
        }
        int maxLen = 0;
        String palindrome = "";

        for (int i = 0; i < len - 1; i++) {
            // odd
            String oddStr = check(s, i, i, len);
            int oddLen = oddStr.length();
            if (oddLen > maxLen) {
                maxLen = oddLen;
                palindrome = oddStr;
            }
            // even
            String evenStr = check(s, i, i + 1, len);
            int evenLen = evenStr.length();
            if (evenLen > maxLen) {
                maxLen = evenLen;
                palindrome = evenStr;
            }
        }

        return palindrome;
    }

    private String check(String s, int start, int end, int len) {
        while (start >= 0  &&  end <= len - 1 && s.charAt(start) == s.charAt(end)) {
            start--;
            end++;
        }
        return s.substring(start + 1, end);
    }
}