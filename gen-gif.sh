# Usage: ./gen-gif.sh <INPUT> <START TIME> <LENGTH> <FPS> <WIDTH> <OUTPUT>
# ex: ./gen-gif.sh input.mp4 10 5 30 640 output.gif

pal="[0:v] fps=$4,scale=$5:-1,split [a][b];[a] palettegen [p];[b][p] paletteuse"

ffmpeg -i "$1" -ss "$2" -t "$3" -filter_complex "$pal" "$6"
