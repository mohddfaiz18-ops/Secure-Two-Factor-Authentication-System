
# Project Statement

## 1. Problem Statement

Basic password-only authentication may not provide an additional verification step for accessing an account.

The **Secure Two-Factor Authentication (2FA) System** is designed to demonstrate a simple two-step authentication process in which the user must first provide valid login credentials and then verify a randomly generated One-Time Password (OTP).

The system also limits login attempts and simulates account locking after repeated failures.

---

## 2. Scope of the Project

The project focuses on demonstrating basic authentication and two-factor verification using Python.

The system includes:

- Username and password verification.
- Password masking during input.
- Random OTP generation.
- OTP verification.
- Maximum login attempt limit.
- Account-lock simulation.
- Time delays during authentication.

The project is designed as an educational terminal-based application.

---

## 3. Target Users

The project is intended for:

- Students learning Python.
- Beginners learning authentication concepts.
- Users studying basic cybersecurity concepts.
- Students demonstrating procedural programming and control flow.

---

## 4. High-Level Features

### User Authentication
Verifies the username and password entered by the user.

### Password Protection
Uses Python's `getpass` module to hide the password during terminal input.

### OTP Verification
Generates a random 4-digit OTP and requires the user to enter it for additional verification.

### Login Attempt Control
Limits the number of authentication attempts to three.

### Account Lock Simulation
Displays an account-lock message when the maximum number of failed attempts is reached.

### Authentication Delays
Uses the `time` module to introduce delays during credential checking, OTP verification, and account locking.

---

## 5. Technologies Used

- **Python**
- `random` module
- `time` module
- `getpass` module
- Visual Studio Code

---

## 6. Project Limitations

This project is an educational demonstration and is not a production-ready authentication system.

The current version:

- Uses hard-coded credentials.
- Displays the OTP directly in the terminal.
- Does not store users in a database.
- Does not use password hashing.
- Does not send OTP through email or SMS.
- Does not implement a permanent account-lock mechanism.

