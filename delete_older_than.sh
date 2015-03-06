#!/usr/local/bin/zsh

BASEDIR=`pwd`
DEFAULT="+7" # Seven days

T=${${1}:-${DEFAULT}}

res=$(find "${BASEDIR}" -mtime ${T} -type f)
echo ${res}

foreach i (${res})
        echo "${i}"
end

echo
read "?Really delete? (C-c to abort)"

foreach i (${res})
        rm "${i}";
end
