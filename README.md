# Secure Two-Factor Authentication (2FA) System

## 1. Project Title

**Secure Two-Factor Authentication (2FA) System**

---

## 2. Overview

The Secure Two-Factor Authentication (2FA) System is a simple terminal-based Python program that demonstrates a two-step login process.

First, the user must enter a correct username and password. If the credentials are correct, the system generates a random One-Time Password (OTP). The user must enter the correct OTP to gain access.

The program also limits the number of login attempts to three. If all attempts fail, the system displays an account-lock message.

This project demonstrates basic Python programming concepts such as variables, loops, conditional statements, functions from Python libraries, random number generation, delays, and secure password input.

> **Note:** This project is an educational simulation of a 2FA system. It is not intended for production authentication because the credentials are hard-coded and the OTP is displayed in the terminal.

---

## 3. Features

### 3.1 Username and Password Verification
- Requests a username and password from the user.
- Checks the entered credentials against the stored credentials.
- Uses `getpass` to hide the password while it is being entered.

### 3.2 OTP Verification
- Generates a random 4-digit OTP after successful credential verification.
- Requests the user to enter the generated OTP.
- Grants access only when the entered OTP matches the generated OTP.

### 3.3 Login Attempt Limit
- Allows a maximum of three login attempts.
- Displays the number of remaining attempts after an unsuccessful login.

### 3.4 Account Lock Simulation
- After three unsuccessful attempts, the program displays an account-lock message.
- A short delay is added to simulate the locking process.

### 3.5 Time Delays
The `time.sleep()` function is used to simulate:
- Credential checking
- OTP verification
- Account locking

---

## 4. Technologies / Tools Used

### Programming Language
- Python

### Python Modules
- `random` - used to generate the OTP.
- `time` - used to create delays.
- `getpass` - used to hide password input in the terminal.

### Development Environment
- Visual Studio Code
- Python Terminal / Command Prompt



## 5. Project Structure

text
Secure-2FA-System/
│
├── main.py
├── README.md
├── statement.md
└── screenshots/
    ├── login.png
    ├── otp_verification.png
    ├── access_granted.png
    └── account_locked.png
