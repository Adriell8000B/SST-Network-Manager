#!/usr/bin/env bash

set -e

echo "--- Starting Render Build Script ---"

## 1. Install Dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

## 2. Fetch the Prisma Binary
echo "Fetching Prisma Query Engine binary..."
prisma py fetch

# --- FIX: Direct Path Copy ---
# Use the full path derived from your successful download log.
# This variable stores the exact location of the downloaded binary file.
PRISMA_ENGINE_FILE="/opt/render/.cache/prisma-python/binaries/5.17.0/393aa359c9ad4a4bb28630fb5613f9c281cde053/prisma-query-engine-debian-openssl-3.0.x"

## 3. Copy the Binary to the Project Root
echo "Attempting to copy Query Engine to project root..."

if [ -f "$PRISMA_ENGINE_FILE" ]; then
    cp "$PRISMA_ENGINE_FILE" ./
    echo "Successfully copied Query Engine to the project root: $(basename "$PRISMA_ENGINE_FILE")"
else
    echo "ERROR: Query Engine not found at expected location $PRISMA_ENGINE_FILE"
    exit 1
fi

echo "--- Build Script Finished Successfully 🎉 ---"