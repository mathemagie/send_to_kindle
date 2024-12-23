#!/bin/bash

file="agent.md"
# Format: YYYYMMDD_HHMM
timestamp=$(date "+%Y%m%d_%H%M")
pdf_file="test_${timestamp}.pdf"
email_file="test_${timestamp}.pdf"

if [ -f "$file" ]; then
    md2pdf --css styles.css $file $pdf_file && python send_email.py $email_file
else
    echo "File $file does not exist"
fi
