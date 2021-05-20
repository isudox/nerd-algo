# 频次哈希表 + 字典排序

要找出出现频率前 K 的单词，必然需要统计每个单词的出现频次。其中，对于出现频次相同的单词，还要进行字典排序，即字典序靠前的单词排在前面。

因此，考虑用哈希表记录每个单词出现的频次，另外，对相同频次的单词，按字典排序。最后整理出前 K 个单词。这个思路很直观。

```python3 []
class Solution:
    def top_k_frequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        mapper = [[] for _ in range(len(words) + 1)]
        for word, cnt in counter.items():
            mapper[cnt].append(word)
        ans = []
        for i in range(len(words), -1, -1):
            if len(ans) == k:
                return ans
            if mapper[i]:
                mapper[i].sort()
                if len(ans) + len(mapper[i]) <= k:
                    ans.extend(mapper[i])
                else:
                    ans.extend(mapper[i][:k - len(ans)])
```

时间复杂度: `O(N*log(N))`
空间复杂度: `O(N)`

# 频次哈希表 + 小根堆

因为题设要找的是出现频率从大到小排，前 k 个单词，所以也可以考虑用一个容量为 k 的小根堆。该小根堆的插入和删除条件如下：

- 当小根堆不满时，直接插入；
- 当小根堆满时，且当前单词的出现频次大于小根堆的顶部元素（即目前已知的出现频次排 k 位的单词），将其替换掉；
- 当小根堆满是，且当前单词的出现频次等于小根堆的顶部元素，如果当前单词的字典序比堆顶元素单词更靠前，则将其替换掉；
- 其他情况，不做处理；

因此，对于上述小根堆的排序，有两个维度：

1. 单词出现频次
2. 单词字典序

条件 1 优先于条件 2。

注，如果是 Java，可以直接用`PriorityQueue`实现自定义的排序；而 Python 的话，需要用自定义对象，重写`__lt__`方法来修改堆排序的逻辑

```python3 []
class Solution:
    def top_k_frequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        pq = []  # store tuple of (cnt, word)
        for word, cnt in counter.items():
            if len(pq) < k:
                heapq.heappush(pq, Pair(cnt, word))
            elif pq[0].cnt < cnt or (pq[0].cnt == cnt and word < pq[0].word):
                heapq.heappop(pq)
                heapq.heappush(pq, Pair(cnt, word))
        ans = []
        while pq:
            ans.insert(0, heapq.heappop(pq).word)
        return ans

class Pair(object):
    def __init__(self, cnt: int, word: str):
        self.cnt = cnt
        self.word = word

    def __lt__(self, another):
        if self.cnt == another.cnt:
            return self.word > another.word
        return self.cnt < another.cnt
```

时间复杂度: `O(N*long(N))`
空间复杂度: `O(N)`
