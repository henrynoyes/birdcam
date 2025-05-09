#!/bin/bash
URL=$(python3 $HOME/birdcam/google_auth/start_broadcast.py)
libcamera-vid --lens-position 8.0 -t 0 --nopreview -v 0 --mode 1920:1080 --framerate 30 --bitrate 2500000 --inline -o - -g 60 | ffmpeg -f lavfi -i anullsrc -thread_queue_size 1024 -use_wallclock_as_timestamps 1 -i pipe:0 -c:v copy -f flv -v verbose "$URL" &
