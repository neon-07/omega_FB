import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

# Email configuration
email_host = 'smtp.gmail.com'
email_port = 465
email_sender = 'fairbet255@gmail.com'  # Your Gmail email address
email_password = 'nwrb zcaq qpbh peku'  # Your Gmail password
email_sender_name = 'Fairbet365'
email_subject = '🎉 Get a 12% Bonus on Your First Deposit at FairBet365! 🎉'

# Read HTML content from file
with open('email_template.html', 'r') as file:
    email_body = file.read()

# List of recipients
df = pd.read_csv('emails.csv')
recipients = df['Email'].tolist()

# Function to split list into chunks
def chunk_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Create chunks of 100 recipients each
recipient_chunks = list(chunk_list(recipients, 100))

try:
    server = smtplib.SMTP_SSL(email_host, email_port)
    server.login(email_sender, email_password)

    # Iterate over each chunk and send emails
    for chunk in recipient_chunks:
        # Create a MIME message
        message = MIMEMultipart()
        message['From'] = f'{email_sender_name} <{email_sender}>'
        message['To'] = ', '.join(chunk)  # Join chunk into a single string
        message['Subject'] = email_subject

        # Attach HTML body to the email
        message.attach(MIMEText(email_body, 'html'))

        # Send the email
        server.sendmail(email_sender, chunk, message.as_string())
        print(f"Emails sent to: {chunk}")

    print("All emails sent successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection to the SMTP server
    server.quit()