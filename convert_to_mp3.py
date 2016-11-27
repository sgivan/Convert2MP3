#!/usr/bin/env python

import sys, argparse
import os
import os.path
import re
import string
import subprocess

f = []
alldirpaths = []
alldirnames = []
allfilenames = []

# parser command line options
parser = argparse.ArgumentParser()
parser.add_argument("--limit", help="limit number of files processed", default=30)
args = parser.parse_args()

cnt1 = 0
cnt2 = 0
of = open("warnings.txt", "w")

cnv_script = os.environ['HOME'] + "/projects/audprocess/bin/convert_m4a_to_hq-mp3.pl"
print cnv_script

for (dirpath, dirnames, filenames) in os.walk("./"):

    for f in filenames:
        if (cnt2 > args.limit):
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
                cmd = cnv_script + " --infile " + re.escape(os.path.join(dirpath, f)) + " -b320 --debug"
                print "cmd: " + cmd
                #rtn = subprocess.call(cnv_script + " --infile \"" + os.path.join(dirpath, f) + "\" -b320 --debug", shell=True);
                rtn = subprocess.call(cmd, shell=True);
                cnt2 += 1
                if (rtn):
                    of.write(os.path.join(dirpath, f))
                    sys.exit("abnormal return from conversion script: '" + str(rtn) +"'")



of.close();

#        if (matchobj):
#            allfilenames.append(os.path.join(dirpath, f))

#for fname in allfilenames:
#    print fname

#for dname in alldirnames:
#    print(dname)

#for dpath in alldirpaths:
#    print("'" + dpath + "'")
    
