public class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.equals(""))
            return 0;
        if (haystack.length() < needle.length())
            return -1;
        int i = 0, j = 0, start = 0;
        while (i < haystack.length() && j < needle.length()) {
            if (haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;
            } else {
                i = i - j + 1;
                j = 0;
            }
            if (j == needle.length())
                return i - j;
        }
        return -1;
    }
}
