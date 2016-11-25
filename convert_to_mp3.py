#!/usr/bin/env python

from os import listdir, walk
import os.path
import string

f = []
alldirpaths = []
alldirnames = []
allfilenames = []

cnt = 0
for (dirpath, dirnames, filenames) in os.walk("./"):
    print dirpath
    for f in filenames:
        allfilenames.append(os.path.join(dirpath, f))

for fname in allfilenames:
    print fname

#for dname in alldirnames:
#    print(dname)

#for dpath in alldirpaths:
#    print("'" + dpath + "'")
    
