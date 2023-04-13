package main

import (
	"strconv"
	"strings"
)

// 929. Unique Email Addresses
// https://leetcode.com/problems/unique-email-addresses/
func numUniqueEmails(emails []string) int {
	ans := 0
	dict := make(map[string]bool)
	for _, email := range emails {
		parsedEmail := parse(email)
		if dict[parsedEmail] == false {
			dict[parsedEmail] = true
			ans++
		}
	}
	return ans
}

func parse(email string) string {
	stringList := strings.Split(email, "@")
	local, host := stringList[0], stringList[1]
	ret := ""
	for _, ch := range local {
		if ch == '.' {
			continue
		}
		if ch == '+' {
			break
		}
		ret += strconv.QuoteRune(ch)
	}
	return ret + "@" + host
}
