package main

import (
	"strconv"
	"strings"
)

// 165. Compare Version Numbers
// https://leetcode.com/problems/compare-version-numbers/

func compareVersion(version1 string, version2 string) int {
	compare := func(a, b string) int {
		inta, _ := strconv.ParseInt(a, 10, 64)
		intb, _ := strconv.ParseInt(b, 10, 64)
		if inta < intb {
			return -1
		} else if inta > intb {
			return 1
		}
		return 0
	}
	ver1 := strings.Split(version1, ".")
	ver2 := strings.Split(version2, ".")
	i := 0
	for i < len(ver1) && i < len(ver2) {
		if ret := compare(ver1[i], ver2[i]); ret != 0 {
			return ret
		}
		i++
	}
	if i < len(ver1) {
		for i < len(ver1) {
			if ret := compare(ver1[i], "0"); ret != 0 {
				return ret
			}
			i++
		}
	} else {
		for i < len(ver2) {
			if ret := compare("0", ver2[i]); ret != 0 {
				return ret
			}
			i++
		}
	}
	return 0
}
