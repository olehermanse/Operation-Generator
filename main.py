#!/usr/bin/env python3
__author__ = "Ole Herman Schumacher Elgesem"
__credits__ = ["Tor Jan Derek Berstad", "Ole Herman Schumacher Elgesem"]
__version__ = "0.0.1"
__email__ = "olehelg@uio.no"
import random
import sys

output_prefix = "default_"
print(sys.argv)
if(len(sys.argv) >= 2):
    output_prefix = sys.argv[1] + "_"

pre_list= []
with open("pre.txt") as f:
    pre_list = f.readlines()
    pre_list = [x.strip('\n') for x in pre_list]
    post_list= []
with open("post.txt") as f:
    post_list= f.readlines()
    post_list = [x.strip('\n') for x in post_list]
alternatives = 4
while(True):
    pre = []
    post = []
    print("\nWhich is best/funniest?")
    for i in range(alternatives):
        a = random.randint(0,len(post_list)-1)
        b = random.randint(0,len(pre_list)-1)
        pre.append(pre_list[b])
        post.append(post_list[a])
        print(str(i+1)+") Operation "+pre_list[b]+" "+post_list[a])
    print(str(alternatives+1)+") None of the above.")
    print("0) Exit")
    choice = input("Make a choice:")
    choice = int(choice)
    if(choice == 0):
        sys.exit(0)

    choice = choice - 1
    op = output_prefix
    if(choice < alternatives):
        with open(op+"prewin.txt", "a") as f:
            f.write(pre[choice]+"\n")
        with open(op+"postwin.txt", "a") as f:
            f.write(post[choice]+"\n")
        with open(op+"bothwin.txt", "a") as f:
            f.write(pre[choice] + " " + post[choice]+"\n")
