#!/bin/bash

SERVER_NAME="prod-web-01"
IP_ADDRESS="192.168.1.10"
MAX_CONNECTIONS=100

echo "Auditing server: $SERVER_NAME"
echo "Located at IP: $IP_ADDRESS"
echo "Max Capacity: $MAX_CONNECTIONS users"

Report_Name="${SERVER_NAME}.audit.txt"

echo "Generating Report: $Report_Name"
