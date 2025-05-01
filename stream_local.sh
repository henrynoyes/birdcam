libcamera-vid --lens-position 8.0 -t 0 --nopreview -v 0 --mode 1920:1080 --framerate 30 --inline -o - | cvlc stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/bird}' :demux=h264 &
