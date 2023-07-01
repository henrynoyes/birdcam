pal="[0:v] fps=$4,scale=$5:-1,split [a][b];[a] palettegen [p];[b][p] paletteuse"

ffmpeg -i "$1" -ss "$2" -t "$3" -filter_complex "$pal" "$6"
