package main

import (
	"strings"
)

// 71. Simplify Path
// https://leetcode.com/problems/simplify-path/

func simplifyPath(path string) string {
	stack := make([]string, 0)
	segments := strings.Split(path, "/")
	for _, seg := range segments {
		if seg == "" || seg == "." {
			continue
		}
		if seg == ".." {
			if len(stack) > 0 {
				stack = stack[:len(stack)-1]
			}
		} else {
			stack = append(stack, seg)
		}
	}
	return "/" + strings.Join(stack, "/")
}
