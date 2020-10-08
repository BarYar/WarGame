import smtplib, ssl

port = 465  # For SSL

# Create a secure SSL context
context = ssl.create_default_context()
b=False
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    while not b:
        try:
            password = input("Type your password and press enter: ")
            server.login("cardgame1j@gmail.com", password)
        except:
            print("Invalid Password.")
        else:
            b=True
    sender_email = "cardgame1j@gmail@gmail.com"
    receiver_email = "baryar102030@gmail.com"
    message = "Hey"
    server.sendmail("cardgame1j@gmail@gmail.com","baryar102030@gmail.com","Hey")