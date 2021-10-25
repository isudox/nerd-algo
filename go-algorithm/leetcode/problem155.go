package leetcode

// 155. Min Stack
// https://leetcode.com/problems/min-stack/

type MinStack struct {
	store    []int
	minStore []int
}

func _() MinStack {
	return MinStack{}
}

func (t *MinStack) Push(val int) {
	t.store = append(t.store, val)
	if len(t.minStore) == 0 || val <= t.minStore[len(t.minStore)-1] {
		t.minStore = append(t.minStore, val)
	}
}

func (t *MinStack) Pop() {
	num := t.Top()
	if num == t.GetMin() {
		t.minStore = t.minStore[:len(t.minStore)-1]
	}
	t.store = t.store[:len(t.store)-1]
}

func (t *MinStack) Top() int {
	return t.store[len(t.store)-1]
}

func (t *MinStack) GetMin() int {
	return t.minStore[len(t.minStore)-1]
}
