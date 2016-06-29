public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        if (strs.length == 1) return strs[0];
        int minLen = strs[0].length();
        for (String str : strs) {
            minLen = str.length() < minLen ? str.length() : minLen;
        }
        for (int i = 0; i < minLen; i++) {
            for (int j = 0; j < strs.length - 1; j++) {
                if (strs[j].charAt(i) != strs[j + 1].charAt(i)) {
                    return strs[j].substring(0, i);
                }
            }
        }
        return strs[0].substring(0, minLen);
    }
}