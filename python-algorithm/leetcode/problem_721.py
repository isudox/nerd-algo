"""721. Accounts Merge
https://leetcode.com/problems/accounts-merge/
"""
import collections
from typing import List


class Solution:
    def accounts_merge(self, accounts: List[List[str]]) -> List[List[str]]:
        def union(a: int, b: int):
            uf[find(a)] = find(b)

        def find(x: int) -> int:
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        n = len(accounts)
        uf = list(range(n))
        email_dict = {}  # key is email, value is the `first` index of accounts which has the key email
        for i in range(n):
            account = accounts[i]
            for j in range(1, len(account)):
                if account[j] not in email_dict:
                    email_dict[account[j]] = i
                else:
                    union(email_dict[account[j]], i)
        graphs = collections.defaultdict(list)
        for i in range(n):
            graphs[find(i)].append(i)
        ans = []
        for idx, idx_list in graphs.items():
            cur = [accounts[idx][0]]
            emails = set()
            for i in idx_list:
                emails.update(accounts[i][1:])
            emails = list(emails)
            emails.sort()
            cur.extend(emails)
            ans.append(cur)
        return ans
