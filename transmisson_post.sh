#!/usr/local/bin/zsh

BASEDIR="/root/.flexget/stat/success"

# Check if the file exists
if [[ -n "${TR_TORRENT_NAME}" && -a "${BASEDIR}/${TR_TORRENT_NAME}" ]]; then
        echo "done" >> "${BASEDIR}/${TR_TORRENT_NAME}";
fi
