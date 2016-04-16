#!/usr/bin/env python3
__author__ = "Ole Herman Schumacher Elgesem"
__version__ = "0.1.0"
__email__ = "olehelg@uio.no"
import os
import sys
from common import load_JSON, save_JSON

# Add raw data from file at path to dictionary d (database)
def update_stats(d, path):
    tmp = []
    with open(path) as f:
        tmp = f.readlines()
    os.remove(path)
    for w in tmp:
        w = w.strip()
        if w in d:
            d[w] += 1
        else:
            d[w] = 1

# import and delete all *win.txt files (these contain raw data, responses)
def collect_results(data, ending):
    files = []
    for file in os.listdir("./"):
        if file.endswith(ending):
            files.append(file)
    for s in files:
        update_stats(data, s)

# merge database(dict) newdata into data
def add_database(data, newdata):
    for result_type, result_dict in newdata.items():
        if not result_type in data:
            data[result_type] = result_dict
        else:
            for word, num in result_dict.items():
                if word in data[result_type]:
                    data[result_type][word] += num
                else:
                    data[result_type][word] = num

# find and merge all *db.txt files
def collect_databases(data):
    files = []
    for file in os.listdir("./"):
        if file.endswith("db.txt"):
            files.append(file)
    for d in files:
        add_database(data, load_JSON(d))
        os.remove(d)

def main(argv):
    database = {"win-pre":{},"win-post":{},"win-both":{}}
    collect_databases(database)
    win_post = database["win-post"]
    win_pre = database["win-pre"]
    win_both = database["win-both"]

    collect_results(win_pre, "prewin.txt")
    collect_results(win_post, "postwin.txt")
    collect_results(win_both, "bothwin.txt")
    print(win_post)
    print(win_pre)
    print(win_both)

    file_prefix = ""
    if(len(argv)>=2):
        file_prefix = argv[1]+"_"
    save_JSON(database, file_prefix+"db.txt")

if __name__ == '__main__':
    main(sys.argv)
