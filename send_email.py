from email.message import EmailMessage
import ssl
import smtplib

from pymongo import MongoClient

client = MongoClient('mongodb+srv://admin:1234@cluster0.q5ybpok.mongodb.net/')
db = client['google_passcode']
collection = db['google_pass']

def get_passwords(query={}):
    passwords = collection.find(query, {'_id': 0, 'password': 1})  
    password_list = [doc['password'] for doc in passwords]
    return password_list

google_passwords = get_passwords({"name": "google password"})

# Print each password separately
password_string = ' '.join(google_passwords)

# ----------------------------------------------------------------------------

email_sender = 'pongpol095@gmail.com'
email_password = password_string
email_reciver = 'dimog92335@xgh6.com'

subject = "this is my second email send"
body = """
Hi this is me. you know who am I?
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())