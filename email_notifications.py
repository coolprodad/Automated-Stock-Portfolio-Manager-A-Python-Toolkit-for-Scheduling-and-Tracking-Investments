import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(subject, body, to_email, from_email, password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Start TLS encryption
    server.login(from_email, password)  # Login to the SMTP server
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# Environment variables for email credentials
from_email = os.getenv('EMAIL_ADDRESS', 'shashankkv98@gmail.com')
password = os.getenv('EMAIL_PASSWORD', 'Titan#10081998')
to_email = 'kvshashank10081998@gmail.com'
subject = 'Stock Update for Every One Hour'
body = 'As for your request, here are the updates on your stock portfolio.'

# Send email
send_email(subject, body, to_email, from_email, password)
