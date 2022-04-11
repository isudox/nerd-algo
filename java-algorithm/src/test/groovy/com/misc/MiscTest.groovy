package com.misc

import spock.lang.Specification

class MiscTest extends Specification {

    void setup() {}

    void cleanup() {}

    def "SumOfPower"(int[] nums, int ans) {
        given:
        def sol = new SumOfPower()
        expect:
        sol.getSum(nums) == ans
        where:
        nums         | ans
        [1, 3, 4]    | 59
        [2, 3, 2, 1] | 69
    }
}
