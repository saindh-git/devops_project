#!/bin/bash
USER_ID=$(id -u)

if [ $USER_ID -ne 0 ]; then
   echo "Access Denied! You are not the Root user (Grandfather)."
   echo "Current User ID is: $USER_ID"
   exit 1
else 
   echo "Access Granted! Welcome, Root User"
   echo "Starting administrative tasks..."
fi

