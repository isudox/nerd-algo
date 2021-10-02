package leetcode

import (
	"reflect"
	"testing"
)

func Test_calculateMinimumHP(t *testing.T) {
	tests := []struct {
		dungeon [][]int
		want    int
	}{
		{[][]int{{-2, -3, 3}, {-5, -10, 1}, {10, 30, -5}}, 7},
		//{[][]int{{0}}, 1},
	}
	for _, tt := range tests {
		t.Run("174. Dungeon Game", func(t *testing.T) {
			if got := calculateMinimumHP(tt.dungeon); got != tt.want {
				t.Errorf("calculateMinimumHP() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_223(t *testing.T) {
	tests := []struct {
		ax1  int
		ay1  int
		ax2  int
		ay2  int
		bx1  int
		by1  int
		bx2  int
		by2  int
		want int
	}{
		{-3, 0, 3, 4, 0, -1, 9, 2, 45},
		{-2, -2, 2, 2, -2, -2, 2, 2, 16},
	}
	for _, tt := range tests {
		t.Run("223. Rectangle Area", func(t *testing.T) {
			if got := computeArea(tt.ax1, tt.ay1, tt.ax2, tt.ay2, tt.bx1, tt.by1, tt.bx2, tt.by2); got != tt.want {
				t.Errorf("computeArea() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_405(t *testing.T) {
	tests := []struct {
		num int
		ans string
	}{
		{26, "1a"},
		{0, "0"},
		{-1, "ffffffff"},
	}
	for _, tt := range tests {
		t.Run("405. Convert a Number to Hexadecimal", func(t *testing.T) {
			if got := toHex(tt.num); got != tt.ans {
				t.Errorf("toHex() = %v, want %v", got, tt.ans)
			}
		})
	}
}

func Test_698(t *testing.T) {
	type args struct {
		nums []int
		k    int
	}
	tests := []struct {
		args args
		want bool
	}{
		{args{[]int{4, 3, 2, 3, 5, 2, 1}, 4}, true},
		{args{[]int{1, 2, 3, 4}, 3}, false},
		{args{[]int{12, 1, 2, 3, 18, 2, 5, 2, 11, 1}, 3}, true},
	}
	for _, tt := range tests {
		t.Run("698. Partition to K Equal Sum Subsets", func(t *testing.T) {
			if got := canPartitionKSubsets(tt.args.nums, tt.args.k); got != tt.want {
				t.Errorf("canPartitionKSubsets() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_922(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		args args
		want []int
	}{
		{args{[]int{4, 2, 5, 7}}, []int{4, 5, 2, 7}},
		{args{[]int{2, 3}}, []int{2, 3}},
	}
	for _, tt := range tests {
		t.Run("922. Sort Array By Parity II", func(t *testing.T) {
			if got := sortArrayByParityII(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("sortArrayByParityII() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_929(t *testing.T) {
	tests := []struct {
		emails []string
		want   int
	}{
		{[]string{"test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"}, 2},
		{[]string{"a@leetcode.com", "b@leetcode.com", "c@leetcode.com"}, 3},
	}
	for _, tt := range tests {
		t.Run("929. Unique Email Addresses", func(t *testing.T) {
			if got := numUniqueEmails(tt.emails); got != tt.want {
				t.Errorf("numUniqueEmails() = %v, want %v", got, tt.want)
			}
		})
	}
}
