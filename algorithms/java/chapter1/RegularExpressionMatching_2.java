// RegularExpressionMatching.java v1.1
public class Solution {
    public boolean isMatch(String s, String p) {
        int lenS = s.length(), lenP = p.length();
        if (lenP == 0) return lenS == 0;
        if (lenP == 1) {
            if (p.charAt(0) == '.') return lenS == 1;
            return lenS == 1 && s.charAt(0) == p.charAt(0);
        }
        if (p.charAt(1) == '*') {
            if (isMatch(s, p.substring(2))) return true;
            if(s.length() > 0 && (p.charAt(0) == '.' || s.charAt(0) == p.charAt(0))) {
                return isMatch(s.substring(1), p);
            }
            return false;
        } else {
            if(lenS > 0 && (p.charAt(0) == '.' || s.charAt(0) == p.charAt(0))) {
                return isMatch(s.substring(1), p.substring(1));
            }
            return false;
        }
    }
}    