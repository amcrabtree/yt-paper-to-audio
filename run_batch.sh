#!/usr/bin/env bash

PDF_DIR="papers"

if [ ! -d "$PDF_DIR" ]; then
    echo "PDF directory not found: $PDF_DIR" >&2
    exit 1
fi

for pdf in "$PDF_DIR"/*.pdf; do
    echo "Processing: $pdf"
    python paper_to_audio.py "$pdf"
done
