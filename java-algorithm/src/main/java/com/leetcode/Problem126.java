package com.leetcode;

import java.util.*;

/**
 * 126. Word Ladder II
 * https://leetcode.com/problems/word-ladder-ii/
 *
 * Given two words (beginWord and endWord), and a dictionary's word list,
 * find `all shortest` transformation sequence(s) from beginWord to endWord,
 * such that:
 *
 *     Only one letter can be changed at a time
 *     Each transformed word must exist in the word list.
 *     Note that beginWord is not a transformed word.
 *
 * Note:
 *
 *     Return an empty list if there is no such transformation sequence.
 *     All words have the same length.
 *     All words contain only lowercase alphabetic characters.
 *     You may assume no duplicates in the word list.
 *     You may assume beginWord and endWord are non-empty and are not the same.
 *
 * Example 1:
 *
 * Input:
 * beginWord = "hit",
 * endWord = "cog",
 * wordList = ["hot","dot","dog","lot","log","cog"]
 *
 * Output:
 * [
 *   ["hit","hot","dot","dog","cog"],
 *   ["hit","hot","lot","log","cog"]
 * ]
 *
 * Example 2:
 *
 * Input:
 * beginWord = "hit"
 * endWord = "cog"
 * wordList = ["hot","dot","dog","lot","log"]
 *
 * Output: []
 *
 * Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
 */
public class Problem126 {
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        List<List<String>> ans = new ArrayList<>();
        Map<String, Set<String>> nextWordMap = new HashMap<>();
        int count = getSteps(beginWord, endWord, wordList, nextWordMap);
        if (count == 0)
            return ans;
        List<String> candidate = new ArrayList<>();
        candidate.add(beginWord);
        Set<String> wordSet = new HashSet<>(wordList);
        wordSet.remove(beginWord);
        dfs(ans, candidate, wordSet, nextWordMap, count, endWord);
        return ans;
    }

    private void dfs(List<List<String>> ans, List<String> candidate, Set<String> wordSet, Map<String, Set<String>> nextWordMap, int count, String endWord) {
        if (candidate.size() > count) return;
        String word = candidate.get(candidate.size() - 1);
        if (!nextWordMap.containsKey(word)) return;
        for (String nextWord : nextWordMap.get(word)) {
            if (wordSet.contains(nextWord)) {
                candidate.add(nextWord);
                wordSet.remove(nextWord);
                if (candidate.size() == count) {
                    if (nextWord.equals(endWord))
                        ans.add(new ArrayList<>(candidate));
                } else if (candidate.size() < count) {
                    dfs(ans, candidate, wordSet, nextWordMap, count, endWord);
                }
                candidate.remove(nextWord);
                wordSet.add(nextWord);
            }
        }
    }

    public int getSteps(String beginWord, String endWord, List<String> wordList, Map<String, Set<String>> nextWordMap) {
        Set<String> wordSet = new HashSet<>(wordList);
        if (wordSet.size() == 0 || !wordSet.contains(endWord))
            return 0;
        Queue<String> queue = new LinkedList<>();
        queue.add(beginWord);
        int ans = 1;
        while (!queue.isEmpty()) {
            int n = queue.size();
            for (int i = 0; i < n; i++) {
                String word = queue.poll();
                if (endWord.equals(word))
                    return ans;
                wordSet.remove(word);
                for (int j = 0; j < word.length(); j++) {
                    for (char c = 'a'; c <= 'z'; c++) {
                        String nextWord = word.substring(0, j) + c + word.substring(j + 1);
                        if (wordSet.contains(nextWord)) {
                            Set<String> nextWords = nextWordMap.getOrDefault(word, new HashSet<>());
                            nextWords.add(nextWord);
                            nextWordMap.put(word, nextWords);
                            queue.add(nextWord);
                        }
                    }
                }
            }
            ans++;
        }
        return 0;
    }

    public static void main(String[] args) {
        Problem126 sol = new Problem126();
//        List<String> list2 = Arrays.asList("hot", "dot", "dog", "lot", "log", "cog");
//        System.out.println(sol.findLadders("hit", "cog", list2));
        List<String> list = Arrays.asList("kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob");
        System.out.println(sol.findLadders("cet", "ism", list));
    }
}
