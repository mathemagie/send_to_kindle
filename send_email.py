import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime
from dotenv import load_dotenv
import logging
import sys

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def send_email(file):
    """
    Sends an email with the provided line as the message content.

    Args:
        line (str): The line to be included in the email message.
        env (str): The environment (staging or prod).
    """
    msg = MIMEMultipart()

    msg[
        "Subject"
    ] = f"[IMPORTS] {datetime.date.today()} {datetime.datetime.now().time()}"
    msg["From"] = "aurelien.fache@gmail.com"
    msg["To"] = "aurelien.fache+kindle@kindle.com"
    msg.attach(MIMEText("PDF attached"))

    with open(f"{file}", "rb") as attachment:
        part = MIMEBase("application", "pdf")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={file}.pdf",
        )
        msg.attach(part)

    smtp_server = smtplib.SMTP("in-v3.mailjet.com", 587)
    smtp_server.set_debuglevel(0)
    smtp_server.starttls()
    username = os.environ.get("MAILJET_USERNAME")
    password = os.environ.get("MAILJET_PASSWORD")
    smtp_server.login(username, password)
    smtp_server.send_message(msg)
    smtp_server.quit()


if __name__ == "__main__":
    send_email(sys.argv[1])
