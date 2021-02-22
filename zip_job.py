#!/usr/bin/env python

import os
from os import path
import sys
from zipfile import ZipFile

arr = ["a", "b", "c", "d"]
for item in arr:  
    try:
        f = open(item + ".txt" ,"w")
        f.close()
    except:
        sys.exit()

for item in arr:
    try:
        with ZipFile(item + "_" + os.environ['VERSION'] + ".zip", "w") as myzip:
            myzip.write(item + ".txt")
    except:
        sys.exit()
