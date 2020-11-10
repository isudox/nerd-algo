"""126. Word Ladder II
https://leetcode.com/problems/word-ladder-ii/

Given two words (beginWord and endWord), and a dictionary's word list,
find `all shortest` transformation sequence(s) from beginWord to endWord,
such that:

    Only one letter can be changed at a time
    Each transformed word must exist in the word list.
    Note that beginWord is not a transformed word.

Note:

    Return an empty list if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
from typing import List


class Solution:
    def find_ladders(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        # TODO
        def combine(p1: List[str], p2: List[str]) -> List[str]:
            if begin_word not in p1:
                return combine(p2, p1)
            p1.extend(p2)
            return p1

        def bfs(p1: List[str], p2: List[str], q1: List[str], q2: List[str]):
            nonlocal min_size
            cur_size = len(p1) + len(p2)
            if cur_size >= min_size:
                return
            if len(q1) > len(q2):
                return bfs(p2, p1, q2, q1)
            for i in range(len(q1)):
                cur_word = q1.pop(0)
                for j in range(word_len):
                    for k in range(26):
                        char = chr(ord('a') + k)
                        if char != cur_word[j]:
                            new_word = cur_word[:j] + char + cur_word[j + 1:]
                            if new_word in q2:
                                new_p1 = p1[:]
                                new_p1.append(end_word)
                                cur_size += 1
                                if cur_size < min_size:
                                    del paths[min_size]
                                    min_size = cur_size
                                    paths[min_size] = [combine(new_p1, p2)]
                                elif cur_size == min_size:
                                    paths[min_size].append(combine(new_p1, p2))
                            elif new_word in word_set and cur_size + 1 < min_size:
                                new_p1 = p1[:]
                                new_p1.append(new_word)
                                word_set.remove(new_word)
                                new_q1 = q1[:]
                                new_q1.append(new_word)
                                bfs(new_p1, p2, new_q1, q2)
                                word_set.add(new_word)

        word_set = set(word_list)
        if end_word not in word_set:
            return []
        word_len = len(end_word)
        min_size = len(word_list) + 1
        paths = {min_size: []}
        bfs([begin_word], [end_word], [begin_word], [end_word])
        return paths[min_size]


if __name__ == '__main__':
    sol = Solution()
    res = sol.find_ladders("cet", "ism",
                           ["kid", "tag", "pup", "ail", "tun", "woo", "erg", "luz", "brr", "gay",
                            "sip", "kay", "per", "val", "mes", "ohs", "now", "boa", "cet", "pal",
                            "bar", "die", "war", "hay", "eco", "pub", "lob", "rue", "fry", "lit",
                            "rex", "jan", "cot", "bid", "ali", "pay", "col", "gum", "ger", "row",
                            "won", "dan", "rum", "fad", "tut", "sag", "yip", "sui", "ark", "has",
                            "zip", "fez", "own", "ump", "dis", "ads", "max", "jaw", "out", "btu",
                            "ana", "gap", "cry", "led", "abe", "box", "ore", "pig", "fie", "toy",
                            "fat", "cal", "lie", "noh", "sew", "ono", "tam", "flu", "mgm", "ply",
                            "awe", "pry", "tit", "tie", "yet", "too", "tax", "jim", "san", "pan",
                            "map", "ski", "ova", "wed", "non", "wac", "nut", "why", "bye", "lye",
                            "oct", "old", "fin", "feb", "chi", "sap", "owl", "log", "tod", "dot",
                            "bow", "fob", "for", "joe", "ivy", "fan", "age", "fax", "hip", "jib",
                            "mel", "hus", "sob", "ifs", "tab", "ara", "dab", "jag", "jar", "arm",
                            "lot", "tom", "sax", "tex", "yum", "pei", "wen", "wry", "ire", "irk",
                            "far", "mew", "wit", "doe", "gas", "rte", "ian", "pot", "ask", "wag",
                            "hag", "amy", "nag", "ron", "soy", "gin", "don", "tug", "fay", "vic",
                            "boo", "nam", "ave", "buy", "sop", "but", "orb", "fen", "paw", "his",
                            "sub", "bob", "yea", "oft", "inn", "rod", "yam", "pew", "web", "hod",
                            "hun", "gyp", "wei", "wis", "rob", "gad", "pie", "mon", "dog", "bib",
                            "rub", "ere", "dig", "era", "cat", "fox", "bee", "mod", "day", "apr",
                            "vie", "nev", "jam", "pam", "new", "aye", "ani", "and", "ibm", "yap",
                            "can", "pyx", "tar", "kin", "fog", "hum", "pip", "cup", "dye", "lyx",
                            "jog", "nun", "par", "wan", "fey", "bus", "oak", "bad", "ats", "set",
                            "qom", "vat", "eat", "pus", "rev", "axe", "ion", "six", "ila", "lao",
                            "mom", "mas", "pro", "few", "opt", "poe", "art", "ash", "oar", "cap",
                            "lop", "may", "shy", "rid", "bat", "sum", "rim", "fee", "bmw", "sky",
                            "maj", "hue", "thy", "ava", "rap", "den", "fla", "auk", "cox", "ibo",
                            "hey", "saw", "vim", "sec", "ltd", "you", "its", "tat", "dew", "eva",
                            "tog", "ram", "let", "see", "zit", "maw", "nix", "ate", "gig", "rep",
                            "owe", "ind", "hog", "eve", "sam", "zoo", "any", "dow", "cod", "bed",
                            "vet", "ham", "sis", "hex", "via", "fir", "nod", "mao", "aug", "mum",
                            "hoe", "bah", "hal", "keg", "hew", "zed", "tow", "gog", "ass", "dem",
                            "who", "bet", "gos", "son", "ear", "spy", "kit", "boy", "due", "sen",
                            "oaf", "mix", "hep", "fur", "ada", "bin", "nil", "mia", "ewe", "hit",
                            "fix", "sad", "rib", "eye", "hop", "haw", "wax", "mid", "tad", "ken",
                            "wad", "rye", "pap", "bog", "gut", "ito", "woe", "our", "ado", "sin",
                            "mad", "ray", "hon", "roy", "dip", "hen", "iva", "lug", "asp", "hui",
                            "yak", "bay", "poi", "yep", "bun", "try", "lad", "elm", "nat", "wyo",
                            "gym", "dug", "toe", "dee", "wig", "sly", "rip", "geo", "cog", "pas",
                            "zen", "odd", "nan", "lay", "pod", "fit", "hem", "joy", "bum", "rio",
                            "yon", "dec", "leg", "put", "sue", "dim", "pet", "yaw", "nub", "bit",
                            "bur", "sid", "sun", "oil", "red", "doc", "moe", "caw", "eel", "dix",
                            "cub", "end", "gem", "off", "yew", "hug", "pop", "tub", "sgt", "lid",
                            "pun", "ton", "sol", "din", "yup", "jab", "pea", "bug", "gag", "mil",
                            "jig", "hub", "low", "did", "tin", "get", "gte", "sox", "lei", "mig",
                            "fig", "lon", "use", "ban", "flo", "nov", "jut", "bag", "mir", "sty",
                            "lap", "two", "ins", "con", "ant", "net", "tux", "ode", "stu", "mug",
                            "cad", "nap", "gun", "fop", "tot", "sow", "sal", "sic", "ted", "wot",
                            "del", "imp", "cob", "way", "ann", "tan", "mci", "job", "wet", "ism",
                            "err", "him", "all", "pad", "hah", "hie", "aim", "ike", "jed", "ego",
                            "mac", "baa", "min", "com", "ill", "was", "cab", "ago", "ina", "big",
                            "ilk", "gal", "tap", "duh", "ola", "ran", "lab", "top", "gob", "hot",
                            "ora", "tia", "kip", "han", "met", "hut", "she", "sac", "fed", "goo",
                            "tee", "ell", "not", "act", "gil", "rut", "ala", "ape", "rig", "cid",
                            "god", "duo", "lin", "aid", "gel", "awl", "lag", "elf", "liz", "ref",
                            "aha", "fib", "oho", "tho", "her", "nor", "ace", "adz", "fun", "ned",
                            "coo", "win", "tao", "coy", "van", "man", "pit", "guy", "foe", "hid",
                            "mai", "sup", "jay", "hob", "mow", "jot", "are", "pol", "arc", "lax",
                            "aft", "alb", "len", "air", "pug", "pox", "vow", "got", "meg", "zoe",
                            "amp", "ale", "bud", "gee", "pin", "dun", "pat", "ten", "mob"])
    print(res)
    print(len(res))
