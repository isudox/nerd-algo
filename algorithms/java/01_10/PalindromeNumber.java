// PalindromeNumber.java v1.0
public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        int y = 0;
        int bak = x;
        while (x > 0) {
            int temp = x;
            x = temp / 10;
            y = y * 10 + temp % 10;
        }
        if (y == bak) return true;
            
        return false;
    }
}