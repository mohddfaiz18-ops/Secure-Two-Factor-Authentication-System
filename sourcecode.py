"""
Project Name: Secure Two-Factor Authentication (2FA) System
Code Type: Procedural Control Flow (While-Loop with Conditional Logic)
Based On: OWASP Security Best Practices (Authentication & Session Management)

Description: 
This script implements a secure terminal-based login system. It validates 
user credentials with generic error handling to prevent username enumeration, 
followed by a simulated time-delayed One-Time Password (OTP) verification layer.
"""
import random 
import time
import getpass
print("welcome faiz please login you account")
attempts = 3
while attempts>0:
    correct_user = "faizkhan"
    correct_pass = "mfaiz18"
    username = input("enter username:")
    password = getpass.getpass("enter password:")
    if username == correct_user and password == correct_pass:
        print("checking credential..")
        time.sleep(2)
        otp = str(random.randint(1000, 9999))
        print(f"your otp is:{otp}")
        user_otp = input("enter otp:")
        time.sleep(1)
        if user_otp == otp:
            print("verifying otp....")
            time.sleep(1)
            print("welcome faiz access granted...")
            break
        else:
          time.sleep(1)
          print("wrong otp..")
    else:
        time.sleep(1)
        print("invalid username or password")
    attempts -= 1
    if attempts>0:
        print(f"access denied...try again. {attempts} attempts left")
    else:
        print("maximum attempts reached.")
        print("locking account...")
        time.sleep(3)
        print("account locked.")
        
        
    
