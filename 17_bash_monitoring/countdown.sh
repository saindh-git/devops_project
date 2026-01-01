#!/bin/bash
COUNT=5

echo "---estate security system restart----"

while [ $COUNT -gt 0 ]
do
    echo "Restarting in $COUNT seconds..."
    ((COUNT--))
    sleep 1
done
echo "RESTART COMPLETE. Estate is secure."
