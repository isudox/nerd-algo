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


if __name__ == '__main__':
    path = os.getcwd() + '/'
    lpath = path + sys.argv[1]
    rpath = path + sys.argv[2]
    filename = path + sys.argv[1] + '_alert_diff.json'
    lret = parse_json_file(lpath)
    rret = parse_json_file(rpath)
    diff = ''
    for rule, alert in lret.items():
        if rule not in rret:
            diff += lret[rule].__str__()
            diff += '\n'

    wf = open(filename, 'w')
    res = wf.write(diff)
    wf.close()
