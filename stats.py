#!/usr/bin/env python3
__author__ = "Ole Herman Schumacher Elgesem"
__version__ = "0.1.0"
__email__ = "olehelg@uio.no"
import random
import sys
import json
import os

def save_JSON(d, path):
    with open(path, "w") as f:
        f.write(json.dumps(d))

def load_JSON(path):
    if not os.path.isfile(path):
        return {}
    with open(path, "r") as f:
        data = json.load(f)
    return data

database = load_JSON("db.txt")
win_post = database["win-post"] if "win-post" in database else {}
win_pre = database["win-pre"] if "win-pre" in database else {}
win_both = database["win-both"] if "win-both" in database else {}

for sentence, value in win_both.items():
    words = sentence.split()
    score = win_pre[words[0]] + win_post[words[1]]
    win_both[sentence] = score

def rank_top(data, msg, num):
    top = []
    for key, value in sorted(data.items(), key=lambda kv: kv[1], reverse=True):
        top.append(key+" ("+str(value)+")")
    num = num if num < len(top) else len(top)
    print("TOP "+str(num)+" "+msg+":")
    for i in range(num):
        print(str(i+1)+") "+top[i])
    print("")

rank_top(win_pre, "PREFIXES", 5)
rank_top(win_post, "POSTFIXES", 5)
rank_top(win_both, "OPERATION NAMES", 10)
