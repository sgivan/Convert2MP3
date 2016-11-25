#!/bin/bash

cd $HOME
#rsync -avh -e ssh genomeogenesis.com:/mnt/home/givans/Music ./
#rsync -avh -e "ssh -p 743" givans@192.168.1.18:/mnt/home/givans/Music ./
rsync -avh -e ssh sgivan@10.0.0.24:Music ./
