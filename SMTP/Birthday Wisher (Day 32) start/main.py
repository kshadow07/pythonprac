import smtplib

email = "QDQAWdwqadq@gmail.com"
password = "dfwfdwefwefwe"

#Write a program to send email
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=email,
        msg="Subject:hello\n\nThis is the body of my email"
    )


    
    