#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "--- Starting Render Build Script ---"

## 1. Install Dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

## 2. Fetch the Prisma Binary
# This downloads the query engine binary specific to the environment.
echo "Fetching Prisma Query Engine binary..."
prisma py fetch

## 3. Find the Final Binary Path using Python
# This Python command finds the directory where the Prisma client is installed.
# We assume the query engine is in the subdirectory 'binaries' within the package installation.
PRISMA_CLIENT_DIR=$(python -c "import prisma; import os; print(os.path.dirname(prisma.__file__))")
ENGINE_NAME="prisma-query-engine-debian-openssl-3.0.x"

# We must now try to locate the engine within the downloaded cache structure.
# A simpler and more direct approach for the shell environment is often a glob search:
DOWNLOADED_ENGINE=$(find /opt/render/.cache/prisma-python/binaries/ -name "$ENGINE_NAME" 2>/dev/null | head -n 1)

## 4. Copy the Binary to the Project Root
# Copying the binary to the project root (./) is the most common way to resolve 
# pathing issues in container deployments like Render.
if [ -f "$DOWNLOADED_ENGINE" ]; then
    cp "$DOWNLOADED_ENGINE" ./
    echo "Successfully copied Query Engine to the project root: $(basename "$DOWNLOADED_ENGINE")"
else
    echo "ERROR: Prisma Query Engine binary not found! Check the 'prisma py fetch' output."
    exit 1
fi

echo "--- Build Script Finished Successfully 🎉 ---"