public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLen = 0;
        int sLen = s.length();
        if (sLen == 0) {
            return 0;
        }
        
        for (int i = 0; i < sLen; i++) {
            int curLen = 0;
            Map<String, Integer> map = new HashMap<String, Integer>();
            for (int j = i; j < sLen; j++) {
                String key = String.valueOf(s.charAt(j));
                if (map.get(key) == null) {
                    map.put(key, 1);
                    curLen += 1;
                    maxLen = curLen > maxLen ? curLen : maxLen;
                } else {
                    curLen = 0;
                    break;
                }
            }
        }
        return maxLen;
    }
}