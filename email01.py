import smtplib

price = '4000'
sender_email = "rajextc225@gmail.com"
rec_email = "rajasmhatre93@gmail.com"
password = "ikvtvnfaavvqrmtb"
message = "hey, this was sent using python"+ price

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls() 
server.login(sender_email,password)
print("login sucess!")

server.sendmail(sender_email,rec_email,message)
print("email has been sent to receiver email")


    