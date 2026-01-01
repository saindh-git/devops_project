#!/bin/bash
echo "--- Disk Health Check ---"

USAGE=85

if [ $USAGE -gt 80 ]; then
   echo "WARNING: Disk usage is at ${USAGE=}%!"
   echo "Action required: Clean up the logs."
else
   echo "SUCCESS: Disk usage is healthy (${USAGE}%)."
fi
