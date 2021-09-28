package leetcode

import (
	"strconv"
	"strings"
	"testing"
)

func Test_929(t *testing.T) {
	type args struct {
		emails []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
	}
	// var dirs = []struct{ x, y int }{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := numUniqueEmails(tt.args.emails); got != tt.want {
				t.Errorf("numUniqueEmails() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestSample(t *testing.T) {
	for _, ch := range "abc" {
		println(strconv.QuoteRune(ch))
	}
	email := "abc@cdf.com"
	strs := strings.Split(email, "@")
	println(strs[0])
	println(strs[1])
}
