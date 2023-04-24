import random
import smtplib

def send_email(to_email, subject, body):
    from_email = "guptavaishu1310@gmail.com"
    password = "dtrkljedlgvnfyno"
    message = f"Subjesarict: {subject}\n\n{body}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, message)
    server.quit()


otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
user_email = input("Enter your email: ")
send_email(user_email, "OTP Verification", f"Your OTP is: {otp}")

user_otp = input("Enter the OTP you received: ")
if user_otp == otp:
    print("User verified successfully!")
else:
    print("Invalid OTP. Please try again.")
