package main

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
			break
		}
		if interval[0] == val+1 {
			if i > 0 && r.Intervals[i-1][1] == val-1 {
				interval[0] = r.Intervals[i-1][0]
				r.Intervals = append(r.Intervals[:i-1], r.Intervals[i:]...)
				return
			} else {
				interval[0] = val
			}
			return
		}
		if interval[0] > val+1 {
			if i > 0 && r.Intervals[i-1][1]+1 == val {
				r.Intervals[i-1][1] = val
			} else {
				r.Intervals = append(r.Intervals[:i+1], r.Intervals[i:]...)
				r.Intervals[i] = []int{val, val}
			}
			return
		}
		if i == len(r.Intervals)-1 {
			if interval[1] == val-1 {
				interval[1] = val
			} else {
				r.Intervals = append(r.Intervals, []int{val, val})
			}
			return
		}
	}
}

func (r *SummaryRanges) GetIntervals() [][]int {
	return r.Intervals
}
