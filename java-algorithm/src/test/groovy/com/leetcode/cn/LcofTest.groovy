package com.leetcode.cn


import spock.lang.Specification

public class LcofTest extends Specification {

    void setup() {}

    void cleanup() {}

    def "lcof test"(int num, int expect) {
        given:
        def solution = new Lcof()

        expect:
        solution.translateNum(num) == expect

        where:
        num   | expect
        12258 | 5
        25    | 2
        506   | 1
    }
}
