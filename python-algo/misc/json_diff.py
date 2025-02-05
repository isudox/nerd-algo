import collections
import json
import os
import sys


def parse_json_file(rpath: str):
    store = {}
    with open(rpath) as f:
        raw = json.load(f)
        for ele in raw:
            store[ele['rule']] = {"name": ele['name'], "id": ele['id']}
    return store


def read_field(rpath: str, field: str, start: int, end: int):
    s = set()
    with open(rpath) as f:
        for line in f:
            segs = line.split(field)
            order_no = segs[1][start:end]
            s.add(order_no)
    print(s)
    print(len(s))


def count_distinct():
    nums = []
    counter = collections.Counter(nums)
    print(counter.keys())


def unique(rpath: str):
    s = set()
    with open(rpath) as f:
        for line in f:
            print(line)
            s.add(line[:-1])
    print(s)
    print(len(s))


if __name__ == '__main__':
    read_field('/Users/bytedance/Downloads/932912688.txt', 'ordernos = ["', 0, 19)
