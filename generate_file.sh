rtl_fm -f 94.5M -W -s 200000 -r 48000 -l 9 - | aplay -r 48k -f S16_LE -v -v -v -d 10 | cat > ksmb2.txt
