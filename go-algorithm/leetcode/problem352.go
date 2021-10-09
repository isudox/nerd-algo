package leetcode

// 352. Data Stream as Disjoint Intervals
// https://leetcode.com/problems/data-stream-as-disjoint-intervals/

type SummaryRanges struct {
	Intervals [][]int
}

func _() SummaryRanges {
	return SummaryRanges{}
}

func (r *SummaryRanges) AddNum(val int) {
	if len(r.Intervals) == 0 {
		r.Intervals = append(r.Intervals, []int{val, val})
		return
	}
	for i, interval := range r.Intervals {
		if interval[0] <= val && val <= interval[1] {
			continue
		}
		if interval[0] > val {
			if i == 0 {
				r.Intervals = append([][]int{{val, val}}, r.Intervals...)
			} else {
				if r.Intervals[i-1][1] == val-1 && interval[0] == val+1 {
					interval[0] = r.Intervals[i-1][0]
					r.Intervals = append(r.Intervals[:i-1], r.Intervals[i:]...)
					return
				} else if r.Intervals[i-1][1] == val-1 {
					r.Intervals[i-1][1] = val
				} else if interval[0] == val+1 {
					interval[0] = val
				} else {
					left := append(r.Intervals[:i], []int{val, val})
					right := r.Intervals[i:]
					r.Intervals = append(left, right...)
					return
				}
			}
		} else {
			if i == len(r.Intervals)-1 {
				r.Intervals = append(r.Intervals, []int{val, val})
				return
			}
		}
	}
}

func (r *SummaryRanges) GetIntervals() [][]int {
	return r.Intervals
}
