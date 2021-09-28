package leetcode

// 1328. Break a Palindrome
// https://leetcode.com/problems/break-a-palindrome/

func breakPalindrome(palindrome string) string {
	if len(palindrome) < 2 {
		return ""
	}
	for i, ch := range palindrome {
		if ch != 'a' {
			if len(palindrome)%2 == 1 && i == len(palindrome)/2 {
				continue
			}
			return palindrome[:i] + "a" + palindrome[i+1:]
		}
		if i == len(palindrome)-1 {
			return palindrome[:i] + "b"
		}
	}
	return ""
}
