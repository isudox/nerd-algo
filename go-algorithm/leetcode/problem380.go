package leetcode

import "math/rand"

// 380. Insert Delete GetRandom O(1)
// https://leetcode.com/problems/insert-delete-getrandom-o1/

type RandomizedSet struct {
	table map[int]int
	store []int
}

func _() RandomizedSet {
	return RandomizedSet{
		table: make(map[int]int),
		store: make([]int, 0),
	}
}

func (t *RandomizedSet) Insert(val int) bool {
	if _, ok := t.table[val]; ok {
		return false
	} else {
		t.store = append(t.store, val)
		t.table[val] = len(t.store) - 1
		return true
	}
}

func (t *RandomizedSet) Remove(val int) bool {
	if index, ok := t.table[val]; ok {
		t.store[index], t.store[len(t.store)-1] = t.store[len(t.store)-1], t.store[index]
		t.store = t.store[:len(t.store)-1]
		delete(t.table, val)
		if index < len(t.store) {
			t.table[t.store[index]] = index
		}
		return true
	} else {
		return false
	}
}

func (t *RandomizedSet) GetRandom() int {
	return t.store[rand.Intn(len(t.store))]
}
