package main

// 258.
//

func addDigits(num int) int {
    next_num := 0
    for num > 9 {
        a, b := num / 10, num % 10
        next_num += b
        num = a
        if num < 10 {
            num += next_num
            next_num = 0
        }
    }
    return num
}

