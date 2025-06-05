import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_notification(task, date, time, to_email):
    sender_email = "personalmanagertask@gmail.com"          # Replace with your Gmail address
    sender_password = "yoce vqof rqhb hrdq"          # Use Gmail App Password (if 2FA enabled)

    message = MIMEMultipart("alternative")
    message["Subject"] = f"Task Reminder: '{task}'"
    message["From"] = sender_email
    message["To"] = to_email

    text = f"Hello,\n\nYour task '{task}' is scheduled on {date} at {time}.\nPlease take necessary action.\n\nBest,\nTask Manager Team"

    html = f"""
    <html>
      <body>
        <p>Hello,<br><br>
           Your task '<strong>{task}</strong>' is scheduled on <strong>{date}</strong> at <strong>{time}</strong>.<br>
           Please take necessary action.<br><br>
           Best,<br>
           Task Manager Team
        </p>
      </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())
        print(f"Notification sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
