#!/bin/bash

echo "---estate security sign-in---"

read -p "Enter your Technician Name:" TECH_NAME
read -p "Which server are you working on:" ASSIGNED_SERVER

echo "ACCESS GRANTED"
echo "Technician $TECH_NAME  is now logged into $ASSIGNED_SERVER" 

LOG_FILE="${TECH_NAME}_log.txt"
echo "Log created on: $(date) " > $LOG_FILE 
echo "Technician: $TECH_NAME " >> $LOG_FILE
echo "Server: $ASSIGNED_SERVER" >> $LOG_FILE

echo "your activity has been logged in $LOG_FILE"
