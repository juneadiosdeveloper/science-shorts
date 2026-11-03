# usage: split.sh src.mp4 name split_s
src=$1; n=$2; s=$3
ffmpeg -loglevel error -y -i $src -t $s -an -c:v libx264 -crf 16 -preset fast ${n}a.mp4
ffmpeg -loglevel error -y -ss $s -i $src -an -vf "crop=iw/1.15:ih/1.15:(iw-ow)/2:(ih-oh)*0.3,scale=1080:1920" -c:v libx264 -crf 16 -preset fast ${n}b.mp4
