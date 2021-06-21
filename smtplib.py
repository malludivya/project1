import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
try:
    
   server.login("yourgmailcount@gmail.com","entr password")
   server.sendmail("from gmail","to gmail","enter the text ex:hlo,how r u")
except:
    print("eof error")
server.quit()
    
