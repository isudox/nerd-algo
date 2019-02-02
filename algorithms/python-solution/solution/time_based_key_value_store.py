# -*- coding: utf-8 -*-


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        if key in self.dic:
            self.dic[key].append({'v': value, 't': timestamp})
        else:
            self.dic[key] = [{'v': value, 't': timestamp}]

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        if key in self.dic:
            for kv in reversed(self.dic[key]):
                if timestamp >= kv['t']:
                    return kv['v']
            return ""
        else:
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
