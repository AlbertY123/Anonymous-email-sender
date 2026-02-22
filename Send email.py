import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
subj = input("What is the email subject")
bd = input("What is the email body")
subject = subj
body = bd
re = input("What is the receiver's email?")
receiver_email = re
password = "Fill yourself"
# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = "anonymousesender111@gmail.com"
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))
text = bd 
subject = 'Subject: {}\n\n{}'
# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login("anonymousesender111@gmail.com", "Micky132")
    server.sendmail("anonymousesender111@gmail.com", receiver_email,text)

