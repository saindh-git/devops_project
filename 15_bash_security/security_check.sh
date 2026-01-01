#!/bin/bash
read -p "Enter Username:" USERNAME
read -p "Enter Department: " DEPT

echo "---Security Processing----"
 
if [ "$USERNAME" == "admin" ] && [ "$DEPT" == "devops" ]; then
    echo "WELCOME, MASTER ARCHITECT. Full Estate Access Granted."
else
   echo "ACCESS DENIED. You do not have the proper clearance."
fi

