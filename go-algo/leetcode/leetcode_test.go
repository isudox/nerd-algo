package main

import (
	"encoding/json"
	"fmt"
	"reflect"
	"strconv"
	"testing"
	"time"
)

type ABC struct {
	Num  int       `json:"num,omitempty"`
	Time time.Time `json:"time,omitempty"`
}

func TestMisc(t *testing.T) {
	datas := map[string]int{
		"2": 1,
		"1": 2,
	}
	n := 10000
	cnt0, cnt1 := 0, 0
	for i := 0; i < n; i++ {
		var num = 0
		for _, d := range datas {
			num = num*10 + d
		}
		if num == 12 {
			cnt0++
		} else {
			cnt1++
		}
	}
	fmt.Printf("12: %d\n21: %d\n", cnt0, cnt1)
	ts := time.Now()
	fmt.Printf("time:%d\n", ts.Unix())
	abc := ABC{
		Num:  1,
		Time: ts,
	}
	bs, _ := json.Marshal(abc)
	fmt.Printf("json: %s\n", string(bs))
	cba := ABC{}
	_ = json.Unmarshal(bs, &cba)
	fmt.Printf("time:%d", cba.Time.Unix())
}

func Test_29(t *testing.T) {
	tests := []struct {
		dividend int
		divisor  int
		ans      int
	}{
		{10, 3, 3},
		{0, 1, 0},
		{1, 1, 1},
		{7, -3, -2},
		{-2147483648, -1, 2147483647},
		{-2147483648, 1, -2147483648},
	}
	for _, tt := range tests {
		t.Run("29. Divide Two Integers", func(t *testing.T) {
			if got := divide(tt.dividend, tt.divisor); got != tt.ans {
				t.Errorf("divide() got %v, want %v", got, tt.ans)
			}
		})
	}
}

func Test_38(t *testing.T) {
	tests := []struct {
		n   int
		ans string
	}{
		{1, "1"},
		{2, "11"},
		{3, "21"},
		{4, "1211"},
		{5, "111221"},
	}
	for _, tt := range tests {
		t.Run("38. Count and Say", func(t *testing.T) {
			if got := countAndSay(tt.n); got != tt.ans {
				t.Errorf("countAndSay() got %v, want %v", got, tt.ans)
			}
		})
	}
}

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
				t.Errorf("canJump() got %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_66(t *testing.T) {
	tests := []struct {
		digits []int
		ans    []int
	}{
		{[]int{9}, []int{1, 0}},
		{[]int{9, 9}, []int{1, 0, 0}},
		{[]int{9, 9, 9}, []int{1, 0, 0, 0}},
	}
	for _, tt := range tests {
		t.Run("66. Plus One", func(t *testing.T) {
			if got := plusOne(tt.digits); !reflect.DeepEqual(got, tt.ans) {
				t.Errorf("plusOne got %+v, want %+v", got, tt.ans)
			}
		})
	}
}

func Test_75(t *testing.T) {
	sortColors([]int{1, 2, 0})
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
				t.Errorf("exist() got %v, want %v", got, tt.ans)
			}
		})
	}
}

func Test_155(t *testing.T) {
	minStack := MinStack{}
	minStack.Push(-2)
	minStack.Push(0)
	minStack.Push(-1)
	println("getMin = ", minStack.GetMin())
	println("top = ", minStack.Top())
	minStack.Pop()
	println("getMin = ", minStack.GetMin())
}

func Test_123(t *testing.T) {
	tests := []struct {
		prices []int
		ans    int
	}{
		{[]int{3, 3, 5, 0, 0, 3, 1, 4}, 6},
		{[]int{1, 2, 3, 4, 5}, 4},
		{[]int{7, 6, 4, 3, 1}, 0},
		{[]int{1}, 0},
	}
	for _, tt := range tests {
		t.Run("123", func(t *testing.T) {
			if got := maxProfit3(tt.prices); got != tt.ans {
				t.Errorf("maxProfit3() = %v, want %v", got, tt.ans)
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

func Test_279(t *testing.T) {
	tests := []struct {
		n   int
		ans int
	}{
		{12, 3},
		{13, 2},
	}
	for _, tt := range tests {
		t.Run("279. Perfect Squares", func(t *testing.T) {
			if got := numSquares(tt.n); got != tt.ans {
				t.Errorf("numSquare() got %v, want %v", got, tt.ans)
			}
		})
	}
}

func Test_309(t *testing.T) {
	tests := []struct {
		prices []int
		ans    int
	}{
		{[]int{1, 2, 3, 0, 2}, 4},
		{[]int{1}, 0},
		{[]int{70, 4, 83, 56, 94, 72, 78, 43, 2, 86, 65, 100, 94, 56, 41, 66, 3, 33, 10, 3, 45, 94, 15, 12, 78, 60, 58, 0, 58, 15, 21, 7, 11, 41, 12, 96, 83, 77, 47, 62, 27, 19, 40, 63, 30, 4, 77, 52, 17, 57, 21, 66, 63, 29, 51, 40, 37, 6, 44, 42, 92, 16, 64, 33, 31, 51, 36, 0, 29, 95, 92, 35, 66, 91, 19, 21, 100, 95, 40, 61, 15, 83, 31, 55, 59, 84, 21, 99, 45, 64, 90, 25, 40, 6, 41, 5, 25, 52, 59, 61, 51, 37, 92, 90, 20, 20, 96, 66, 79, 28, 83, 60, 91, 30, 52, 55, 1, 99, 8, 68, 14, 84, 59, 5, 34, 93, 25, 10, 93, 21, 35, 66, 88, 20, 97, 25, 63, 80, 20, 86, 33, 53, 43, 86, 53, 55, 61, 77, 9, 2, 56, 78, 43, 19, 68, 69, 49, 1, 6, 5, 82, 46, 24, 33, 85, 24, 56, 51, 45, 100, 94, 26, 15, 33, 35, 59, 25, 65, 32, 26, 93, 73, 0, 40, 92, 56, 76, 18, 2, 45, 64, 66, 64, 39, 77, 1, 55, 90, 10, 27, 85, 40, 95, 78, 39, 40, 62, 30, 12, 57, 84, 95, 86, 57, 41, 52, 77, 17, 9, 15, 33, 17, 68, 63, 59, 40, 5, 63, 30, 86, 57, 5, 55, 47, 0, 92, 95, 100, 25, 79, 84, 93, 83, 93, 18, 20, 32, 63, 65, 56, 68, 7, 31, 100, 88, 93, 11, 43, 20, 13, 54, 34, 29, 90, 50, 24, 13, 44, 89, 57, 65, 95, 58, 32, 67, 38, 2, 41, 4, 63, 56, 88, 39, 57, 10, 1, 97, 98, 25, 45, 96, 35, 22, 0, 37, 74, 98, 14, 37, 77, 54, 40, 17, 9, 28, 83, 13, 92, 3, 8, 60, 52, 64, 8, 87, 77, 96, 70, 61, 3, 96, 83, 56, 5, 99, 81, 94, 3, 38, 91, 55, 83, 15, 30, 39, 54, 79, 55, 86, 85, 32, 27, 20, 74, 91, 99, 100, 46, 69, 77, 34, 97, 0, 50, 51, 21, 12, 3, 84, 84, 48, 69, 94, 28, 64, 36, 70, 34, 70, 11, 89, 58, 6, 90, 86, 4, 97, 63, 10, 37, 48, 68, 30, 29, 53, 4, 91, 7, 56, 63, 22, 93, 69, 93, 1, 85, 11, 20, 41, 36, 66, 67, 57, 76, 85, 37, 80, 99, 63, 23, 71, 11, 73, 41, 48, 54, 61, 49, 91, 97, 60, 38, 99, 8, 17, 2, 5, 56, 3, 69, 90, 62, 75, 76, 55, 71, 83, 34, 2, 36, 56, 40, 15, 62, 39, 78, 7, 37, 58, 22, 64, 59, 80, 16, 2, 34, 83, 43, 40, 39, 38, 35, 89, 72, 56, 77, 78, 14, 45, 0, 57, 32, 82, 93, 96, 3, 51, 27, 36, 38, 1, 19, 66, 98, 93, 91, 18, 95, 93, 39, 12, 40, 73, 100, 17, 72, 93, 25, 35, 45, 91, 78, 13, 97, 56, 40, 69, 86, 69, 99, 4, 36, 36, 82, 35, 52, 12, 46, 74, 57, 65, 91, 51, 41, 42, 17, 78, 49, 75, 9, 23, 65, 44, 47, 93, 84, 70, 19, 22, 57, 27, 84, 57, 85, 2, 61, 17, 90, 34, 49, 74, 64, 46, 61, 0, 28, 57, 78, 75, 31, 27, 24, 10, 93, 34, 19, 75, 53, 17, 26, 2, 41, 89, 79, 37, 14, 93, 55, 74, 11, 77, 60, 61, 2, 68, 0, 15, 12, 47, 12, 48, 57, 73, 17, 18, 11, 83, 38, 5, 36, 53, 94, 40, 48, 81, 53, 32, 53, 12, 21, 90, 100, 32, 29, 94, 92, 83, 80, 36, 73, 59, 61, 43, 100, 36, 71, 89, 9, 24, 56, 7, 48, 34, 58, 0, 43, 34, 18, 1, 29, 97, 70, 92, 88, 0, 48, 51, 53, 0, 50, 21, 91, 23, 34, 49, 19, 17, 9, 23, 43, 87, 72, 39, 17, 17, 97, 14, 29, 4, 10, 84, 10, 33, 100, 86, 43, 20, 22, 58, 90, 70, 48, 23, 75, 4, 66, 97, 95, 1, 80, 24, 43, 97, 15, 38, 53, 55, 86, 63, 40, 7, 26, 60, 95, 12, 98, 15, 95, 71, 86, 46, 33, 68, 32, 86, 89, 18, 88, 97, 32, 42, 5, 57, 13, 1, 23, 34, 37, 13, 65, 13, 47, 55, 85, 37, 57, 14, 89, 94, 57, 13, 6, 98, 47, 52, 51, 19, 99, 42, 1, 19, 74, 60, 8, 48, 28, 65, 6, 12, 57, 49, 27, 95, 1, 2, 10, 25, 49, 68, 57, 32, 99, 24, 19, 25, 32, 89, 88, 73, 96, 57, 14, 65, 34, 8, 82, 9, 94, 91, 19, 53, 61, 70, 54, 4, 66, 26, 8, 63, 62, 9, 20, 42, 17, 52, 97, 51, 53, 19, 48, 76, 40, 80, 6, 1, 89, 52, 70, 38, 95, 62, 24, 88, 64, 42, 61, 6, 50, 91, 87, 69, 13, 58, 43, 98, 19, 94, 65, 56, 72, 20, 72, 92, 85, 58, 46, 67, 2, 23, 88, 58, 25, 88, 18, 92, 46, 15, 18, 37, 9, 90, 2, 38, 0, 16, 86, 44, 69, 71, 70, 30, 38, 17, 69, 69, 80, 73, 79, 56, 17, 95, 12, 37, 43, 5, 5, 6, 42, 16, 44, 22, 62, 37, 86, 8, 51, 73, 46, 44, 15, 98, 54, 22, 47, 28, 11, 75, 52, 49, 38, 84, 55, 3, 69, 100, 54, 66, 6, 23, 98, 22, 99, 21, 74, 75, 33, 67, 8, 80, 90, 23, 46, 93, 69, 85, 46, 87, 76, 93, 38, 77, 37, 72, 35, 3, 82, 11, 67, 46, 53, 29, 60, 33, 12, 62, 23, 27, 72, 35, 63, 68, 14, 35, 27, 98, 94, 65, 3, 13, 48, 83, 27, 84, 86, 49, 31, 63, 40, 12, 34, 79, 61, 47, 29, 33, 52, 100, 85, 38, 24, 1, 16, 62, 89, 36, 74, 9, 49, 62, 89}, 17116},
	}
	for _, tt := range tests {
		t.Run("122. Best Time to Buy and Sell Stock II", func(t *testing.T) {
			if got := maxProfit(tt.prices); got != tt.ans {
				t.Errorf("maxProfit() got %v, want %v", got, tt.ans)
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

func Test_421(t *testing.T) {
	tests := []struct {
		nums []int
		ans  int
	}{
		{[]int{3, 10, 5, 25, 2, 8}, 28},
		{[]int{0}, 0},
		{[]int{2, 4}, 6},
		{[]int{8, 10, 2}, 10},
		{[]int{14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70}, 127},
	}
	for _, tt := range tests {
		t.Run("421. Maximum XOR of Two Numbers in an Array", func(t *testing.T) {
			if got := findMaximumXOR(tt.nums); got != tt.ans {
				t.Errorf("findMaximumXOR() = %v, want %v", got, tt.ans)
			}
		})
	}
}

func Test_434(t *testing.T) {
	tests := []struct {
		s   string
		ans int
	}{
		{"Hello, my Name is John", 5},
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

func Test_496(t *testing.T) {
	tests := []struct {
		nums1 []int
		nums2 []int
		ans   []int
	}{
		{[]int{4, 1, 2}, []int{1, 3, 4, 2}, []int{-1, 3, -1}},
		{[]int{2, 4}, []int{1, 2, 3, 4}, []int{3, -1}},
	}
	for _, tt := range tests {
		t.Run("496. Next Greater Element I", func(t *testing.T) {
			if got := nextGreaterElement1(tt.nums1, tt.nums2); !reflect.DeepEqual(got, tt.ans) {
				t.Errorf("nextGreaterElement1() = %v, want %v", got, tt.ans)
			}
		})
	}
}

func Test_525(t *testing.T) {
	tests := []struct {
		nums []int
		ans  int
	}{
		{[]int{0, 1}, 2},
		{[]int{0, 1, 0}, 2},
	}
	for _, tt := range tests {
		t.Run("525. Contiguous Array", func(t *testing.T) {
			if got := findMaxLength(tt.nums); got != tt.ans {
				t.Errorf("findMaxLength() got %v, want %v", got, tt.ans)
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

func Test_852(t *testing.T) {
	tests := []struct {
		arr []int
		ans int
	}{
		{[]int{0, 1, 0}, 1},
		{[]int{1, 3, 5, 4, 2}, 2},
		{[]int{3, 4, 5, 1}, 2},
		{[]int{18, 29, 38, 59, 98, 100, 99, 98, 90}, 5},
		{[]int{3, 5, 3, 2, 0}, 1},
		{[]int{1, 5, 4, 3, 2, 1}, 1},
	}
	for _, tt := range tests {
		t.Run("852. Peak Index in a Mountain Array", func(t *testing.T) {
			if got := peakIndexInMountainArray(tt.arr); got != tt.ans {
				t.Errorf("peakIndexInMountainArray() got %v, want %v", got, tt.ans)
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

func Test_941(t *testing.T) {
	tests := []struct {
		arr []int
		ans bool
	}{
		{[]int{2, 1}, false},
		{[]int{3, 5, 5}, false},
		{[]int{1, 2, 3, 2, 1}, true},
		{[]int{9, 8, 7, 6, 5, 4, 3, 2, 1, 0}, false},
	}
	for _, tt := range tests {
		t.Run("941. Valid Mountain Array", func(t *testing.T) {
			if got := validMountainArray(tt.arr); got != tt.ans {
				t.Errorf("validMountainArray() = %v, want %v", got, tt.ans)
			}
		})
	}
}

func Test_993(t *testing.T) {
	node1 := &TreeNode{Val: 1, Left: nil, Right: nil}
	node2 := &TreeNode{2, nil, nil}
	node3 := &TreeNode{3, nil, nil}
	node4 := &TreeNode{4, nil, nil}
	node5 := &TreeNode{5, nil, nil}
	node6 := &TreeNode{6, nil, nil}
	node7 := &TreeNode{7, nil, nil}
	node8 := &TreeNode{8, nil, nil}
	node9 := &TreeNode{9, nil, nil}
	node1.Right = node2
	node2.Left, node2.Right = node3, node4
	node3.Left, node3.Right = node5, node6
	node4.Left, node4.Right = node7, node8
	node6.Left = node9
	tests := []struct {
		root *TreeNode
		x    int
		y    int
		ans  bool
	}{
		{node1, 5, 8, true},
	}
	for _, tt := range tests {
		t.Run("993. Cousins in Binary Tree", func(t *testing.T) {
			if got := isCousins(tt.root, tt.x, tt.y); got != tt.ans {
				t.Errorf("isCousins() = %v, want %v", got, tt.ans)
			}
		})
	}
}

func TestXXXX(t *testing.T) {
	var ss []string
	println(helper0(ss...))
	ss = []string{"a", "b"}
	println(helper0(ss...))

	var arr = make([]int, 10)
	for i := 0; i < 10; i++ {
		arr[i] = i
	}
	println(arr[8])
	aa := map[string]string{
		"a": "A",
	}
	println("aa[b]:" + aa["b"])

	val, err := strconv.ParseInt("5d8c5d85c8", 36, 64)
	if err != nil {
		println("error:%+v", err)
	}
	println("val=", val)
	makeIt()
}

func helper0(ss ...string) int {
	return len(ss)
}

func makeIt() (s ABC) {
	defer func() {
		fmt.Printf("s.Num = %d", s.Num)
	}()
	s.Num = 1
	return ABC{2, time.Now()}
}
