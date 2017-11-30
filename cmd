rsync -avz -e ssh scott@192.168.1.9:'/Users/scott/Music/iTunes/iTunes\ Media/Music' ./
rsync -avh -e ssh genomeogenesis.com:/mnt/home/givans/Music ./
ffprobe -i out.mp3 -v quiet -show_entries stream=bit_rate -of default=noprint_wrappers=1
