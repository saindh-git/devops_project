#!/bin/bash

show_status() {
    echo "Checking Estate Status..."
    uptime
}

while true
do 
    echo "=========================="
    echo "  ESTATE MASTER DASHBOARD "
    echo "=========================="
    echo "1. Show System Uptime"
    echo "2. Show Disk Usage"
    echo "3. Exit"
    read -p "Select an option: " CHOICE
    
    case $CHOICE in
        1) show_status ;;
        2) df -h | head -n 2 ;;
        3) echo "Exiting..."; break ;; # The 'break' shatters the while loop
        *) echo "Invalid Choice, try again." ;;
    esac
done


