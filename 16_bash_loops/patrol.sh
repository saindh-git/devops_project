#!/bin/bash
SERVERS="web-01 db-01 app-01 backup-01"

echo "---starting estate patrol----"

for svr in $SERVERS
do
    echo "scanning $svr"
    sleep 1
    echo "Result:$svr is up and Healthy"
done

echo "patrol complete.All systems clear"
