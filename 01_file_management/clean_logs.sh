#!/bin/bash
if [ ! -d "archive" ]; then
   echo "archieve folder is missing. creating it now"
   mkdir archive
fi

if [ ls *.log > /dev/null 2>&1 ]; then

echo "moving logs to the archieve"

mv *.log archive/
else
   echo "no logs found.house is already clean!"
if



