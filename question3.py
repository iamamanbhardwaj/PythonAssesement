from datetime import datetime
import requests
from datetime import datetime
from requests.exceptions import HTTPError
import smtplib, ssl

###
# Calling this python script from windows task scheduler by calling bat file 
# "C:\Users\aman.bhardwaj\AppData\Local\Programs\Python\Python38-32\python.exe" "D:\poc\python\question3_job.py" 
###


def sendEmailtoAdmin(message):
    admin_email = "aman.bhardwaj@3pillarglobal.com"
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "testingcovidvaccine@gmail.com"
    password = "My12345678!@#"

    # enable Less secure app access
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, admin_email, message)

    except Exception as e:
        print(e)
    finally:
        server.quit() 

def testGetAPI(urls): 
    for url in urls:

        try:
            myFile = open('ServicesStatusLog.txt', 'a+') 

            myFile.write(f'HTTP GET url {url} called on {datetime.now()}\n')

            response = requests.get(url)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()

            myFile.write(f'Response: {response.json()}\n\n')
        except HTTPError as http_err:
            myFile.write(f'Error {http_err} \n\n')
            sendEmailtoAdmin(f'Hi Admin, \n API {url} was called on date {datetime.now()}. \n\nIt errored out and gave the response as :\n {http_err} \n\n.\n\n\n. kindly check you API detils ASAP!! ')
        finally:
            myFile.close()


testGetAPI(['https://api.github.com','https://testresponse.free.beeceptor.com/my/api/test500', 'https://5ff5ef18941eaf0017f374e3.mockapi.io/users'])