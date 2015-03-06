#!/usr/bin/zsh

BASEDIR="./stat/success"

foreach i (${BASEDIR}/*)
        if [[ $(tail ${i} -n 1 | tr -d '\n') != "done" ]]; then
                echo "done" >> $i;
        fi
end
