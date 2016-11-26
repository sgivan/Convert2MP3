#!/usr/bin/env python

import sys
import os
import os.path
import re
import string
import subprocess

f = []
alldirpaths = []
alldirnames = []
allfilenames = []

cnt1 = 0
cnt2 = 0
cnv_script = os.environ['HOME'] + "/projects/audprocess/bin/convert_m4a_to_hq-mp3.pl"
print cnv_script

for (dirpath, dirnames, filenames) in os.walk("./"):

    for f in filenames:
        if (cnt2 > 3):
            break
        matchobj = re.match( r'(.+)m4a$', f, re.M|re.I)

        if (matchobj):
            print "this matched: '" + f + "'"
            newfile = matchobj.group(1) + "mp3"
            cnt1 += 1
            if (os.path.exists(os.path.join(dirpath,newfile))):
                print os.path.join(dirpath,newfile) + " exists"
            else:
                print os.path.join(dirpath,newfile) + " does not exist"
                rtn = subprocess.call(cnv_script + " --infile '" + os.path.  join(dirpath, f) + "' -b320", shell=True);
                cnt2 += 1
                if (rtn):
                    sys.exit("abnormal return from conversion script: '" + str(rtn) +"'")


#        if (matchobj):
#            allfilenames.append(os.path.join(dirpath, f))

#for fname in allfilenames:
#    print fname

#for dname in alldirnames:
#    print(dname)

#for dpath in alldirpaths:
#    print("'" + dpath + "'")
    
