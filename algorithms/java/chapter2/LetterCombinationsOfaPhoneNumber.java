public class Solution {
    private static String[] keymap = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList<>();
        if (digits == null || digits.length() == 0) return res;
        this.combineLetters(digits, "", digits.length(), 0, res);
        return res;
    }

    private void combineLetters(String digits, String str, int len, int pos, List<String> list) {
        String key = keymap[digits.charAt(pos) - '2'];
        for (int i = 0; i < key.length(); i++) {
            if (pos == len - 1) list.add(str + key.charAt(i));
            else combineLetters(digits, str + key.charAt(i), len, pos + 1, list);
        }
    }
}