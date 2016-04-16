#!/usr/bin/env python3
__author__ = "Ole Herman Schumacher Elgesem"
__version__ = "0.0.2"
__email__ = "olehelg@uio.no"
import json
import os

def save_JSON(d, path):
    with open(path, "w") as f:
        f.write(json.dumps(d,indent=2, sort_keys=True))

def load_JSON(path):
    if not os.path.isfile(path):
        return {}
    with open(path, "r") as f:
        data = json.load(f)
    return data
