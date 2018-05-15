#!/bin/bash

USERNAME='c45cd1f54ae73bdf239e9fb19133a1c18f30773f59b4f6f920c3ced5fd0cb783ft7QzoSKl+X7BAbN21/s65eEzf0'
PASSWORD='ecVpCRk6x5UVSCONQEHpMOtYWEY'

REQ="user=$USERNAME&$PASSWORD=bar"
LINK="http://www.consortium.ri.cmu.edu/data/ck/"

wget --save-cookies cookies.txt \
     --keep-session-cookies \
     --post-data $REQ \
     --delete-after \
     "$LINK"

     # Now grab the page or pages we care about.
wget --load-cookies cookies.txt \
    -r -np -nH \
    "$LINK"
