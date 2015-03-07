#!/usr/local/bin/zsh

BASEDIR="/root/.flexget/stat/success"

# Check if the file exists
if [[ -n "${TR_TORRENT_NAME}" && -a "${BASEDIR}/${TR_TORRENT_NAME}" ]]; then
        if [[ $(tail ${i} -n 1 | tr -d '\n') != "done" ]]; then
                echo "done" >> "${BASEDIR}/${TR_TORRENT_NAME}";
        fi 
fi
