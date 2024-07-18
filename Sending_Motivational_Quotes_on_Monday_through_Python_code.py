import smtplib
import datetime
import pandas
import csv
import os
#os.chdir(r"C:\Users\MUHAMMAD WALEED\AppData\Local\Programs\Python\Python312")  # This line is for applying Task Scheduler

def send_email(Email,Subject,Message):
    try:
        API = 'smtp.gmail.com'
        Gmail = 'waleedkamal801@gmail.com'
        Password = 'kuep ufnk icfr pmwi'
        Port = 587
        mail =smtplib.SMTP(API,Port)
        mail.starttls()
        mail.login(Gmail,Password)
        email = f"Subject:{Subject}\n\n{Message}"
        mail.sendmail(Gmail,Email,email)
        mail.quit()
        print(f"Email Successfully Sent to {Email}")
    except:
        print(f"Email not Sent to {Email}")

def email_send():
    #Message = ""
    f = datetime.datetime.today().strftime('%A')
    g = pandas.read_csv('Email_file.csv')
    h = pandas.read_csv('Quotes_File.csv')
    Subject = "Todays Quotes"
    Message = h.loc[0,"Quotes"]
    for i,u in g.iterrows():
        if u["Day"] == f:
            Email = u["Email"]
            '''for t,p in h.iterrows():
                Subject = "Todays Quotes"
                Message = Message + p["Quotes"]'''
            send_email(Email,Subject,Message)

if __name__=="__main__":
    email_send()

