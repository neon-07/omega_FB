import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

# Email configuration
email_host = 'smtp.gmail.com'
email_port = 465 
email_sender = 'fairbet255@gmail.com'  # Your Gmail email address  " fairbet255@gmail.com" / "fairbetin@gmail.com" / "infairbet@gmail.com"
email_password = 'nwrb zcaq qpbh peku'  # Your Gmail password  "nwrb zcaq qpbh peku" / "czxk tgwc olhj enuo" / "bqns mgbe bfaz ymif"
email_sender_name = 'Fairbet365'
email_subject = '🎉 Get a 12% Bonus on Your First Deposit at FairBet365! 🎉'

# Read HTML content from file
with open('email_template.html', 'r') as file:  
    email_body = file.read()
    

# List of recipients
df = pd.read_csv('emails.csv')
recipients = df['Email'].tolist()

#recipients = ['sawantindranil@gmail.com']

try:
    server = smtplib.SMTP_SSL(email_host, email_port)
    server.login(email_sender, email_password)

    # Iterate over recipients and send emails
    for recipient in recipients:
        # Create a MIME message
        message = MIMEMultipart()
        message['From'] = f'{email_sender_name} <{email_sender}>'
        message['To'] = recipient
        message['Subject'] = email_subject

        # Attach HTML body to the email
        message.attach(MIMEText(email_body, 'html'))

        # Send the email
        server.sendmail(email_sender, recipient, message.as_string())
    print(recipients)
    print("Emails sent successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection to the SMTP server
    server.quit()
