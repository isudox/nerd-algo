package leetcode

import (
	"reflect"
	"testing"
)

func Test_55(t *testing.T) {
	tests := []struct {
		nums []int
		want bool
	}{
		{[]int{2, 0}, true},
		{[]int{2, 3, 1, 1, 4}, true},
		{[]int{3, 2, 1, 0, 4}, false},
	}
	for _, tt := range tests {
		t.Run("55. Jump Game", func(t *testing.T) {
			if got := canJump(tt.nums); got != tt.want {
				t.Errorf("canJump() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_79(t *testing.T) {
	tests := []struct {
		board [][]byte
		word  string
		ans   bool
	}{
		{[][]byte{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}}, "ABCCED", true},
		{[][]byte{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}}, "SEE", true},
		{[][]byte{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}}, "ABCB", false},
		{[][]byte{{'A'}}, "A", true},
	}
	for _, tt := range tests {
		t.Run("79. Word Search", func(t *testing.T) {
			if got := exist(tt.board, tt.word); got != tt.ans {
				t.Errorf("exist() = %v, want %v", got, tt.ans)
			}
		})
	}
}

func Test_166(t *testing.T) {
	tests := []struct {
		numerator   int
		denominator int
		ans         string
	}{
		{1, 2, "0.5"},
		{2, 1, "2"},
		{3, 2, "1.5"},
		{2, 3, "0.(6)"},
		{1, 6, "0.1(6)"},
		{4, 333, "0.(012)"},
		{-50, 8, "-6.25"},
	}
	for _, tt := range tests {
		t.Run("166. Fraction to Recurring Decimal", func(t *testing.T) {
			if got := fractionToDecimal(tt.numerator, tt.denominator); got != tt.ans {
				t.Errorf("fractionToDecimal() = %v, want %v", got, tt.ans)
			}
		})
	}
}
func Test_174(t *testing.T) {
	tests := []struct {
		dungeon [][]int
		want    int
	}{
		{[][]int{{-2, -3, 3}, {-5, -10, 1}, {10, 30, -5}}, 7},
		{[][]int{{0}}, 1},
	}
	for _, tt := range tests {
		t.Run("174. Dungeon Game", func(t *testing.T) {
			if got := calculateMinimumHP(tt.dungeon); got != tt.want {
				t.Errorf("calculateMinimumHP() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_187(t *testing.T) {
	tests := []struct {
		s   string
		ans []string
	}{
		{"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", []string{"AAAAACCCCC", "CCCCCAAAAA"}},
		{"AAAAAAAAAAAAA", []string{"AAAAAAAAAA"}},
		{"AAAAAAAAA", []string{}},
	}
	for _, tt := range tests {
		t.Run("187. Repeated DNA Sequences", func(t *testing.T) {
			if got := findRepeatedDnaSequences(tt.s); !reflect.DeepEqual(got, tt.ans) {
				t.Errorf("findRepeatedDnaSequences() = %v, want %v", got, tt.ans)
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

func Test_273(t *testing.T) {
	tests := []struct {
		num int
		ans string
	}{
		{2147483647, "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"},
		{1000000, "One Million"},
	}
	for _, tt := range tests {
		t.Run("273. Integer to English Words", func(t *testing.T) {
			if got := numberToWords(tt.num); got != tt.ans {
				t.Errorf("numberToWords = %v, want %v", got, tt.ans)
			}
		})
	}
}
func Test_352(t *testing.T) {
	t.Run("352. Data Stream as Disjoint Intervals", func(t *testing.T) {
		r := SummaryRanges{}
		r.AddNum(1)
		r.AddNum(9)
		r.AddNum(2)
		t.Log(r.GetIntervals())
	})
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

func Test_414(t *testing.T) {
	tests := []struct {
		nums []int
		ans  int
	}{
		{[]int{5, 2, 2}, 5},
		//{[]int{1,2,-2147483648}, -2147483648},
	}
	for _, tt := range tests {
		t.Run("414. Third Maximum Number", func(t *testing.T) {
			if got := thirdMax(tt.nums); got != tt.ans {
				t.Errorf("thirdMax() = %v, want %v", got, tt.ans)
			}
		})
	}
}

func Test_434(t *testing.T) {
	tests := []struct {
		s   string
		ans int
	}{
		{"Hello, my name is John", 5},
	}
	for _, tt := range tests {
		t.Run("434. Number of Segments in a String", func(t *testing.T) {
			if got := countSegments(tt.s); got != tt.ans {
				t.Errorf("countSegments() = %v, want %v", got, tt.ans)
			}
		})
	}
}

func Test_441(t *testing.T) {
	tests := []struct {
		n   int
		ans int
	}{
		{5, 2},
		{6, 3},
		{8, 3},
	}
	for _, tt := range tests {
		t.Run("441. Arranging Coins", func(t *testing.T) {
			if got := arrangeCoins(tt.n); got != tt.ans {
				t.Errorf("got = %v, want = %v", got, tt.ans)
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
