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
parser.add_argument("--bitrate", help="bitrate of converted files; pick 128, 256 or 320", default=320)
parser.add_argument("--debug", help="send debugging output to terminal", action='store_true')
parser.add_argument("--verbose", help="send verbose output to terminal", action='store_true')
parser.add_argument("--keeplower", help="if output file exists, keep it if it has a lower bit rate", action='store_true')
parser.add_argument("--keephigher", help="if output file exists, keep it if it has a higher bit rate", action='store_true')
args = parser.parse_args()

looplimit = args.limit
debug = args.debug
verbose = args.verbose
if (debug): verbose = True
bitrate = 320
bitrateflag = "--b320"
keeplower = args.keeplower
keephigher = args.keephigher
if (args.bitrate):
        if (args.bitrate == '128'):
            bitrateflag = "--b128"
        elif (args.bitrate == '256'):
            bitrateflag = "--b256"
'''
if (1):
    print "args.bitrate " + args.bitrate
    print "args.limit " + args.limit
    if (args.bitrate == '256'):
        print "yes, " + args.bitrate
    sys.exit()
'''

cnt1 = 0
cnt2 = 0
of = open("warnings.txt", "w")

cnv_script = os.environ['HOME'] + "/projects/audprocess/bin/convert_m4a_to_hq-mp3.pl"
if (debug): print cnv_script

for (dirpath, dirnames, filenames) in os.walk("./"):

    for f in filenames:

        if (cnt2 >= int(args.limit)):
            break

        matchobj = re.match( r'(.+)m4a$', f, re.M|re.I)

        if (matchobj):
            if (verbose): print "\nfile: '" + f + "'"
            newfile = matchobj.group(1) + "mp3"
            cnt1 += 1
            cmd = cnv_script
            if (os.path.exists(os.path.join(dirpath,newfile))):
                if (verbose): print os.path.join(dirpath,newfile) + " exists"

                if (keeplower):
                    cmd = cmd + " --verbose --lowerbitrate --infile " + re.escape(os.path.join(dirpath, f)) + " " + bitrateflag
                elif (keephigher):
                    cmd = cmd + " --verbose --higherbitrate --infile " + re.escape(os.path.join(dirpath, f)) + " " + bitrateflag
                else:
                    cmd = cmd + " --verbose --infile " + re.escape(os.path.join(dirpath, f)) + " " + bitrateflag

            else:
                if (verbose): print os.path.join(dirpath,newfile) + " does not exist"
                #cmd = cnv_script + " --verbose --infile " + re.escape(os.path.join(dirpath, f)) + " " + bitrateflag
                cmd = cmd + " --verbose --infile " + re.escape(os.path.join(dirpath, f)) + " " + bitrateflag
                
            if (debug): print "cmd: " + cmd
            #rtn = subprocess.call(cnv_script + " --infile \"" + os.path.join(dirpath, f) + "\" -b320", shell=True);
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
    
