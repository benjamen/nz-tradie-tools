#!/bin/bash
# Returns how many real articles exist for today.
# Exit 0 = under limit (write one more). Exit 1 = limit reached (do nothing).
TODAY=$(date +%Y-%m-%d)
SITE_DIR="$(dirname "$0")/.."
COUNT=$(grep -rl "date: $TODAY" "$SITE_DIR/content/articles/" 2>/dev/null | wc -l)
echo "Articles today: $COUNT / 3"
if [ "$COUNT" -ge 3 ]; then
    echo "LIMIT REACHED — write nothing, reply HEARTBEAT_OK"
    exit 1
else
    echo "WRITE $((3 - COUNT)) MORE — then stop"
    exit 0
fi
