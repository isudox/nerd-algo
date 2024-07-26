package com.leetcode

import com.common.*
import org.spockframework.util.Assert
import spock.lang.Specification

/**
 * Test algorithms with incomplete cases by Spock.
 */
class LeetCodeTest extends Specification {

    void setup() {}

    void cleanup() {}

    def "1. Two Sum"(int[] nums, int target, int[] result) {
        given:
        def solution = new Problem1()
        expect:
        solution.twoSum1(nums, target) == result
        solution.twoSum2(nums, target) == result
        where:
        nums                           | target | result
        [1, 5, 8, 10, 23, 99] as int[] | 31     | [2, 4] as int[]
        [1, 5, 8, 10, 23, 99] as int[] | 100    | [0, 5] as int[]
        [-1, 0, 5, 10, 15, 8] as int[] | 9      | [0, 3] as int[]
        [-1, -3, -5, 10, 100] as int[] | 110    | [3, 4] as int[]
    }

    def "2. Add Two Numbers"() {
        given:
        def solution = new Problem2()
        def arr1 = [2, 4, 3] as int[]
        def arr2 = [5, 6, 4] as int[]
        def l1 = Converter.convertListNode(arr1)
        def l2 = Converter.convertListNode(arr2)
        when:
        def res1 = solution.addTwoNumbers1(l1, l2)
        def res2 = solution.addTwoNumbers2(l1, l2)
        def expected = Converter.convertListNode([7, 0, 8] as int[])
        then:
        Converter.convertArray(expected) == Converter.convertArray(res1)
        Converter.convertArray(expected) == Converter.convertArray(res2)
    }

    def "3. Longest Substring Without Repeating Characters"(String s, int len) {
        given:
        def solution = new Problem3()
        expect:
        solution.lengthOfLongestSubstring(s) == len
        where:
        s          | len
        "abcabcbb" | 3
        "bbbbb"    | 1
        "pwwkew"   | 3
    }

    def "23. Merge k Sorted Lists"() {
        given:
        def solution = new Problem23()
        def i1 = [1, 4, 5] as int[]
        def i2 = [1, 3, 4] as int[]
        int[] i3 = [2, 6]
        def l1 = Converter.convertListNode(i1)
        def l2 = Converter.convertListNode(i2)
        def l3 = Converter.convertListNode(i3)
        when:
        def res = solution.mergeKLists([l1, l2, l3] as ListNode[])
        then:
        Converter.convertArray(res) == [1, 1, 2, 3, 4, 4, 5, 6] as int[]
    }

    def "25. Reverse Nodes in k-Group"(int[] nums, int k, int[] res) {
        given:
        def solution = new Problem25()
        def node = Converter.convertListNode(nums)
        expect:
        Converter.convertArray(solution.reverseKGroup(node, k)) == res
        where:
        nums                     | k | res
        [1] as int[]             | 3 | [1] as int[]
        [1, 2, 3, 4, 5] as int[] | 1 | [1, 2, 3, 4, 5] as int[]
        [1, 2, 3, 4, 5] as int[] | 2 | [2, 1, 4, 3, 5] as int[]
        [1, 2, 3, 4, 5] as int[] | 3 | [3, 2, 1, 4, 5] as int[]
    }

    def "31. Next Permutation"(int[] nums, int[] ans) {
        given:
        def sol = new Problem31()
        expect:
        sol.nextPermutation(nums)
        assert nums == ans
        where:
        nums      | ans
        [1, 2, 3] | [1, 3, 2]
        [1, 3, 2] | [2, 1, 3]
        [3, 2, 1] | [1, 2, 3]
        [5, 1, 1] | [1, 1, 5]
        [1, 1, 5] | [1, 5, 1]
        [1]       | [1]
    }

    def "32. Longest Valid Parentheses"(String s, int len) {
        given:
        def solution = new Problem32()
        expect:
        solution.longestValidParentheses(s) == len
        solution.longestValidParentheses2(s) == len
        where:
        s           | len
        ""          | 0
        "()"        | 2
        "((()"      | 2
        "(()()"     | 4
        "(()()(()"  | 4
        ")()())"    | 4
        "(()))())(" | 4
        "()(()))))" | 6
    }

    def "33. Search in Rotated Sorted Array"(int[] nums, int target, int res) {
        given:
        def solution = new Problem33()
        expect:
        solution.search1(nums, target) == res
        solution.search2(nums, target) == res
        where:
        nums                  | target | res
        []                    | 1      | -1
        [1]                   | 1      | 0
        [1, 3]                | 3      | 1
        [4, 5, 6, 7, 0, 1, 2] | 0      | 4
        [4, 5, 6, 7, 0, 1, 2] | 3      | -1
    }

    def "34. Find First and Last Position of Element in Sorted Array"(int[] nums, int target, int[] res) {
        given:
        def solution = new Problem34()
        expect:
        solution.searchRange(nums, target) == res
        where:
        nums                         | target | res
        [5, 7, 7, 8, 8, 10] as int[] | 8      | [3, 4] as int[]
        [5, 7, 7, 8, 8, 10] as int[] | 6      | [-1, -1] as int[]
    }

    def "35. Search Insert Position"(int[] nums, int target, int res) {
        given:
        def solution = new Problem35()
        expect:
        solution.searchInsert(nums, target) == res
        where:
        nums         | target | res
        []           | 9      | 0
        [1]          | 2      | 1
        [1, 3, 5, 6] | 5      | 2
        [1, 3, 5, 6] | 2      | 1
        [1, 3, 5, 6] | 7      | 4
        [1, 3, 5, 6] | 0      | 0
    }

    def "36. Valid Sudoku"(char[][] board, boolean res) {
        given:
        def solution = new Problem36()
        expect:
        res == solution.isValidSudoku(board)
        where:
        board                                           | res
        [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]] | false
        [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]] | true
    }

    def "39. Combination Sum"(int[] candidates, int target, List<List<Integer>> ans) {
        given:
        def solution = new Problem39()
        expect:
        solution.combinationSum(candidates, target) == ans
        where:
        candidates   | target | ans
        [2, 3, 6, 7] | 7      | [[2, 2, 3], [7]]
        [2, 3, 5]    | 8      | [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    }

    def "40. Combination Sum II"(int[] candidates, int target, List<List<Integer>> expect) {
        given:
        def solution = new Problem40()
        expect:
        solution.combinationSum2(candidates, target) == expect
        where:
        candidates             | target | expect
        [10, 1, 2, 7, 6, 1, 5] | 8      | [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        [2, 5, 2, 1, 2]        | 5      | [[1, 2, 2], [5]]
    }

    def "41. First Missing Positive"(int[] nums, int expect) {
        given:
        def solution = new Problem41()
        expect:
        solution.firstMissingPositive(nums) == expect
        where:
        nums              | expect
        [1, 2, 0]         | 3
        [3, 4, -1, 1]     | 2
        [7, 8, 9, 11, 12] | 1
    }

    def "42. Trapping Rain Water"(int[] height, int expect) {
        given:
        def solution = new Problem42()
        expect:
        solution.trap(height) == expect
        where:
        height                               | expect
        [3, 2, 1, 2, 1]                      | 1
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] | 6
    }

    def "44. Wildcard Matching"(String s, String p, boolean ans) {
        given:
        def sol = new Problem44()
        expect:
        sol.isMatch(s, p) == ans
        where:
        s       | p       | ans
        "acdcb" | "a*c?b" | false
        "adceb" | "*a*b"  | true
        "cb"    | "?a"    | false
        "aa"    | "*"     | true
        "aa"    | "a"     | false
    }

    def "46. Permutations"(int[] nums, List<List<Integer>> expect) {
        given:
        def solution = new Problem46()
        expect:
        solution.permute(nums) == expect
        where:
        nums      | expect
        [1, 2, 3] | [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]
    }

    def "49. Group Anagrams"(String[] strs, List<List<String>> ans) {
        given:
        def sol = new Problem49()
        expect:
        sol.groupAnagrams(strs) == ans
        where:
        strs                                       | ans
        ["eat", "tea", "tan", "ate", "nat", "bat"] | [["bat"], ["tan", "nat"], ["eat", "tea", "ate"]]
    }

    def "53. Maximum Subarray"(int[] nums, int expect) {
        given:
        def solution = new Problem53()
        expect:
        solution.maxSubArray(nums) == expect
        where:
        nums                            | expect
        [-2]                            | -2
        [-2, -1]                        | -1
        [-2, 1, -3, 4, -1, 2, 1, -5, 4] | 6
    }

    def "62. Unique Paths"(int m, int n, int ans) {
        given:
        def sol = new Problem62()
        expect:
        sol.uniquePaths(m, n) == ans
        where:
        m | n | ans
        7 | 3 | 28
        3 | 2 | 3
        9 | 9 | 12870
    }

    def "63. Unique Paths II"(int[][] grid, int ans) {
        given:
        def sol = new Problem63()
        expect:
        sol.uniquePathsWithObstacles(grid) == ans
        where:
        grid        | ans
        [[1]]       | 0
        [[0, 0, 0],
         [0, 1, 0],
         [0, 0, 0]] | 2
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]] | 6
    }

    def "64. Minimum Path Sum"(int[][] grid, int ans) {
        given:
        def sol = new Problem64()
        expect:
        sol.findPathSum(grid) == ans
        where:
        grid        | ans
        [[1, 3, 1],
         [1, 5, 1],
         [4, 2, 1]] | 7
    }

    def "70. Climbing Stairs"(int n, int expect) {
        given:
        def solution = new Problem70()
        expect:
        solution.climbStairs(n) == expect
        where:
        n  | expect
        3  | 3
        10 | 89
    }

    def "78. Subsets"(int[] nums, List<List<Integer>> expect) {
        given:
        def solution = new Problem78()
        expect:
        solution.subsets(nums) == expect
        where:
        nums      | expect
        []        | [[]]
        [1]       | [[], [1]]
        [1, 2]    | [[], [1], [2], [1, 2]]
        [1, 2, 3] | [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    }

    def "84. Largest Rectangle in Histogram"(int[] heights, int result) {
        given:
        def solution = new Problem84()
        expect:
        solution.largestRectangleArea(heights) == result
        where:
        heights               | result
        [2, 1, 5, 6, 2, 3]    | 10
        [6, 2, 5, 4, 5, 1, 6] | 12
        [2, 2, 2, 2, 2]       | 10
        []                    | 0
    }

    def '87. Scramble String'(String s1, String s2, boolean ans) {
        given:
        def sol = new Problem87()
        expect:
        sol.isScramble(s1, s2) == ans
        where:
        s1                            | s2                            | ans
        "eebaacbcbcadaaedceaaacadccd" | "eadcaacabaddaceacbceaabeccd" | false
        "great"                       | "rgeat"                       | true
        "abcde"                       | "caebd"                       | false
        "a"                           | "a"                           | true
        "b"                           | "a"                           | false
    }

    def "90. Subsets II"(int[] nums, List<List<Integer>> expect) {
        given:
        def solution = new Problem90()
        expect:
        solution.subsetsWithDup(nums) == expect
        where:
        nums      | expect
        [2, 2, 2] | [[], [2], [2, 2], [2, 2, 2]]
        [1, 2, 2] | [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
    }

    def "91. Decode Ways"(String s, int ans) {
        given:
        def sol = new Problem91()
        expect:
        sol.numDecodings(s) == ans
        sol.numDecodings2(s) == ans
        where:
        s        | ans
        "226"    | 3
        "201"    | 1
        "12"     | 2
        "27"     | 1
        "06"     | 0
        "110011" | 0
    }

    def "96. Unique Binary Search Trees"(int n, int ans) {
        given:
        def sol = new Problem96()
        expect:
        sol.numTrees(n) == ans
        sol.numTrees2(n) == ans
        where:
        n | ans
        3 | 5
        4 | 14
        5 | 42
    }

    def "127. Word Ladder"(String beginWord, String endWord, List<String> wordList, int ans) {
        given:
        def sol = new Problem127()
        expect:
        sol.ladderLength(beginWord, endWord, wordList) == ans
        where:
        beginWord | endWord | wordList | ans
        "talk"    | "tail"  | ["talk", "tons", "fall", "tail", "gale", "hall", "negs"] | 0
        "hot"     | "dog"   | ["hot", "dog"] | 0
        "hit"     | "cog"   | ["hot", "dot", "dog", "lot", "log"] | 0
        "hit"     | "cog"   | ["hot", "dot", "dog", "lot", "log", "cog"] | 5
        "sand"    | "acne"  | ["slit", "bunk", "wars", "ping", "viva", "wynn", "wows", "irks", "gang", "pool", "mock", "fort", "heel", "send", "ship", "cols", "alec", "foal", "nabs", "gaze", "giza", "mays", "dogs", "karo", "cums", "jedi", "webb", "lend", "mire", "jose", "catt", "grow", "toss", "magi", "leis", "bead", "kara", "hoof", "than", "ires", "baas", "vein", "kari", "riga", "oars", "gags", "thug", "yawn", "wive", "view", "germ", "flab", "july", "tuck", "rory", "bean", "feed", "rhee", "jeez", "gobs", "lath", "desk", "yoko", "cute", "zeus", "thus", "dims", "link", "dirt", "mara", "disc", "limy", "lewd", "maud", "duly", "elsa", "hart", "rays", "rues", "camp", "lack", "okra", "tome", "math", "plug", "monk", "orly", "friz", "hogs", "yoda", "poop", "tick", "plod", "cloy", "pees", "imps", "lead", "pope", "mall", "frey", "been", "plea", "poll", "male", "teak", "soho", "glob", "bell", "mary", "hail", "scan", "yips", "like", "mull", "kory", "odor", "byte", "kaye", "word", "honk", "asks", "slid", "hopi", "toke", "gore", "flew", "tins", "mown", "oise", "hall", "vega", "sing", "fool", "boat", "bobs", "lain", "soft", "hard", "rots", "sees", "apex", "chan", "told", "woos", "unit", "scow", "gilt", "beef", "jars", "tyre", "imus", "neon", "soap", "dabs", "rein", "ovid", "hose", "husk", "loll", "asia", "cope", "tail", "hazy", "clad", "lash", "sags", "moll", "eddy", "fuel", "lift", "flog", "land", "sigh", "saks", "sail", "hook", "visa", "tier", "maws", "roeg", "gila", "eyes", "noah", "hypo", "tore", "eggs", "rove", "chap", "room", "wait", "lurk", "race", "host", "dada", "lola", "gabs", "sobs", "joel", "keck", "axed", "mead", "gust", "laid", "ends", "oort", "nose", "peer", "kept", "abet", "iran", "mick", "dead", "hags", "tens", "gown", "sick", "odis", "miro", "bill", "fawn", "sumo", "kilt", "huge", "ores", "oran", "flag", "tost", "seth", "sift", "poet", "reds", "pips", "cape", "togo", "wale", "limn", "toll", "ploy", "inns", "snag", "hoes", "jerk", "flux", "fido", "zane", "arab", "gamy", "raze", "lank", "hurt", "rail", "hind", "hoot", "dogy", "away", "pest", "hoed", "pose", "lose", "pole", "alva", "dino", "kind", "clan", "dips", "soup", "veto", "edna", "damp", "gush", "amen", "wits", "pubs", "fuzz", "cash", "pine", "trod", "gunk", "nude", "lost", "rite", "cory", "walt", "mica", "cart", "avow", "wind", "book", "leon", "life", "bang", "draw", "leek", "skis", "dram", "ripe", "mine", "urea", "tiff", "over", "gale", "weir", "defy", "norm", "tull", "whiz", "gill", "ward", "crag", "when", "mill", "firs", "sans", "flue", "reid", "ekes", "jain", "mutt", "hems", "laps", "piss", "pall", "rowe", "prey", "cull", "knew", "size", "wets", "hurl", "wont", "suva", "girt", "prys", "prow", "warn", "naps", "gong", "thru", "livy", "boar", "sade", "amok", "vice", "slat", "emir", "jade", "karl", "loyd", "cerf", "bess", "loss", "rums", "lats", "bode", "subs", "muss", "maim", "kits", "thin", "york", "punt", "gays", "alpo", "aids", "drag", "eras", "mats", "pyre", "clot", "step", "oath", "lout", "wary", "carp", "hums", "tang", "pout", "whip", "fled", "omar", "such", "kano", "jake", "stan", "loop", "fuss", "mini", "byrd", "exit", "fizz", "lire", "emil", "prop", "noes", "awed", "gift", "soli", "sale", "gage", "orin", "slur", "limp", "saar", "arks", "mast", "gnat", "port", "into", "geed", "pave", "awls", "cent", "cunt", "full", "dint", "hank", "mate", "coin", "tars", "scud", "veer", "coax", "bops", "uris", "loom", "shod", "crib", "lids", "drys", "fish", "edit", "dick", "erna", "else", "hahs", "alga", "moho", "wire", "fora", "tums", "ruth", "bets", "duns", "mold", "mush", "swop", "ruby", "bolt", "nave", "kite", "ahem", "brad", "tern", "nips", "whew", "bait", "ooze", "gino", "yuck", "drum", "shoe", "lobe", "dusk", "cult", "paws", "anew", "dado", "nook", "half", "lams", "rich", "cato", "java", "kemp", "vain", "fees", "sham", "auks", "gish", "fire", "elam", "salt", "sour", "loth", "whit", "yogi", "shes", "scam", "yous", "lucy", "inez", "geld", "whig", "thee", "kelp", "loaf", "harm", "tomb", "ever", "airs", "page", "laud", "stun", "paid", "goop", "cobs", "judy", "grab", "doha", "crew", "item", "fogs", "tong", "blip", "vest", "bran", "wend", "bawl", "feel", "jets", "mixt", "tell", "dire", "devi", "milo", "deng", "yews", "weak", "mark", "doug", "fare", "rigs", "poke", "hies", "sian", "suez", "quip", "kens", "lass", "zips", "elva", "brat", "cosy", "teri", "hull", "spun", "russ", "pupa", "weed", "pulp", "main", "grim", "hone", "cord", "barf", "olav", "gaps", "rote", "wilt", "lars", "roll", "balm", "jana", "give", "eire", "faun", "suck", "kegs", "nita", "weer", "tush", "spry", "loge", "nays", "heir", "dope", "roar", "peep", "nags", "ates", "bane", "seas", "sign", "fred", "they", "lien", "kiev", "fops", "said", "lawn", "lind", "miff", "mass", "trig", "sins", "furl", "ruin", "sent", "cray", "maya", "clog", "puns", "silk", "axis", "grog", "jots", "dyer", "mope", "rand", "vend", "keen", "chou", "dose", "rain", "eats", "sped", "maui", "evan", "time", "todd", "skit", "lief", "sops", "outs", "moot", "faze", "biro", "gook", "fill", "oval", "skew", "veil", "born", "slob", "hyde", "twin", "eloy", "beat", "ergs", "sure", "kobe", "eggo", "hens", "jive", "flax", "mons", "dunk", "yest", "begs", "dial", "lodz", "burp", "pile", "much", "dock", "rene", "sago", "racy", "have", "yalu", "glow", "move", "peps", "hods", "kins", "salk", "hand", "cons", "dare", "myra", "sega", "type", "mari", "pelt", "hula", "gulf", "jugs", "flay", "fest", "spat", "toms", "zeno", "taps", "deny", "swag", "afro", "baud", "jabs", "smut", "egos", "lara", "toes", "song", "fray", "luis", "brut", "olen", "mere", "ruff", "slum", "glad", "buds", "silt", "rued", "gelt", "hive", "teem", "ides", "sink", "ands", "wisp", "omen", "lyre", "yuks", "curb", "loam", "darn", "liar", "pugs", "pane", "carl", "sang", "scar", "zeds", "claw", "berg", "hits", "mile", "lite", "khan", "erik", "slug", "loon", "dena", "ruse", "talk", "tusk", "gaol", "tads", "beds", "sock", "howe", "gave", "snob", "ahab", "part", "meir", "jell", "stir", "tels", "spit", "hash", "omit", "jinx", "lyra", "puck", "laue", "beep", "eros", "owed", "cede", "brew", "slue", "mitt", "jest", "lynx", "wads", "gena", "dank", "volt", "gray", "pony", "veld", "bask", "fens", "argo", "work", "taxi", "afar", "boon", "lube", "pass", "lazy", "mist", "blot", "mach", "poky", "rams", "sits", "rend", "dome", "pray", "duck", "hers", "lure", "keep", "gory", "chat", "runt", "jams", "lays", "posy", "bats", "hoff", "rock", "keri", "raul", "yves", "lama", "ramp", "vote", "jody", "pock", "gist", "sass", "iago", "coos", "rank", "lowe", "vows", "koch", "taco", "jinn", "juno", "rape", "band", "aces", "goal", "huck", "lila", "tuft", "swan", "blab", "leda", "gems", "hide", "tack", "porn", "scum", "frat", "plum", "duds", "shad", "arms", "pare", "chin", "gain", "knee", "foot", "line", "dove", "vera", "jays", "fund", "reno", "skid", "boys", "corn", "gwyn", "sash", "weld", "ruiz", "dior", "jess", "leaf", "pars", "cote", "zing", "scat", "nice", "dart", "only", "owls", "hike", "trey", "whys", "ding", "klan", "ross", "barb", "ants", "lean", "dopy", "hock", "tour", "grip", "aldo", "whim", "prom", "rear", "dins", "duff", "dell", "loch", "lava", "sung", "yank", "thar", "curl", "venn", "blow", "pomp", "heat", "trap", "dali", "nets", "seen", "gash", "twig", "dads", "emmy", "rhea", "navy", "haws", "mite", "bows", "alas", "ives", "play", "soon", "doll", "chum", "ajar", "foam", "call", "puke", "kris", "wily", "came", "ales", "reef", "raid", "diet", "prod", "prut", "loot", "soar", "coed", "celt", "seam", "dray", "lump", "jags", "nods", "sole", "kink", "peso", "howl", "cost", "tsar", "uric", "sore", "woes", "sewn", "sake", "cask", "caps", "burl", "tame", "bulk", "neva", "from", "meet", "webs", "spar", "fuck", "buoy", "wept", "west", "dual", "pica", "sold", "seed", "gads", "riff", "neck", "deed", "rudy", "drop", "vale", "flit", "romp", "peak", "jape", "jews", "fain", "dens", "hugo", "elba", "mink", "town", "clam", "feud", "fern", "dung", "newt", "mime", "deem", "inti", "gigs", "sosa", "lope", "lard", "cara", "smug", "lego", "flex", "doth", "paar", "moon", "wren", "tale", "kant", "eels", "muck", "toga", "zens", "lops", "duet", "coil", "gall", "teal", "glib", "muir", "ails", "boer", "them", "rake", "conn", "neat", "frog", "trip", "coma", "must", "mono", "lira", "craw", "sled", "wear", "toby", "reel", "hips", "nate", "pump", "mont", "died", "moss", "lair", "jibe", "oils", "pied", "hobs", "cads", "haze", "muse", "cogs", "figs", "cues", "roes", "whet", "boru", "cozy", "amos", "tans", "news", "hake", "cots", "boas", "tutu", "wavy", "pipe", "typo", "albs", "boom", "dyke", "wail", "woke", "ware", "rita", "fail", "slab", "owes", "jane", "rack", "hell", "lags", "mend", "mask", "hume", "wane", "acne", "team", "holy", "runs", "exes", "dole", "trim", "zola", "trek", "puma", "wacs", "veep", "yaps", "sums", "lush", "tubs", "most", "witt", "bong", "rule", "hear", "awry", "sots", "nils", "bash", "gasp", "inch", "pens", "fies", "juts", "pate", "vine", "zulu", "this", "bare", "veal", "josh", "reek", "ours", "cowl", "club", "farm", "teat", "coat", "dish", "fore", "weft", "exam", "vlad", "floe", "beak", "lane", "ella", "warp", "goth", "ming", "pits", "rent", "tito", "wish", "amps", "says", "hawk", "ways", "punk", "nark", "cagy", "east", "paul", "bose", "solo", "teed", "text", "hews", "snip", "lips", "emit", "orgy", "icon", "tuna", "soul", "kurd", "clod", "calk", "aunt", "bake", "copy", "acid", "duse", "kiln", "spec", "fans", "bani", "irma", "pads", "batu", "logo", "pack", "oder", "atop", "funk", "gide", "bede", "bibs", "taut", "guns", "dana", "puff", "lyme", "flat", "lake", "june", "sets", "gull", "hops", "earn", "clip", "fell", "kama", "seal", "diaz", "cite", "chew", "cuba", "bury", "yard", "bank", "byes", "apia", "cree", "nosh", "judo", "walk", "tape", "taro", "boot", "cods", "lade", "cong", "deft", "slim", "jeri", "rile", "park", "aeon", "fact", "slow", "goff", "cane", "earp", "tart", "does", "acts", "hope", "cant", "buts", "shin", "dude", "ergo", "mode", "gene", "lept", "chen", "beta", "eden", "pang", "saab", "fang", "whir", "cove", "perk", "fads", "rugs", "herb", "putt", "nous", "vane", "corm", "stay", "bids", "vela", "roof", "isms", "sics", "gone", "swum", "wiry", "cram", "rink", "pert", "heap", "sikh", "dais", "cell", "peel", "nuke", "buss", "rasp", "none", "slut", "bent", "dams", "serb", "dork", "bays", "kale", "cora", "wake", "welt", "rind", "trot", "sloe", "pity", "rout", "eves", "fats", "furs", "pogo", "beth", "hued", "edam", "iamb", "glee", "lute", "keel", "airy", "easy", "tire", "rube", "bogy", "sine", "chop", "rood", "elbe", "mike", "garb", "jill", "gaul", "chit", "dons", "bars", "ride", "beck", "toad", "make", "head", "suds", "pike", "snot", "swat", "peed", "same", "gaza", "lent", "gait", "gael", "elks", "hang", "nerf", "rosy", "shut", "glop", "pain", "dion", "deaf", "hero", "doer", "wost", "wage", "wash", "pats", "narc", "ions", "dice", "quay", "vied", "eons", "case", "pour", "urns", "reva", "rags", "aden", "bone", "rang", "aura", "iraq", "toot", "rome", "hals", "megs", "pond", "john", "yeps", "pawl", "warm", "bird", "tint", "jowl", "gibe", "come", "hold", "pail", "wipe", "bike", "rips", "eery", "kent", "hims", "inks", "fink", "mott", "ices", "macy", "serf", "keys", "tarp", "cops", "sods", "feet", "tear", "benz", "buys", "colo", "boil", "sews", "enos", "watt", "pull", "brag", "cork", "save", "mint", "feat", "jamb", "rubs", "roxy", "toys", "nosy", "yowl", "tamp", "lobs", "foul", "doom", "sown", "pigs", "hemp", "fame", "boor", "cube", "tops", "loco", "lads", "eyre", "alta", "aged", "flop", "pram", "lesa", "sawn", "plow", "aral", "load", "lied", "pled", "boob", "bert", "rows", "zits", "rick", "hint", "dido", "fist", "marc", "wuss", "node", "smog", "nora", "shim", "glut", "bale", "perl", "what", "tort", "meek", "brie", "bind", "cake", "psst", "dour", "jove", "tree", "chip", "stud", "thou", "mobs", "sows", "opts", "diva", "perm", "wise", "cuds", "sols", "alan", "mild", "pure", "gail", "wins", "offs", "nile", "yelp", "minn", "tors", "tran", "homy", "sadr", "erse", "nero", "scab", "finn", "mich", "turd", "then", "poem", "noun", "oxus", "brow", "door", "saws", "eben", "wart", "wand", "rosa", "left", "lina", "cabs", "rapt", "olin", "suet", "kalb", "mans", "dawn", "riel", "temp", "chug", "peal", "drew", "null", "hath", "many", "took", "fond", "gate", "sate", "leak", "zany", "vans", "mart", "hess", "home", "long", "dirk", "bile", "lace", "moog", "axes", "zone", "fork", "duct", "rico", "rife", "deep", "tiny", "hugh", "bilk", "waft", "swig", "pans", "with", "kern", "busy", "film", "lulu", "king", "lord", "veda", "tray", "legs", "soot", "ells", "wasp", "hunt", "earl", "ouch", "diem", "yell", "pegs", "blvd", "polk", "soda", "zorn", "liza", "slop", "week", "kill", "rusk", "eric", "sump", "haul", "rims", "crop", "blob", "face", "bins", "read", "care", "pele", "ritz", "beau", "golf", "drip", "dike", "stab", "jibs", "hove", "junk", "hoax", "tats", "fief", "quad", "peat", "ream", "hats", "root", "flak", "grit", "clap", "pugh", "bosh", "lock", "mute", "crow", "iced", "lisa", "bela", "fems", "oxes", "vies", "gybe", "huff", "bull", "cuss", "sunk", "pups", "fobs", "turf", "sect", "atom", "debt", "sane", "writ", "anon", "mayo", "aria", "seer", "thor", "brim", "gawk", "jack", "jazz", "menu", "yolk", "surf", "libs", "lets", "bans", "toil", "open", "aced", "poor", "mess", "wham", "fran", "gina", "dote", "love", "mood", "pale", "reps", "ines", "shot", "alar", "twit", "site", "dill", "yoga", "sear", "vamp", "abel", "lieu", "cuff", "orbs", "rose", "tank", "gape", "guam", "adar", "vole", "your", "dean", "dear", "hebe", "crab", "hump", "mole", "vase", "rode", "dash", "sera", "balk", "lela", "inca", "gaea", "bush", "loud", "pies", "aide", "blew", "mien", "side", "kerr", "ring", "tess", "prep", "rant", "lugs", "hobo", "joke", "odds", "yule", "aida", "true", "pone", "lode", "nona", "weep", "coda", "elmo", "skim", "wink", "bras", "pier", "bung", "pets", "tabs", "ryan", "jock", "body", "sofa", "joey", "zion", "mace", "kick", "vile", "leno", "bali", "fart", "that", "redo", "ills", "jogs", "pent", "drub", "slaw", "tide", "lena", "seep", "gyps", "wave", "amid", "fear", "ties", "flan", "wimp", "kali", "shun", "crap", "sage", "rune", "logs", "cain", "digs", "abut", "obit", "paps", "rids", "fair", "hack", "huns", "road", "caws", "curt", "jute", "fisk", "fowl", "duty", "holt", "miss", "rude", "vito", "baal", "ural", "mann", "mind", "belt", "clem", "last", "musk", "roam", "abed", "days", "bore", "fuze", "fall", "pict", "dump", "dies", "fiat", "vent", "pork", "eyed", "docs", "rive", "spas", "rope", "ariz", "tout", "game", "jump", "blur", "anti", "lisp", "turn", "sand", "food", "moos", "hoop", "saul", "arch", "fury", "rise", "diss", "hubs", "burs", "grid", "ilks", "suns", "flea", "soil", "lung", "want", "nola", "fins", "thud", "kidd", "juan", "heps", "nape", "rash", "burt", "bump", "tots", "brit", "mums", "bole", "shah", "tees", "skip", "limb", "umps", "ache", "arcs", "raft", "halo", "luce", "bahs", "leta", "conk", "duos", "siva", "went", "peek", "sulk", "reap", "free", "dubs", "lang", "toto", "hasp", "ball", "rats", "nair", "myst", "wang", "snug", "nash", "laos", "ante", "opal", "tina", "pore", "bite", "haas", "myth", "yugo", "foci", "dent", "bade", "pear", "mods", "auto", "shop", "etch", "lyly", "curs", "aron", "slew", "tyro", "sack", "wade", "clio", "gyro", "butt", "icky", "char", "itch", "halt", "gals", "yang", "tend", "pact", "bees", "suit", "puny", "hows", "nina", "brno", "oops", "lick", "sons", "kilo", "bust", "nome", "mona", "dull", "join", "hour", "papa", "stag", "bern", "wove", "lull", "slip", "laze", "roil", "alto", "bath", "buck", "alma", "anus", "evil", "dumb", "oreo", "rare", "near", "cure", "isis", "hill", "kyle", "pace", "comb", "nits", "flip", "clop", "mort", "thea", "wall", "kiel", "judd", "coop", "dave", "very", "amie", "blah", "flub", "talc", "bold", "fogy", "idea", "prof", "horn", "shoo", "aped", "pins", "helm", "wees", "beer", "womb", "clue", "alba", "aloe", "fine", "bard", "limo", "shaw", "pint", "swim", "dust", "indy", "hale", "cats", "troy", "wens", "luke", "vern", "deli", "both", "brig", "daub", "sara", "sued", "bier", "noel", "olga", "dupe", "look", "pisa", "knox", "murk", "dame", "matt", "gold", "jame", "toge", "luck", "peck", "tass", "calf", "pill", "wore", "wadi", "thur", "parr", "maul", "tzar", "ones", "lees", "dark", "fake", "bast", "zoom", "here", "moro", "wine", "bums", "cows", "jean", "palm", "fume", "plop", "help", "tuba", "leap", "cans", "back", "avid", "lice", "lust", "polo", "dory", "stew", "kate", "rama", "coke", "bled", "mugs", "ajax", "arts", "drug", "pena", "cody", "hole", "sean", "deck", "guts", "kong", "bate", "pitt", "como", "lyle", "siam", "rook", "baby", "jigs", "bret", "bark", "lori", "reba", "sups", "made", "buzz", "gnaw", "alps", "clay", "post", "viol", "dina", "card", "lana", "doff", "yups", "tons", "live", "kids", "pair", "yawl", "name", "oven", "sirs", "gyms", "prig", "down", "leos", "noon", "nibs", "cook", "safe", "cobb", "raja", "awes", "sari", "nerd", "fold", "lots", "pete", "deal", "bias", "zeal", "girl", "rage", "cool", "gout", "whey", "soak", "thaw", "bear", "wing", "nagy", "well", "oink", "sven", "kurt", "etna", "held", "wood", "high", "feta", "twee", "ford", "cave", "knot", "tory", "ibis", "yaks", "vets", "foxy", "sank", "cone", "pius", "tall", "seem", "wool", "flap", "gird", "lore", "coot", "mewl", "sere", "real", "puts", "sell", "nuts", "foil", "lilt", "saga", "heft", "dyed", "goat", "spew", "daze", "frye", "adds", "glen", "tojo", "pixy", "gobi", "stop", "tile", "hiss", "shed", "hahn", "baku", "ahas", "sill", "swap", "also", "carr", "manx", "lime", "debs", "moat", "eked", "bola", "pods", "coon", "lacy", "tube", "minx", "buff", "pres", "clew", "gaff", "flee", "burn", "whom", "cola", "fret", "purl", "wick", "wigs", "donn", "guys", "toni", "oxen", "wite", "vial", "spam", "huts", "vats", "lima", "core", "eula", "thad", "peon", "erie", "oats", "boyd", "cued", "olaf", "tams", "secs", "urey", "wile", "penn", "bred", "rill", "vary", "sues", "mail", "feds", "aves", "code", "beam", "reed", "neil", "hark", "pols", "gris", "gods", "mesa", "test", "coup", "heed", "dora", "hied", "tune", "doze", "pews", "oaks", "bloc", "tips", "maid", "goof", "four", "woof", "silo", "bray", "zest", "kiss", "yong", "file", "hilt", "iris", "tuns", "lily", "ears", "pant", "jury", "taft", "data", "gild", "pick", "kook", "colt", "bohr", "anal", "asps", "babe", "bach", "mash", "biko", "bowl", "huey", "jilt", "goes", "guff", "bend", "nike", "tami", "gosh", "tike", "gees", "urge", "path", "bony", "jude", "lynn", "lois", "teas", "dunn", "elul", "bonn", "moms", "bugs", "slay", "yeah", "loan", "hulk", "lows", "damn", "nell", "jung", "avis", "mane", "waco", "loin", "knob", "tyke", "anna", "hire", "luau", "tidy", "nuns", "pots", "quid", "exec", "hans", "hera", "hush", "shag", "scot", "moan", "wald", "ursa", "lorn", "hunk", "loft", "yore", "alum", "mows", "slog", "emma", "spud", "rice", "worn", "erma", "need", "bags", "lark", "kirk", "pooh", "dyes", "area", "dime", "luvs", "foch", "refs", "cast", "alit", "tugs", "even", "role", "toed", "caph", "nigh", "sony", "bide", "robs", "folk", "daft", "past", "blue", "flaw", "sana", "fits", "barr", "riot", "dots", "lamp", "cock", "fibs", "harp", "tent", "hate", "mali", "togs", "gear", "tues", "bass", "pros", "numb", "emus", "hare", "fate", "wife", "mean", "pink", "dune", "ares", "dine", "oily", "tony", "czar", "spay", "push", "glum", "till", "moth", "glue", "dive", "scad", "pops", "woks", "andy", "leah", "cusp", "hair", "alex", "vibe", "bulb", "boll", "firm", "joys", "tara", "cole", "levy", "owen", "chow", "rump", "jail", "lapp", "beet", "slap", "kith", "more", "maps", "bond", "hick", "opus", "rust", "wist", "shat", "phil", "snow", "lott", "lora", "cary", "mote", "rift", "oust", "klee", "goad", "pith", "heep", "lupe", "ivan", "mimi", "bald", "fuse", "cuts", "lens", "leer", "eyry", "know", "razz", "tare", "pals", "geek", "greg", "teen", "clef", "wags", "weal", "each", "haft", "nova", "waif", "rate", "katy", "yale", "dale", "leas", "axum", "quiz", "pawn", "fend", "capt", "laws", "city", "chad", "coal", "nail", "zaps", "sort", "loci", "less", "spur", "note", "foes", "fags", "gulp", "snap", "bogs", "wrap", "dane", "melt", "ease", "felt", "shea", "calm", "star", "swam", "aery", "year", "plan", "odin", "curd", "mira", "mops", "shit", "davy", "apes", "inky", "hues", "lome", "bits", "vila", "show", "best", "mice", "gins", "next", "roan", "ymir", "mars", "oman", "wild", "heal", "plus", "erin", "rave", "robe", "fast", "hutu", "aver", "jodi", "alms", "yams", "zero", "revs", "wean", "chic", "self", "jeep", "jobs", "waxy", "duel", "seek", "spot", "raps", "pimp", "adan", "slam", "tool", "morn", "futz", "ewes", "errs", "knit", "rung", "kans", "muff", "huhs", "tows", "lest", "meal", "azov", "gnus", "agar", "sips", "sway", "otis", "tone", "tate", "epic", "trio", "tics", "fade", "lear", "owns", "robt", "weds", "five", "lyon", "terr", "arno", "mama", "grey", "disk", "sept", "sire", "bart", "saps", "whoa", "turk", "stow", "pyle", "joni", "zinc", "negs", "task", "leif", "ribs", "malt", "nine", "bunt", "grin", "dona", "nope", "hams", "some", "molt", "smit", "sacs", "joan", "slav", "lady", "base", "heck", "list", "take", "herd", "will", "nubs", "burg", "hugs", "peru", "coif", "zoos", "nick", "idol", "levi", "grub", "roth", "adam", "elma", "tags", "tote", "yaws", "cali", "mete", "lula", "cubs", "prim", "luna", "jolt", "span", "pita", "dodo", "puss", "deer", "term", "dolt", "goon", "gary", "yarn", "aims", "just", "rena", "tine", "cyst", "meld", "loki", "wong", "were", "hung", "maze", "arid", "cars", "wolf", "marx", "faye", "eave", "raga", "flow", "neal", "lone", "anne", "cage", "tied", "tilt", "soto", "opel", "date", "buns", "dorm", "kane", "akin", "ewer", "drab", "thai", "jeer", "grad", "berm", "rods", "saki", "grus", "vast", "late", "lint", "mule", "risk", "labs", "snit", "gala", "find", "spin", "ired", "slot", "oafs", "lies", "mews", "wino", "milk", "bout", "onus", "tram", "jaws", "peas", "cleo", "seat", "gums", "cold", "vang", "dewy", "hood", "rush", "mack", "yuan", "odes", "boos", "jami", "mare", "plot", "swab", "borg", "hays", "form", "mesh", "mani", "fife", "good", "gram", "lion", "myna", "moor", "skin", "posh", "burr", "rime", "done", "ruts", "pays", "stem", "ting", "arty", "slag", "iron", "ayes", "stub", "oral", "gets", "chid", "yens", "snub", "ages", "wide", "bail", "verb", "lamb", "bomb", "army", "yoke", "gels", "tits", "bork", "mils", "nary", "barn", "hype", "odom", "avon", "hewn", "rios", "cams", "tact", "boss", "oleo", "duke", "eris", "gwen", "elms", "deon", "sims", "quit", "nest", "font", "dues", "yeas", "zeta", "bevy", "gent", "torn", "cups", "worm", "baum", "axon", "purr", "vise", "grew", "govs", "meat", "chef", "rest", "lame"] | 11
    }

    def "136. Single Number"(int[] nums, int ans) {
        given:
        def solution = new Problem136()
        expect:
        solution.singleNumber(nums) == ans
        solution.reduce(nums) == ans
        where:
        nums            | ans
        [0]             | 0
        [2, 2, 1]       | 1
        [4, 1, 2, 1, 2] | 4
    }

    def "152. Maximum Product Subarray"(int[] nums, int ans) {
        given:
        def sol = new Problem152()
        expect:
        sol.maxProduct(nums) == ans
        where:
        nums          | ans
        [0, 2]        | 2
        [2, 3, -2, 4] | 6
        [-2, 0, -1]   | 0
    }

    def "159. Longest Substring with At Most Two Distinct Characters"(String s, int ans) {
        given:
        def sol = new Problem159()
        expect:
        sol.lengthOfLongestSubstringTwoDistinct(s) == ans
        where:
        s          | ans
        "eceba"    | 3
        "ccaabbb"  | 5
        "aaaaa"    | 5
        "abababab" | 8
        "abaccc"   | 4
    }

    def "167. Two Sum II - Input array is sorted"(int[] nums, int target, int[] ans) {
        given:
        def sol = new Problem167()
        expect:
        sol.twoSum(nums, target) == ans
        where:
        nums           | target | ans
        [2, 7, 11, 15] | 9      | [1, 2]
    }

    def "179. Largest Number"(int[] nums, String ans) {
        given:
        def sol = new Problem179()
        expect:
        sol.largestNumber(nums) == ans
        where:
        nums              | ans
        [10, 2]           | "210"
        [3, 30, 34, 5, 9] | "9534330"
        [0, 0, 0]         | "0"
        [10]              | "10"
    }

    def "206. Reverse Linked List"(int[] input, int[] output) {
        given:
        def sol = new Problem206()
        expect:
        ListNode node = sol.reverseList(Converter.convertListNode(input))
        Converter.convertArray(node) == output
        where:
        input           | output
        [1, 2, 3, 4, 5] | [5, 4, 3, 2, 1]
        [1]             | [1]
    }

    def "208. Implement Trie (Prefix Tree)"() {
        given:
        Problem208.Trie trie = new Problem208.Trie()
        trie.insert("apple")
        Assert.that(trie.search("apple"))
        Assert.that(!trie.search("app"))
        Assert.that(trie.startsWith("app"))
        trie.insert("app")
        Assert.that(trie.search("app"))
    }

    def "213. House Robber II"(int[] nums, int ans) {
        given:
        def sol = new Problem213()
        expect:
        sol.rob(nums) == ans
        where:
        nums         | ans
        [2, 3, 2]    | 3
        [1, 2, 3, 1] | 4
        [1, 2, 1, 1] | 3
        [1, 2]       | 2
    }

    def "216. Combination Sum III"(int k, int n, List<List<Integer>> expect) {
        given:
        def solution = new Problem216()
        expect:
        solution.combinationSum3(k, n) == expect
        where:
        k | n  || expect
        2 | 6  || [[1, 5], [2, 4]]
        3 | 7  || [[1, 2, 4]]
        3 | 9  || [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        5 | 18 || [[1, 2, 3, 4, 8], [1, 2, 3, 5, 7], [1, 2, 4, 5, 6]]
    }

    def "221. Maximal Square"(char[][] matrix, int ans) {
        given:
        def sol = new Problem221()
        expect:
        sol.maximalSquare(matrix) == ans
        where:
        matrix                                  | ans
        [
                ["1", "0", "1", "1", "0", "1"],
                ["1", "1", "1", "1", "1", "1"],
                ["0", "1", "1", "0", "1", "1"],
                ["1", "1", "1", "0", "1", "0"],
                ["0", "1", "1", "1", "1", "1"],
                ["1", "1", "0", "1", "1", "1"]
        ]                                       | 4
    }

    def '254. Factor Combinations'(int n, List<List<Integer>> ans) {
        given:
        def sol = new Problem254()
        expect:
        sol.getFactors(n) == ans
        where:
        n        | ans
        1        | []
        12       | [[2, 2, 3], [2, 6], [3, 4]]
        32       | [[2, 2, 2, 2, 2], [2, 2, 2, 4], [2, 2, 8], [2, 4, 4], [2, 16], [4, 8]]
        23848713 | [[3, 3, 7, 378551], [3, 3, 2649857], [3, 7, 1135653], [3, 21, 378551], [3, 7949571], [7, 9, 378551], [7, 3406959], [9, 2649857], [21, 1135653], [63, 378551]]
    }

    def '264. Ugly Number II'(int n, int ans) {
        given:
        def sol = new Problem264()
        expect:
        sol.nthUglyNumber(n) == ans
        sol.nthUglyNumber2(n) == ans
        where:
        n    | ans
        1    | 1
        10   | 12
        1690 | 2123366400
    }

    def "279. Perfect Squares"(int n, int ans) {
        given:
        def sol = new Problem279()
        expect:
        sol.numSquares(n) == ans
        sol.numSquares2(n) == ans
        where:
        n      | ans
        1      | 1
        12     | 3
        13     | 2
        9999   | 4
        999999 | 4
    }

    def "283. Move Zeroes"(int[] nums, int[] ans) {
        given:
        def sol = new Problem283()
        sol.moveZeroes(nums)
        expect:
        nums == ans
        where:
        nums             | ans
        [0, 1, 0, 3, 12] | [1, 3, 12, 0, 0]
        [0, 0, 1, 3, 12] | [1, 3, 12, 0, 0]
    }

    def "300. Longest Increasing Subsequence"(int[] nums, int ans) {
        given:
        def sol = new Problem300()
        expect:
        sol.lengthOfLIS(nums) == ans
        where:
        nums                         | ans
        [10, 9, 2, 5, 3, 7, 101, 18] | 4
    }

    def "304. Range Sum Query 2D - Immutable"(int[][] nums, int ans) {
        given:
        def numMatrix = new Problem304.NumMatrix(nums)
        expect:
        numMatrix.sumRegion(2, 1, 4, 3) == ans
        where:
        nums                                                                                  | ans
        [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]] | 8
    }

    def "312. Burst Balloons"(int[] nums, int ans) {
        given:
        def sol = new Problem312()
        expect:
        sol.maxCoins(nums) == ans
        where:
        nums         | ans
        [3, 1, 5, 8] | 167
        [1, 3, 5, 8] | 160
    }

    def "315. Count of Smaller Numbers After Self"(int[] nums, int[] ans) {
        given:
        def sol = new Problem315()
        expect:
        Converter.collToArr(sol.countSmaller(nums)) == ans
        where:
        nums         | ans
        [5, 2, 6, 1] | [2, 1, 1, 0]
    }

    def "329. Longest Increasing Path in a Matrix"(int[][] matrix, int ans) {
        given:
        def sol = new Problem329()
        expect:
        sol.longestIncreasingPath(matrix) == ans
        where:
        matrix      | ans
        [[9, 9, 4],
         [6, 6, 8],
         [2, 1, 1]] | 4
        [[3, 4, 5],
         [3, 2, 6],
         [2, 2, 1]] | 4
        []          | 0
        [[]]        | 0
    }

    def "350. Intersection of Two Arrays II"(int[] nums1, int[] nums2, int[] ans) {
        given:
        def sol = new Problem350()
        expect:
        sol.intersect(nums1, nums2) == ans
        sol.intersect1(nums1, nums2) == ans
        where:
        nums1        | nums2  | ans
        [2, 1]       | [1, 2] | [1, 2]
        [1, 2, 2, 1] | [2, 2] | [2, 2]
    }

    def "392. Is Subsequence"(String s, String t, boolean ans) {
        given:
        def sol = new Problem392()
        expect:
        sol.isSubsequence(s, t) == ans
        where:
        s     | t        | ans
        "abc" | "ahbgdc" | true
        "axc" | "ahbgdc" | false
        "acb" | "ahbgdc" | false
    }

    def '403. Frog Jump'(int[] stones, boolean ans) {
        given:
        def sol = new Problem403()
        expect:
        sol.canCross(stones) == ans
        sol.canCross2(stones) == ans
        where:
        stones                     | ans
        [0, 1, 3, 5, 6, 8, 12, 17] | true
        [0, 1, 2, 3, 4, 8, 9, 11]  | false
    }

    def "406. Queue Reconstruction by Height"(int[][] people, int[][] ans) {
        given:
        def sol = new Problem406()
        expect:
        sol.reconstructQueue(people) == ans
        where:
        people                                           | ans
        [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]] | [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    }

    def "446. Arithmetic Slices II - Subsequence"(int[] nums, int ans) {
        given:
        def sol = new Problem446()
        expect:
        sol.numberOfArithmeticSlices(nums) == ans
        where:
        nums                                                                     | ans
        [2, 4, 6, 8, 10]                                                         | 7
        [1, 2, 3, 4, 4, 4]                                                       | 8
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] | 16776915
    }

    def "452. Minimum Number of Arrows to Burst Balloons"(int[][] points, int ans) {
        given:
        def sol = new Problem452()
        expect:
        sol.findMinArrowShots(points) == ans
        where:
        points                              | ans
        [[10, 16], [2, 8], [1, 6], [7, 12]] | 2
        [[1, 2], [3, 4], [5, 6], [7, 8]]    | 4
        [[1, 2], [2, 3], [3, 4], [4, 5]]    | 2
        []                                  | 0
        [[1, 2]]                            | 1
        [[2, 3], [2, 3]]                    | 1
    }

    def "494. Target Sum"(int[] nums, int s, int expect) {
        given:
        def solution = new Problem494()
        expect:
        solution.findTargetSumWays1(nums, s) == expect
        solution.findTargetSumWays2(nums, s) == expect
        solution.findTargetSumWays3(nums, s) == expect
        where:
        nums                                                                         | s  | expect
        [1, 1, 1, 1, 1]                                                              | 3  | 5
        [27, 22, 39, 22, 40, 32, 44, 45, 46, 8, 8, 21, 27, 8, 11, 29, 16, 15, 41, 0] | 10 | 0
        [19, 32, 36, 7, 37, 10, 44, 21, 40, 39, 39, 18, 5, 34, 3, 40, 33, 2, 46, 46] | 29 | 5715
    }

    def "560. Subarray Sum Equals K"(int[] nums, int k, int ans) {
        given:
        def sol = new Problem560()
        expect:
        sol.subarraySum(nums, k) == ans
        where:
        nums        | k | ans
        [1, 1, 1]   | 2 | 2
        [1] * 20000 | 1 | 20000
    }

    def "576. Out of Boundary Paths"(int m, int n, int maxMove, int startRow, int startColumn, int ans) {
        given:
        def sol = new Problem576()
        expect:
        sol.findPaths(m, n, maxMove, startRow, startColumn) == ans
        sol.findPaths2(m, n, maxMove, startRow, startColumn) == ans
        where:
        m | n  | maxMove | startRow | startColumn | ans
        2 | 2  | 2       | 0        | 0           | 6
        1 | 3  | 3       | 0        | 1           | 12
        4 | 5  | 8       | 3        | 2           | 3875
        8 | 50 | 23      | 5        | 26          | 914783380
    }

    def "581. Shortest Unsorted Continuous Subarray"(int[] nums, int ans) {
        given:
        def sol = new Problem581()
        expect:
        sol.findUnsortedSubarray(nums) == ans
        where:
        nums                     | ans
        [2, 6, 4, 8, 10, 9, 15]  | 5
        [1, 2, 3, 4]             | 0
        [2, 6, 4]                | 2
        [1]                      | 0
        [5, 3, 9, 1, 7, 3, 2, 5] | 8
        [1, 3, 5, 2]             | 3
    }

    def "583. Delete Operation for Two Strings"(String word1, String word2, int ans) {
        given:
        def sol = new Problem583()
        expect:
        sol.minDistance(word1, word2) == ans
        where:
        word1      | word2  | ans
        "sea"      | "eat"  | 2
        "leetcode" | "etco" | 4
    }

    def "605. Can Place Flowers"(int[] flowerbed, int n, boolean ans) {
        given:
        def sol = new Problem605()
        expect:
        sol.canPlaceFlowers(flowerbed, n) == ans
        where:
        flowerbed          | n | ans
        [1, 0, 0, 0, 0, 1] | 2 | false
        [1, 0, 0, 0, 1]    | 2 | false
        [0, 0]             | 2 | false
        [0, 0, 0, 0, 1]    | 2 | true
    }

    def "611. Valid Triangle Number"(int[] nums, int ans) {
        given:
        def sol = new Problem611()
        expect:
        sol.triangleNumber(nums) == ans
        where:
        nums         | ans
        [2, 2, 3, 4] | 3
        [1, 1, 3, 4] | 0
    }

    def "649. Dota2 Senate"(String senate, String ans) {
        given:
        def sol = new Problem649()
        expect:
        sol.predictPartyVictory(senate) == ans
        where:
        senate                            | ans
        "RD"                              | "Radiant"
        "RDD"                             | "Dire"
        "DRRDRDRDRDDRDRDR"                | "Radiant"
        "RRDRDDRRRDDRDRRDRDRRDDRRDRDRRDD" | "Radiant"
    }

    def "668. Kth Smallest Number in Multiplication Table"(int m, int n, int k, int ans) {
        given:
        def sol = new Problem668()
        expect:
        sol.findKthNumber(m, n, k) == ans
        where:
        m    | n     | k         | ans
        9895 | 28405 | 100787757 | 31666344
    }

    def "773. Sliding Puzzle"(int[][] board, int ans) {
        given:
        def sol = new Problem773()
        expect:
        sol.slidingPuzzle(board) == ans
        where:
        board                  | ans
        [[1, 2, 3], [4, 5, 0]] | 0
        [[1, 2, 3], [4, 0, 5]] | 1
        [[1, 2, 3], [5, 4, 0]] | -1
        [[4, 1, 2], [5, 0, 3]] | 5
        [[3, 2, 4], [1, 5, 0]] | 14
    }

    def "785. Is Graph Bipartite"(int[][] graph, boolean ans) {
        given:
        def sol = new Problem785()
        expect:
        sol.isBipartite(graph) == ans
        where:
        graph                                  | ans
        [[]]                                   | true
        [[1, 3], [0, 2], [1, 3], [0, 2]]       | true
        [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]] | false
    }

    def "791. Custom Sort String"(String s, String t, String ans) {
        given:
        def solution = new Problem791()
        expect:
        solution.customSortString(s, t) == ans
        where:
        s      | t       | ans
        "cba"  | "abcd"  | "cbad"
        "abc"  | "badef" | "abdef"
        ""     | "abc"   | "abc"
        "def"  | "cba"   | "cba"
        "kqep" | "pekeq" | "kqeep"
    }

    def "815. Bus Routes"(int[][] routes, int source, int target, int ans) {
        given:
        def sol = new Problem815()
        expect:
        sol.numBusesToDestination(routes, source, target) == ans
        where:
        routes                                            | source | target | ans
        [[1, 2, 7], [3, 6, 7]]                            | 1      | 6      | 2
        [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]] | 15     | 12     | -1
    }

    def "847. Shortest Path Visiting All Nodes"(int[][] graph, int ans) {
        given:
        def sol = new Problem847()
        expect:
//        sol.shortestPathLength(graph) == ans
        where:
        graph                                    | ans
        [[1, 2, 3], [0], [0], [0]]               | 4
        [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]] | 4
    }

    def "849. Maximize Distance to Closest Person"(int[] seats, int ans) {
        given:
        def sol = new Problem849()
        expect:
        sol.maxDistToClosest(seats) == ans
        where:
        seats                 | ans
        [1, 0, 0, 0, 1, 0, 1] | 2
        [1, 0, 0, 0]          | 3
        [0, 0, 0, 1]          | 3
        [0, 0, 1, 0, 1, 1]    | 2
        [0, 1]                | 1
    }

    def "864. Shortest Path to Get All Keys"(String[] grid, int ans) {
        given:
        def sol = new Problem864()
        expect:
        sol.shortestPathAllKeys(grid) == ans
        where:
        grid                        | ans
        ["@.a.#", "###.#", "b.A.B"] | 8
    }

    def "909. Snakes and Ladders"(int[][] board, int ans) {
        given:
        def sol = new Problem909()
        expect:
        sol.snakesAndLadders(board) == ans
        where:
        board                      | ans
        [[-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 15, -1, -1, -1, -1]] | 4
    }

    def "941. Valid Mountain Array"(int[] nums, boolean ans) {
        given:
        def sol = new Problem941()
        expect:
        sol.validMountainArray(nums) == ans
        sol.validMountainArray1(nums) == ans
        where:
        nums         | ans
        [1, 2]       | false
        [1, 2, 3]    | false
        [3, 2, 1]    | false
        [3, 5, 5]    | false
        [0, 3, 2, 1] | true
    }

    def "946. Validate Stack Sequences"(int[] pushed, int[] popped, boolean ans) {
        given:
        def solution = new Problem946()
        expect:
        solution.validateStackSequences(pushed, popped) == ans
        solution.ans(pushed, popped) == ans
        where:
        pushed          | popped          | ans
        []              | []              | true
        [1, 2]          | [1, 2, 3]       | false
        [2, 1, 0]       | [1, 2, 0]       | true
        [1, 2, 3, 4, 5] | [4, 5, 3, 2, 1] | true
        [1, 2, 3, 4, 5] | [4, 3, 5, 1, 2] | false
        [2, 3, 0, 1]    | [0, 3, 2, 1]    | true
    }

    def "961. N-Repeated Element in Size 2N Array"(int[] arr, int ans) {
        given:
        def solution = new Problem961()
        expect:
        solution.repeatedNTimes(arr) == ans
        where:
        arr                      | ans
        [1, 2, 3, 3]             | 3
        [2, 1, 2, 5, 3, 2]       | 2
        [5, 1, 5, 2, 5, 3, 5, 4] | 5
    }

    def "962. Maximum Width Ramp"(int[] arr, int ans) {
        given:
        def solution = new Problem962()
        expect:
        solution.maxWidthRamp(arr) == ans
        where:
        arr                            | ans
        [6, 0, 8, 2, 1, 5]             | 4
        [9, 8, 1, 0, 1, 9, 4, 0, 4, 1] | 7
    }

    def "963. Minimum Area Rectangle II"(int[][] points, double ans) {
        given:
        def solution = new Problem963()
        expect:
        solution.minAreaFreeRect(points) == ans
        where:
        points                                   | ans
        [[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]] | 0.0
        [[1, 2], [2, 1], [1, 0], [0, 1]]         | 2.0
        [[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]] | 1.0
    }

    def "964. Least Operators to Express Number"(int x, int target, int ans) {
        given:
        def solution = new Problem964()
        expect:
        solution.leastOpsExpressTarget(x, target) == ans
        where:
        x   | target    | ans
        3   | 19        | 5
        5   | 501       | 8
        100 | 200000000 | 7
    }

    def "967. Numbers With Same Consecutive Differences"(int n, int k, int[] ans) {
        given:
        def solution = new Problem967()
        expect:
        solution.numsSameConsecDiff(n, k) == ans
        where:
        n | k || ans
        1 | 0 || [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        1 | 9 || [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        3 | 7 || [181, 292, 707, 818, 929]
        2 | 1 || [12, 10, 23, 21, 34, 32, 45, 43, 56, 54, 67, 65, 78, 76, 89, 87, 98]
    }

    def "969. Pancake Sorting"(int[] nums, Integer[] res) {
        given:
        def solution = new Problem969()
        expect:
        Converter.collToArr(solution.pancakeSort(nums)) == res
        where:
        nums         | res
        [3, 2, 4, 1] | [3, 4, 2, 3, 2]
        [1, 2, 3]    | []
    }

    def "973. K Closest Points to Origin"(int[][] points, int k, int[][] ans) {
        given:
        def sol = new Problem973()
        expect:
        sol.kClosest(points, k) == ans
        where:
        points                     | k | ans
        [[1, 3], [-2, 2]]          | 1 | [[-2, 2]]
        [[0, 1], [1, 0]]           | 2 | [[0, 1], [1, 0]]
        [[3, 3], [5, -1], [-2, 4]] | 2 | [[3, 3], [-2, 4]]
    }

    def "974. Subarray Sums Divisible by K"(int[] A, int K, int res) {
        given:
        def solution = new Problem974()
        expect:
        solution.subarraysDivByK(A, K) == res
        where:
        A                    | K | res
        [1, 2, 3, 4, 5]      | 5 | 4
        [4, 5, 0, -2, -3, 1] | 5 | 7
    }

    def "976. Largest Perimeter Triangle"(int[] A, int res) {
        given:
        def solution = new Problem976()
        expect:
        solution.largestPerimeter(A) == res
        where:
        A            | res
        [2, 1, 2]    | 5
        [1, 2, 1]    | 0
        [3, 2, 3, 4] | 10
        [3, 6, 2, 3] | 8
    }

    def "977. Squares of a Sorted Array"(int[] A, int[] res) {
        given:
        def solution = new Problem977()
        expect:
        solution.sortedSquares2(A) == res
        where:
        A                  | res
        [-4, -1, 0, 3, 10] | [0, 1, 9, 16, 100]
        [-7, -3, 2, 3, 11] | [4, 9, 9, 49, 121]
    }

    def "978. Longest Turbulent Subarray"(int[] arr, int ans) {
        given:
        def sol = new Problem978()
        expect:
        sol.maxTurbulenceSize(arr) == ans
        where:
        arr                          | ans
        [9, 4, 2, 10, 7, 8, 8, 1, 9] | 5
        [4, 8, 12, 16]               | 2
        [1]                          | 1
        [1, 1, 1]                    | 1
    }

    def "979. Distribute Coins in Binary Tree"(TreeNode root, int res) {
        given:
        def solution = new Problem979()
        expect:
        solution.distributeCoins(root) == res
        where:
        root | res
        null | 0
    }

    def "980. Unique Paths III"(int[][] grid, int res) {
        given:
        def solution = new Problem980()
        expect:
        solution.uniquePathsIII(grid) == res
        where:
        grid                                        | res
        [[1, 2], [0, 0]]                            | 1
        [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]] | 2
        [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]  | 4
    }

    def "982. Triples with Bitwise AND Equal To Zero"(int[] nums, int res) {
        given:
        def solution = new Problem982()
        expect:
        solution.countTriplets(nums) == res
        where:
        nums      | res
        [2, 1, 3] | 12
    }

    def "983. Minimum Cost For Tickets"(int[] days, int[] costs, int res) {
        given:
        def solution = new Problem983()
        expect:
        solution.mincostTickets(days, costs) == res
        where:
        days                                    | costs      | res
        [1, 4, 6, 7, 8, 20]                     | [2, 7, 15] | 11
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31] | [2, 7, 15] | 17
    }

    def "984. String Without AAA or BBB"(int A, int B, String res) {
        given:
        def solution = new Problem984()
        expect:
        solution.strWithout3a3b(A, B) == res
        where:
        A | B || res
        1 | 1 || "ab"
        1 | 2 || "bba"
        4 | 1 || "aabaa"
    }

    def "1001. Grid Illumination"(int n, int[][] lamps, int[][] queries, int[] ans) {
        given:
        def sol = new Problem1001()
        expect:
        sol.gridIllumination(n, lamps, queries) == ans
        where:
        n | lamps            | queries          | ans
//        5 | [[0, 0], [4, 4]] | [[1, 1], [1, 0]]         | [1, 0]
//        5 | [[0, 0], [4, 4]] | [[1, 1], [1, 1]]         | [1, 1]
//        5 | [[0, 0], [0, 4]] | [[0, 4], [0, 1], [1, 4]] | [1, 1, 0]
        5 | [[0, 0], [1, 0]] | [[1, 1], [1, 1]] | [1, 0]
    }

    def "1014. Best Sightseeing Pair"(int[] arr, int result) {
        given:
        def sol = new Problem1014()
        expect:
        sol.maxScoreSightseeingPair(arr) == result
        where:
        arr             | result
        [1, 2]          | 2
        [5, 3, 1]       | 7
        [8, 1, 5, 2, 6] | 11
    }

    def "1202. Smallest String With Swaps"(String s, List<List<Integer>> pairs, String ans) {
        given:
        def sol = new Problem1202()
        expect:
        sol.smallestStringWithSwaps(s, pairs) == ans
        where:
        s      | pairs                    | ans
        "dcab" | [[0, 3], [1, 2]]         | "bacd"
        "dcab" | [[0, 3], [1, 2], [0, 2]] | "abcd"
        "cba"  | [[0, 1], [1, 2]]         | "abc"
    }

    def "1207. Unique Number of Occurrences"(int[] arr, boolean ans) {
        given:
        def sol = new Problem1207()
        expect:
        sol.uniqueOccurrences(arr) == ans
        where:
        arr                                | ans
        [1, 2, 2, 1, 1, 3]                 | true
        [1, 2]                             | false
        [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0] | true
    }

    def "1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance"(int n, int[][] edges, int distanceThreshold, int ans) {
        given:
        def p = new Problem1334()
        expect:
        p.findTheCity(n, edges, distanceThreshold) == ans
        where:
        n | edges                                                                | distanceThreshold | ans
        5 | [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]   | 2                 | 0
        6 | [[0, 1, 10], [0, 2, 1], [2, 3, 1], [1, 3, 1], [1, 4, 1], [4, 5, 10]] | 20                | 5
    }

    def "1631. Path With Minimum Effort"(int[][] heights, int ans) {
        given:
        def sol = new Problem1631()
        expect:
        sol.minimumEffortPath(heights) == ans
        where:
        heights                                                                               | ans
        [[1, 2, 2], [3, 8, 2], [5, 3, 5]]                                                     | 2
        [[1, 2, 3], [3, 8, 4], [5, 3, 5]]                                                     | 1
        [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]] | 0
    }

    def "2156. Find Substring With Given Hash Value"(String s, int power, int modulo, int k, int hashValue, String ans) {
        given:
        def sol = new Problem2156()
        expect:
        sol.subStrHash(s, power, modulo, k, hashValue) == ans
        where:
        s                                                           | power | modulo | k  | hashValue | ans
        "xqgfatvtlwnnkxipmipcpqwbxihxblaplpfckvxtihonijhtezdnkjmmk" | 22    | 51     | 41 | 9         | "xqgfatvtlwnnkxipmipcpqwbxihxblaplpfckvxti"
    }
}
