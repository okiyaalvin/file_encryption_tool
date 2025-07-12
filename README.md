# 🔐 Encryption App — Secure Login and File Encryption System

This project provides a simple UI-based system that allows users to **create accounts**, **log in**, and **securely encrypt/decrypt data** using strong cryptographic techniques.

---

## 🗂️ Project Structure

- `main.py`: The main application file. Handles the **user interface** and authentication flow (login and account creation).
- `encrypt.py`: Contains all **encryption and decryption logic** using the Fernet algorithm.
- UI module: Built into `main.py`, includes the authentication interface and logic.

---

## ✅ Features

- User can **create a new account**
- User can **log in** with valid credentials
- Upon successful authentication, the system enables:
  - **Encryption of sensitive data**
  - **Decryption of previously encrypted data**

---

## 🔒 Encryption Algorithm

This project uses the **Fernet** encryption algorithm, which is part of the `cryptography` library.

- Fernet is built on **AES 128-bit encryption** in **CBC mode (Cipher Block Chaining)** with PKCS7 padding.
- It ensures that:
  - Data cannot be read or altered without the encryption key
  - Encrypted data includes a message authentication code (MAC) for tamper detection

This makes Fernet a **secure, authenticated, symmetric encryption method** suitable for encrypting user data.

---

## 🛠️ Prerequisites

Install the required libraries before running the app:

```bash
pip install cryptography pycryptodome
