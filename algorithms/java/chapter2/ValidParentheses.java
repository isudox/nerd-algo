public class Solution {
    public boolean isValid(String s) {
        char[] stack = new char[s.length()];
        int index = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{') {
                stack[index++] = s.charAt(i);
            } else if (s.charAt(i) == ')') {
                if (index == 0 || stack[--index] != '(') return false;
            } else if (s.charAt(i) == ']') {
                if (index == 0 || stack[--index] != '[') return false;
            } else {
                if (index == 0 || stack[--index] != '{') return false;
            }
        }
        return index == 0;
    }
}