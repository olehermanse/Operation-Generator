#!/usr/bin/env python3
__author__ = "Ole Herman Schumacher Elgesem"
__version__ = "0.0.1"
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

def update_stats(d, path):
    tmp = []
    with open(path) as f:
        tmp = f.readlines()
    os.remove(path)
    for w in tmp:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1

def collect_files(data, ending):
    files = []
    for file in os.listdir("./"):
        if file.endswith(ending):
            files.append(file)
    for s in files:
        update_stats(data, s)

win_post = load_JSON("db_post.txt")
collect_files(win_post, "postwin.txt")
win_pre = load_JSON("db_pre.txt")
collect_files(win_pre, "prewin.txt")
win_both = load_JSON("db_both.txt")
collect_files(win_both, "bothwin.txt")

print(win_post)
print(win_pre)
print(win_both)

save_JSON(win_post, "db_post.txt")
save_JSON(win_pre, "db_pre.txt")
save_JSON(win_both, "db_both.txt")
