pip install -r requirements.txt

prisma py fetch

DOWNLOADED_BINARY_DIR=$(find /opt/render/.cache/prisma-python/binaries -type d -name "393aa359c9ad4a4bb28630fb5613f9c281cde053" 2>/dev/null | head -n 1)

if [ -n "$DOWNLOADED_BINARY_DIR" ]; then
	cp "$DOWNLOADED_BINARY_DIR/prisma-query-engine-debian-openssl-3.0.x" ./
	echo "Copied Prisma Query Engine to project root."
fi