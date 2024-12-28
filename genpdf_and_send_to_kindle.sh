#!/bin/bash

# Check if a file argument was provided
if [ $# -eq 0 ]; then
    echo "Error: No file argument provided"
    echo "Usage: $0 <markdown_file>"
    exit 1
fi

file="$1"
# Format: YYYYMMDD_HHMM
timestamp=$(date "+%Y%m%d_%H%M")
pdf_file="test_${timestamp}.pdf"
email_file="test_${timestamp}.pdf"

if [ -f "$file" ]; then
    echo "Generating PDF file: $pdf_file from markdown file: $file"
    md2pdf --css styles.css $file $pdf_file
    echo "Sending email to kindle with file: $email_file"
    python send_email.py $email_file
else
    echo "File $file does not exist"
fi
