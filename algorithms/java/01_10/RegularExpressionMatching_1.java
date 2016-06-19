// RegularExpressionMatching.java v1.0
public class Solution {
    public boolean isMatch(String s, String p) {
        return java.util.regex.Pattern.compile(p).matcher(s).matches();
    }
}       