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


def read_field(rpath: str):
    s = set()
    with open(rpath) as f:
        for line in f:
            segs = line.split('ordernos = [')
            order_nos = segs[1][:-2]
            order_nos_list = order_nos.split(',')
            for no in order_nos_list:
                s.add(no)
    print(s)
    print(len(s))

def count_distinct():
    nums = []
    counter = collections.Counter(nums)
    print(counter.keys())


if __name__ == '__main__':
    read_field('/Users/bytedance/Downloads/20241016192031E3AC658DE910A58665F4.txt')
