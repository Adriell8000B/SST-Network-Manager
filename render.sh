#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "--- Starting Render Build Script ---"

## 1. Install Dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

## 2. Fetch the Prisma Binary
# This downloads the query engine binary specific to the environment (debian-openssl-3.0.x on Render).
echo "Fetching Prisma Query Engine binary..."
prisma py fetch

## 3. Find the Final Binary Path
# The 'prisma py path' command outputs the exact location where the application 
# expects to find the query engine binary.
echo "Determining the target path for the binary..."
PRISMA_ENGINE_PATH=$(prisma py path)

# This command extracts the directory of the query engine binary.
DOWNLOADED_DIR=$(dirname "$PRISMA_ENGINE_PATH")

## 4. Copy the Binary to a Well-Known Location (Project Root)
# Copying the binary to a known location, like the project root (.), often resolves 
# runtime pathing issues when gunicorn starts the application.
if [ -f "$PRISMA_ENGINE_PATH" ]; then
	cp "$PRISMA_ENGINE_PATH" ./
	echo "Successfully copied Query Engine to the project root: $(basename "$PRISMA_ENGINE_PATH")"
else
    echo "Warning: Prisma Query Engine binary not found at the expected path: $PRISMA_ENGINE_PATH"
fi

echo "--- Build Script Finished Successfully 🎉 ---"
