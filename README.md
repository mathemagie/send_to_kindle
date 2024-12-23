# PDF Generation and Email Sending Script

This script converts a Markdown file to PDF and sends it via email.

## Prerequisites

- Python 3.x
- `md2pdf` package
- Required Python packages (see `requirements.txt`)
- Environment variables set up for email credentials

## Usage

 md2pdf --css styles.css agent.md test17.pdf && python send_email.py test17.pdf