#!/bin/bash

log_message() {
    echo "[$(date +%T)] REPORT:$1"
}

log_message "Foreman is starting the shift."
sleep 1
log_message "Checking the perimeter..."
sleep 1
log_message "All systems are operational."
