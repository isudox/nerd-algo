public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> list = new ArrayList<>();
        if (n <= 0) return list;
        recursive(list, "", n, n);
        return list;
    }
    private void recursive(List<String> result, String paren, int left, int right) {
        if (left == 0 && right == 0) {
            result.add(paren);
            return;
        }
        if (left > 0) {
            recursive(result, paren + "(", left - 1, right);
        }
        if (right > 0 && left < right) {
            recursive(result, paren + ")", left, right - 1);
        }
    }
}