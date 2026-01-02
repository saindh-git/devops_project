#!/bin/bash

SOURCE_DIR="source_files"
BACKUP_DIR="backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="estate_backup_$TIMESTAMP.tar.gz"

prepare_vault() {
    if [ ! -d $BACKUP_DIR ]; then
    echo "creating $BACKUP_DIR...."
    mkdir -p "$BACKUP_DIR"
    fi
}

prepare_vault

echo "starting backup for $SOURCE_DIR...."

tar -czf "$BACKUP_DIR/$BACKUP_NAME" "$SOURCE_DIR"

if [ $? -eq 0 ]; then
    echo "SUCCESS: backup saved as $BACKUP_NAME"
else
    echo "FAILURE: Backup Failed!"
fi

