#!/bin/bash

for f in *.wav; do printf "ffmpeg -y -i '%q' -acodec libmp3lame -b:a 320k '%q.mp3'\n" "$f" "${f%.*}"; done | xargs -I CMD --max-procs=8 bash -c CMD
