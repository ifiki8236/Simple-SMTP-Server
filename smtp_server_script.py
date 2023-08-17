import smtplib

#SMTP server start
smtp_server = ''
port = 587 #port for emails and SSL protocol
myServer = smtplib.SMTP(smtp_server, port) #initialize server

#host email and password
host_email = ''
password = ''

#client email 
client_email = ''

#start SMTP server
try:
    myServer.starttls()
    print('[Server Started]')
except Exception as e:
    print(f'Error {e}')
    exit()

#log in to email
try:
    myServer.login(host_email, password)
    print('Login successful')
except Exception as e:
    print(f'Could not log into host email {e}')
    exit()

#compose email
subject = input('Subject of Email: ')
body = input('What Do You Want to Say?: ')
composed_email = f'Subject: {subject}\n\n{body}'

#send email
try:
    myServer.sendmail(host_email, client_email, composed_email)
    print('Email Sent!')
except Exception as e:
    print(f'Email failed to send {e}')
    exit()
    
#close server
myServer.quit()
